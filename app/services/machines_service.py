"""
Service layer for health monitoring and machine management.
Provides the same functionality as machines_api.py but as service methods.
"""
import json
import math
import os
import sys
from typing import Dict, Any, List

# Import centralized logging and configuration
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.logger_config import get_logger
from config.app_config import config
logger = get_logger(__name__)

# Add the parent directory to the path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.predictor import MaintenancePredictor
from utils.data_loader import DataLoader
from client.swe_client import superwise_client, SuperwiseRequest, MachineAnalysisRequest, SuperwiseResponse


class ServiceException(Exception):
    """Custom exception for service layer errors."""
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class MachinesService:
    """Service class for machine management and health monitoring."""
    
    def __init__(self):
        """Initialize the service with required dependencies."""
        self.predictor = MaintenancePredictor()
        self.data_loader = DataLoader()
        logger.info("MachinesService initialized successfully")
    
    def sanitize_float(self, value):
        """Sanitize float values to ensure JSON compliance."""
        if isinstance(value, (int, float)):
            if math.isnan(value):
                return 0.0
            elif math.isinf(value):
                return 999999.0 if value > 0 else -999999.0
            else:
                return float(value)
        return value
    
    def get_root_info(self) -> Dict[str, Any]:
        """Get root information about the service."""
        logger.info("Root service method accessed")
        return {
            "message": "Manufacturing Predictive Maintenance Service",
            "version": "1.0.0",
            "endpoints": {
                "health": "health_check",
                "status": "system_status",
                "machines": "get_machines",
                "machine_details": "get_machine_details",
                "superwise_ask": "ask_superwise_ai",
            }
        }
    
    def health_check(self) -> Dict[str, str]:
        """Health check service method."""
        logger.info("Health check service method accessed")
        return {"status": "healthy", "service": "maintenance-ai-service"}
    
    def system_status(self) -> Dict[str, Any]:
        """Get overall system status and health metrics."""
        logger.info("System status service method accessed")
        try:
            logger.debug("Retrieving system status information")
            status_data = {
                "status": "operational",
                "uptime": "99.9%",
                "last_check": "2024-01-01T12:00:00Z",
                "services": {
                    "database": "healthy",
                    "prediction_engine": "healthy",
                    "data_loader": "healthy"
                }
            }
            logger.info("System status retrieved successfully")
            return status_data
        except Exception as e:
            logger.error(f"Failed to get system status: {str(e)}")
            raise ServiceException(f"Failed to get system status: {str(e)}", 500)
    
    def get_machines(self) -> Dict[str, List[Dict[str, Any]]]:
        """Get list of all machines and their current status."""
        logger.info("Machines service method accessed")
        try:
            logger.debug("Loading latest sensor data")
            latest_data = self.data_loader.get_latest_sensor_data()
            logger.info(f"Loaded sensor data for {len(latest_data)} machines")
            
            # Extract all machine IDs for batch analysis
            machine_ids = latest_data['machine_id'].tolist()
            logger.debug(f"Collected {len(machine_ids)} machine IDs for batch analysis: {machine_ids}")
            
            # Try Superwise AI batch analysis first
            risk_assessments = {}
            superwise_success_count = 0
            fallback_count = 0
            
            try:
                logger.debug(f"Attempting Superwise AI batch analysis for {len(machine_ids)} machines")
                batch_response = superwise_client.analyze_machine_failure_risk(machine_ids=machine_ids)
                
                # Check if we got individual risk assessments for each machine
                if isinstance(batch_response, dict) and all(mid in batch_response for mid in machine_ids):
                    risk_assessments = batch_response
                    superwise_success_count = len(machine_ids)
                    logger.info(f"Superwise AI batch analysis successful for all {len(machine_ids)} machines")
                else:
                    # If batch response doesn't contain all machines, fall back to individual analysis
                    logger.warning("Batch response incomplete, falling back to individual analysis")
                    raise Exception("Incomplete batch response")
                    
            except Exception as e:
                logger.warning(f"Superwise AI batch analysis failed: {str(e)}")
                logger.debug("Falling back to individual machine analysis")
                
                # Fallback to individual analysis for each machine
                for machine_id in machine_ids:
                    try:
                        logger.debug(f"Attempting individual Superwise AI analysis for machine {machine_id}")
                        response = superwise_client.analyze_machine_failure_risk(machine_id=machine_id)
                        risk_assessments[machine_id] = response['risk_level']
                        superwise_success_count += 1
                        logger.info(f"Individual Superwise AI analysis successful for machine {machine_id}")
                    except Exception as individual_e:
                        logger.warning(f"Individual Superwise AI failed for machine {machine_id}: {str(individual_e)}")
                        # Use local predictor as final fallback
                        machine_data = latest_data[latest_data['machine_id'] == machine_id].iloc[0]
                        sensor_dict = machine_data.to_dict()
                        prediction = self.predictor.calculate_failure_risk(sensor_dict)
                        risk_assessments[machine_id] = prediction['failure_risk']
                        fallback_count += 1
                        logger.info(f"Fallback analysis for machine {machine_id}: {risk_assessments[machine_id]}")
            
            # Build the final machines list
            machines = []
            for _, row in latest_data.iterrows():
                machine_id = row['machine_id']
                status = risk_assessments.get(machine_id, "Unknown")
                
                machine_data = {
                    "machine_id": machine_id,
                    "status": status,
                    "last_reading": row['timestamp'].isoformat(),
                    "vibration": self.sanitize_float(row['vibration']),
                    "temperature": self.sanitize_float(row['temperature']),
                    "current": self.sanitize_float(row['current']),
                    "pressure": self.sanitize_float(row['pressure']),
                    "operating_hours": self.sanitize_float(row['operating_hours'])
                }
                machines.append(machine_data)
                logger.debug(f"Added machine data for {machine_id} with status {status}")
            
            logger.info(f"Successfully processed {len(machines)} machines - Superwise AI: {superwise_success_count}, Fallback: {fallback_count}")
            return {"machines": machines}
        
        except Exception as e:
            logger.error(f"Failed to get machines: {str(e)}")
            raise ServiceException(f"Failed to get machines: {str(e)}", 500)
    
    def get_machine_details(self, machine_id: str) -> Dict[str, Any]:
        """Get detailed information for a specific machine."""
        logger.info(f"Machine details service method accessed for machine: {machine_id}")
        try:
            logger.debug(f"Loading machine history for {machine_id}")
            # Get machine history
            history = self.data_loader.get_machine_history(machine_id)
            
            if history.empty:
                logger.warning(f"Machine {machine_id} not found")
                raise ServiceException("Machine not found", 404)
            
            logger.info(f"Found {len(history)} history points for machine {machine_id}")
            
            # Get latest data and prediction
            latest_data = history.iloc[-1].to_dict()
            logger.debug(f"Latest data for {machine_id}: {latest_data}")
            
            logger.debug(f"Calculating failure risk for {machine_id}")
            prediction = self.predictor.calculate_failure_risk(latest_data)
            
            # Calculate cost savings
            logger.debug(f"Calculating cost savings for {machine_id}")
            cost_savings = self.predictor.calculate_cost_savings(prediction['predicted_days_to_failure'])
            
            # Sanitize prediction values
            sanitized_prediction = {
                "machine_id": prediction.get("machine_id", machine_id),
                "failure_risk": prediction.get("failure_risk", "Unknown"),
                "risk_score": self.sanitize_float(prediction.get("risk_score", 0)),
                "reason": prediction.get("reason", ""),
                "predicted_days_to_failure": self.sanitize_float(prediction.get("predicted_days_to_failure", 0)),
                "confidence": self.sanitize_float(prediction.get("confidence", 0)),
                "recommendations": prediction.get("recommendations", [])
            }
            
            # Sanitize cost savings values
            sanitized_cost_savings = {
                "savings": self.sanitize_float(cost_savings.get("savings", 0)),
                "planned_maintenance_cost": self.sanitize_float(cost_savings.get("planned_maintenance_cost", 0)),
                "unplanned_downtime_cost": self.sanitize_float(cost_savings.get("unplanned_downtime_cost", 0)),
                "downtime_hours": self.sanitize_float(cost_savings.get("downtime_hours", 0))
            }
            
            result = {
                "machine_id": machine_id,
                "current_status": sanitized_prediction,
                "cost_savings": sanitized_cost_savings,
                "history_points": len(history),
                "latest_reading": latest_data['timestamp'].isoformat()
            }
            
            logger.info(f"Successfully retrieved details for machine {machine_id}")
            return result
        
        except ServiceException:
            raise
        except Exception as e:
            logger.error(f"Failed to get machine details for {machine_id}: {str(e)}")
            raise ServiceException(f"Failed to get machine details: {str(e)}", 500)
    
    def ask_superwise_ai(self, request: SuperwiseRequest) -> SuperwiseResponse:
        """
        Ask a question to Superwise AI.
        
        Args:
            request: Question and optional chat history
            
        Returns:
            AI response from Superwise
        """
        logger.info(f"Superwise AI ask service method accessed with question: {request.question[:100]}...")
        try:
            logger.debug(f"Question: {request.question}")
            logger.debug(f"Chat history length: {len(request.chat_history)}")
            
            response = superwise_client.ask_question(
                question=request.question,
                chat_history=request.chat_history
            )
            
            logger.info(f"Superwise AI response received: {response}")
            
            # Extract risk level from the AI response
            ai_response = response.get('response', '')
                    
            result = SuperwiseResponse(output=ai_response, risk_level='')
            logger.info("Superwise AI ask request completed successfully")
            return result
        
        except Exception as e:
            logger.error(f"Superwise AI ask request failed: {str(e)}")
            raise ServiceException(f"Superwise AI request failed: {str(e)}", 500)


# Create a singleton instance for easy access
machines_service = MachinesService()

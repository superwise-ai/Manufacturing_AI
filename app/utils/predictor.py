"""
Predictive maintenance logic and failure prediction algorithms.
"""
import numpy as np
from typing import Dict, Any, List
from datetime import datetime, timedelta

# Import centralized logging and configuration
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from logger_config import get_logger
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.app_config import config
logger = get_logger(__name__)


class MaintenancePredictor:
    """Handles predictive maintenance calculations and failure predictions."""
    
    def __init__(self):
        # Use thresholds from configuration
        self.thresholds = config.RISK_THRESHOLDS
        logger.info("MaintenancePredictor initialized with configuration thresholds")
    
    def calculate_failure_risk(self, sensor_data: Dict[str, float]) -> Dict[str, Any]:
        """
        Calculate failure risk based on sensor data.
        
        Args:
            sensor_data: Dictionary containing sensor readings
            
        Returns:
            Dictionary with risk assessment and prediction
        """
        machine_id = sensor_data.get('machine_id', 'Unknown')
        vibration = sensor_data.get('vibration', 0)
        temperature = sensor_data.get('temperature', 0)
        current = sensor_data.get('current', 0)
        pressure = sensor_data.get('pressure', 0)
        operating_hours = sensor_data.get('operating_hours', 0)
        
        # Calculate individual risk scores
        vibration_risk = self._calculate_parameter_risk(vibration, 'vibration')
        temperature_risk = self._calculate_parameter_risk(temperature, 'temperature')
        current_risk = self._calculate_parameter_risk(current, 'current')
        pressure_risk = self._calculate_parameter_risk(pressure, 'pressure')
        
        # Calculate overall risk score (weighted average)
        weights = {'vibration': 0.3, 'temperature': 0.25, 'current': 0.25, 'pressure': 0.2}
        overall_risk = (
            vibration_risk * weights['vibration'] +
            temperature_risk * weights['temperature'] +
            current_risk * weights['current'] +
            pressure_risk * weights['pressure']
        )
        
        # Determine risk level
        if overall_risk >= 0.8:
            risk_level = "High"
            days_to_failure = max(1, int(10 * (1 - overall_risk)))
        elif overall_risk >= 0.5:
            risk_level = "Medium"
            days_to_failure = max(5, int(30 * (1 - overall_risk)))
        else:
            risk_level = "Low"
            days_to_failure = max(30, int(90 * (1 - overall_risk)))
        
        # Generate reason for prediction
        reason = self._generate_reason(
            vibration, temperature, current, pressure,
            vibration_risk, temperature_risk, current_risk, pressure_risk
        )
        
        return {
            "machine_id": machine_id,
            "failure_risk": risk_level,
            "risk_score": round(overall_risk, 2),
            "reason": reason,
            "predicted_days_to_failure": days_to_failure,
            "confidence": min(95, max(60, int(overall_risk * 100))),
            "recommendations": self._generate_recommendations(risk_level, sensor_data)
        }
    
    def _calculate_parameter_risk(self, value: float, parameter: str) -> float:
        """Calculate risk score for a single parameter."""
        thresholds = self.thresholds[parameter]
        
        if value <= thresholds['low']:
            return 0.2
        elif value <= thresholds['medium']:
            return 0.5
        elif value <= thresholds['high']:
            return 0.8
        else:
            return 1.0
    
    def _generate_reason(self, vibration: float, temperature: float, 
                        current: float, pressure: float,
                        v_risk: float, t_risk: float, c_risk: float, p_risk: float) -> str:
        """Generate human-readable reason for the prediction."""
        reasons = []
        
        if v_risk >= 0.8:
            reasons.append(f"Vibration exceeded {self.thresholds['vibration']['high']} g")
        if t_risk >= 0.8:
            reasons.append(f"Temperature rose above {self.thresholds['temperature']['high']}°C")
        if c_risk >= 0.8:
            reasons.append(f"Current consumption above {self.thresholds['current']['high']} A")
        if p_risk >= 0.8:
            reasons.append(f"Pressure exceeded {self.thresholds['pressure']['high']} bar")
        
        if not reasons:
            return "All parameters within normal operating ranges"
        
        return " and ".join(reasons)
    
    def _generate_recommendations(self, risk_level: str, sensor_data: Dict[str, float]) -> List[str]:
        """Generate maintenance recommendations based on risk level."""
        recommendations = []
        
        if risk_level == "High":
            recommendations.extend([
                "Schedule immediate maintenance",
                "Consider reducing machine load",
                "Monitor continuously for changes"
            ])
        elif risk_level == "Medium":
            recommendations.extend([
                "Schedule maintenance within 1-2 weeks",
                "Increase monitoring frequency",
                "Check for unusual patterns"
            ])
        else:
            recommendations.extend([
                "Continue regular monitoring",
                "Schedule routine maintenance as planned"
            ])
        
        return recommendations
    
    def calculate_cost_savings(self, predicted_failure_days: int, 
                             unplanned_downtime_cost: float = 10000) -> Dict[str, float]:
        """Calculate potential cost savings from predictive maintenance."""
        if predicted_failure_days <= 0:
            return {"savings": 0, "downtime_cost": unplanned_downtime_cost}
        
        # Cost of planned maintenance vs unplanned downtime
        planned_maintenance_cost = 2000  # Average cost of planned maintenance
        downtime_hours = 24  # Hours of downtime for unplanned failure
        
        savings = unplanned_downtime_cost - planned_maintenance_cost
        
        return {
            "savings": savings,
            "planned_maintenance_cost": planned_maintenance_cost,
            "unplanned_downtime_cost": unplanned_downtime_cost,
            "downtime_hours": downtime_hours
        }

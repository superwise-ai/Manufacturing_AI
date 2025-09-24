"""
Data loading utilities for sensor data and maintenance records.
"""
import pandas as pd
import os
from typing import Dict, List, Optional, Any

# Import centralized logging and configuration
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from logger_config import get_logger
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.app_config import config
logger = get_logger(__name__)


class DataLoader:
    """Handles loading and processing of sensor data and maintenance records."""
    
    def __init__(self, data_dir: str = None):
        self.data_dir = data_dir or config.DATA_DIR
        self.sensor_data = None
        self.maintenance_data = None
        logger.info(f"DataLoader initialized with data directory: {self.data_dir}")
    
    def load_sensor_data(self) -> pd.DataFrame:
        """Load synthetic sensor data from CSV."""
        logger.debug("Loading sensor data")
        if self.sensor_data is None:
            file_path = os.path.join(self.data_dir, "synthetic_sensor_data.csv")
            logger.debug(f"Loading sensor data from: {file_path}")
            self.sensor_data = pd.read_csv(file_path)
            self.sensor_data['timestamp'] = pd.to_datetime(self.sensor_data['timestamp'])
            logger.info(f"Loaded {len(self.sensor_data)} sensor data records")
        else:
            logger.debug("Using cached sensor data")
        return self.sensor_data
    
    def load_maintenance_data(self) -> pd.DataFrame:
        """Load maintenance records from CSV."""
        if self.maintenance_data is None:
            file_path = os.path.join(self.data_dir, "synthetic_maintenance_records.csv")
            self.maintenance_data = pd.read_csv(file_path)
            self.maintenance_data['last_service_date'] = pd.to_datetime(self.maintenance_data['last_service_date'])
            self.maintenance_data['next_service_due'] = pd.to_datetime(self.maintenance_data['next_service_due'])
        return self.maintenance_data
    
    def get_latest_sensor_data(self) -> pd.DataFrame:
        """Get the most recent sensor readings for each machine."""
        sensor_data = self.load_sensor_data()
        latest_data = sensor_data.groupby('machine_id').last().reset_index()
        return latest_data
    
    
    def get_machine_history(self, machine_id: str) -> pd.DataFrame:
        """Get historical data for a specific machine."""
        sensor_data = self.load_sensor_data()
        return sensor_data[sensor_data['machine_id'] == machine_id].sort_values('timestamp')
    
    def get_maintenance_schedule(self) -> pd.DataFrame:
        """Get upcoming maintenance schedule."""
        maintenance_data = self.load_maintenance_data()
        return maintenance_data.sort_values('next_service_due')
    
    def get_machines_overdue(self) -> List[str]:
        """Get list of machines that are overdue for maintenance."""
        from datetime import datetime
        maintenance_data = self.load_maintenance_data()
        today = datetime.now()
        overdue = maintenance_data[maintenance_data['next_service_due'] < today]
        return overdue['machine_id'].tolist()
    
    def get_machine_maintenance_data(self, machine_id: str) -> Optional[Dict[str, Any]]:
        """Get maintenance data for a specific machine."""
        maintenance_data = self.load_maintenance_data()
        machine_maintenance = maintenance_data[maintenance_data['machine_id'] == machine_id]
        
        if machine_maintenance.empty:
            logger.warning(f"No maintenance data found for machine {machine_id}")
            return None
        
        # Get the most recent maintenance record
        latest_maintenance = machine_maintenance.iloc[-1].to_dict()
        
        return {
            "machine_id": machine_id,
            "last_service_date": latest_maintenance['last_service_date'],
            "service_notes": latest_maintenance['service_notes'],
            "next_service_due": latest_maintenance['next_service_due'],
            "service_cost": latest_maintenance['service_cost']
        }
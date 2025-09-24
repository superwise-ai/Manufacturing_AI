"""
Tests for the Streamlit dashboard components.
"""
import pytest
import pandas as pd
import sys
import os

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utils.data_loader import DataLoader
from app.utils.predictor import MaintenancePredictor

def test_data_loader():
    """Test the DataLoader class."""
    loader = DataLoader()
    
    # Test loading sensor data
    sensor_data = loader.load_sensor_data()
    assert isinstance(sensor_data, pd.DataFrame)
    assert not sensor_data.empty
    assert 'machine_id' in sensor_data.columns
    assert 'vibration' in sensor_data.columns
    assert 'temperature' in sensor_data.columns
    
    # Test loading maintenance data
    maintenance_data = loader.load_maintenance_data()
    assert isinstance(maintenance_data, pd.DataFrame)
    assert not maintenance_data.empty
    assert 'machine_id' in maintenance_data.columns
    assert 'last_service_date' in maintenance_data.columns
    
    # Test getting latest sensor data
    latest_data = loader.get_latest_sensor_data()
    assert isinstance(latest_data, pd.DataFrame)
    assert not latest_data.empty
    
    # Test getting machine history
    history = loader.get_machine_history('CNC_1')
    assert isinstance(history, pd.DataFrame)

def test_predictor():
    """Test the MaintenancePredictor class."""
    predictor = MaintenancePredictor()
    
    # Test with sample sensor data
    sample_data = {
        'machine_id': 'CNC_1',
        'vibration': 1.5,
        'temperature': 75.0,
        'current': 13.0,
        'pressure': 2.3,
        'operating_hours': 1200
    }
    
    prediction = predictor.calculate_failure_risk(sample_data)
    
    # Check required fields
    assert 'machine_id' in prediction
    assert 'failure_risk' in prediction
    assert 'risk_score' in prediction
    assert 'reason' in prediction
    assert 'predicted_days_to_failure' in prediction
    assert 'confidence' in prediction
    assert 'recommendations' in prediction
    
    # Check data types
    assert isinstance(prediction['machine_id'], str)
    assert isinstance(prediction['failure_risk'], str)
    assert isinstance(prediction['risk_score'], (int, float))
    assert isinstance(prediction['reason'], str)
    assert isinstance(prediction['predicted_days_to_failure'], int)
    assert isinstance(prediction['confidence'], int)
    assert isinstance(prediction['recommendations'], list)
    
    # Check risk level is valid
    assert prediction['failure_risk'] in ['Low', 'Medium', 'High']
    
    # Check risk score is between 0 and 1
    assert 0 <= prediction['risk_score'] <= 1
    
    # Check confidence is between 0 and 100
    assert 0 <= prediction['confidence'] <= 100

def test_predictor_edge_cases():
    """Test predictor with edge cases."""
    predictor = MaintenancePredictor()
    
    # Test with extreme values
    extreme_data = {
        'machine_id': 'CNC_1',
        'vibration': 5.0,  # Very high
        'temperature': 120.0,  # Very high
        'current': 25.0,  # Very high
        'pressure': 5.0,  # Very high
        'operating_hours': 10000
    }
    
    prediction = predictor.calculate_failure_risk(extreme_data)
    assert prediction['failure_risk'] == 'High'
    assert prediction['risk_score'] >= 0.8
    
    # Test with very low values
    low_data = {
        'machine_id': 'CNC_1',
        'vibration': 0.5,
        'temperature': 50.0,
        'current': 8.0,
        'pressure': 1.0,
        'operating_hours': 100
    }
    
    prediction = predictor.calculate_failure_risk(low_data)
    assert prediction['failure_risk'] == 'Low'
    assert prediction['risk_score'] <= 0.5

def test_cost_savings_calculation():
    """Test cost savings calculation."""
    predictor = MaintenancePredictor()
    
    # Test with different failure predictions
    savings_1 = predictor.calculate_cost_savings(5)  # 5 days to failure
    assert 'savings' in savings_1
    assert 'planned_maintenance_cost' in savings_1
    assert 'unplanned_downtime_cost' in savings_1
    assert savings_1['savings'] > 0
    
    savings_2 = predictor.calculate_cost_savings(0)  # Immediate failure
    assert savings_2['savings'] == 0

def test_data_consistency():
    """Test data consistency between loader and predictor."""
    loader = DataLoader()
    predictor = MaintenancePredictor()
    
    # Get latest sensor data
    latest_data = loader.get_latest_sensor_data()
    
    # Test prediction for each machine
    for _, row in latest_data.iterrows():
        sensor_dict = row.to_dict()
        prediction = predictor.calculate_failure_risk(sensor_dict)
        
        # Check that machine_id matches
        assert prediction['machine_id'] == row['machine_id']
        
        # Check that prediction is valid
        assert prediction['failure_risk'] in ['Low', 'Medium', 'High']
        assert 0 <= prediction['risk_score'] <= 1
        assert prediction['predicted_days_to_failure'] > 0

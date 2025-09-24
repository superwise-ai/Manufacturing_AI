"""
Tests for the health API endpoints.
"""
import pytest
import requests
import json
import sys
import os

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.machines_service import MachinesService

# Create service instance
service = MachinesService()

def test_root_endpoint():
    """Test the root endpoint."""
    response = service.get_root_info()
    assert "message" in response
    assert "version" in response
    assert response["message"] == "Manufacturing Predictive Maintenance Service"
    assert response["version"] == "1.0.0"

def test_health_check():
    """Test the health check endpoint."""
    response = service.health_check()
    assert response["status"] == "healthy"
    assert response["service"] == "maintenance-ai-service"

def test_machines_endpoint():
    """Test the machines endpoint."""
    response = service.get_machines()
    assert "machines" in response
    assert isinstance(response["machines"], list)

def test_machine_details_endpoint():
    """Test the machine details endpoint."""
    response = service.get_machine_details("CNC_1")
    assert "machine_id" in response
    assert "current_status" in response
    assert "cost_savings" in response
    assert response["machine_id"] == "CNC_1"

def test_machine_details_not_found():
    """Test machine details endpoint with non-existent machine."""
    with pytest.raises(Exception) as exc_info:
        service.get_machine_details("NONEXISTENT")
    assert "Machine not found" in str(exc_info.value)

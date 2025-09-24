"""
Machines Page for Manufacturing Predictive Maintenance Dashboard

This page displays the machine status table for all machines and links to machine details.
"""

import streamlit as st
import json
from datetime import datetime, timedelta
import os
import sys
import time

# Import centralized logging and configuration
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.logger_config import get_logger
from config.front_end_config import frontend_config
from services.machines_service import machines_service, ServiceException
from machine_details import show_machine_details_content, show_machine_details_page
from header import create_header

logger = get_logger(__name__)

@st.cache_data(ttl=frontend_config.CACHE_TTL)
def get_service_data(method_name, *args, **kwargs):
    """Helper function to get data from service with error handling."""
    logger.debug(f"Calling service method: {method_name}")
    try:
        method = getattr(machines_service, method_name)
        result = method(*args, **kwargs)
        logger.debug(f"Service method {method_name} successful")
        return result
    except ServiceException as e:
        logger.error(f"Service Error for {method_name}: {str(e)}")
        st.error(f"Service Error: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error for {method_name}: {str(e)}")
        st.error(f"Unexpected error: {str(e)}")
        return None

def get_machine_status_color(status):
    """Get color based on machine status."""
    return frontend_config.get_status_colors().get(status, "#757575")

def show_custom_loader(message="Loading Machines", submessage="Please wait while we fetch machine data"):
    """Show custom loader with blue effect."""
    st.markdown(f"""
    <div class="custom-loader-container">
        <div class="custom-loader"></div>
        <div class="custom-loader-text">{message}</div>
        <div class="custom-loader-subtext">{submessage}</div>
    </div>
    """, unsafe_allow_html=True)

def show_machines_page():
    """Show the machines page with status table."""
    logger.info("Machines page started")
    
    # Load CSS styles
    from utils.css_styles import get_dashboard_styles
    st.markdown(get_dashboard_styles(), unsafe_allow_html=True)
    
    # Create a placeholder for the loader
    loader_placeholder = st.empty()
    
    # Show loader
    with loader_placeholder.container():
        show_custom_loader("Loading Machines", "Fetching machine data and status information...")
    
     # Get machine data
    logger.info("Loading machine data from API")
    machines_data = get_service_data("get_machines")
    
    if machines_data is None:
        loader_placeholder.empty()
        st.error("Failed to load machine data")
        return
    
    machines = machines_data.get("machines", [])
    
    # Clear the loader
    loader_placeholder.empty()
    
    # Professional Machine Status Table
    st.markdown("""
    <div class="machines-table-container">
        <div class="section-heading">Machine Status</div>
    """, unsafe_allow_html=True)
    
    # Create a professional table header
    st.markdown("""
    <div class="machines-table-header">
        <div class="table-header-row">
            <div class="table-header-cell machine-id-header">Machine ID</div>
            <div class="table-header-cell status-header">Status</div>
            <div class="table-header-cell last-reading-header">Last Reading</div>
            <div class="table-header-cell temperature-header">Temperature</div>
            <div class="table-header-cell vibration-header">Vibration</div>
            <div class="table-header-cell current-header">Current</div>
            <div class="table-header-cell pressure-header">Pressure</div>
            <div class="table-header-cell actions-header">Actions</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Display each machine as a professional row with Streamlit buttons
    for i, machine in enumerate(machines):
        # Color code based on status
        status_color = get_machine_status_color(machine['status'])
        status_icon = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}.get(machine['status'], "⚪")
        
        # Create a single row with proper grid alignment
        st.markdown(f"""
        <div class="machines-table-row {'even' if i % 2 == 0 else 'odd'}">
            <div class="table-cell machine-id-cell">
                <span class="machine-id-text" style="color: {status_color}; font-weight: 700;">{machine['machine_id']}</span>
            </div>
            <div class="table-cell status-cell">
                <span class="status-badge status-{machine['status'].lower()}" style="color: {status_color};">
                    {status_icon} {machine['status']}
                </span>
            </div>
            <div class="table-cell last-reading-cell">
                <span class="reading-text">{machine['last_reading']}</span>
            </div>
            <div class="table-cell temperature-cell">
                <span class="metric-value temperature-value">{machine['temperature']:.1f}°C</span>
            </div>
            <div class="table-cell vibration-cell">
                <span class="metric-value vibration-value">{machine['vibration']:.1f}</span>
            </div>
            <div class="table-cell current-cell">
                <span class="metric-value current-value">{machine['current']:.1f}A</span>
            </div>
            <div class="table-cell pressure-cell">
                <span class="metric-value pressure-value">{machine['pressure']:.1f} bar</span>
            </div>
            <div class="table-cell actions-cell">
                <a href="?page=machine_details&machine_id={machine['machine_id']}" target="_self" class="view-details-link">
                    View Details
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Close the table container
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)
    
    
    # Add some spacing
    st.markdown("")
    
    # Footer
    footer_config = frontend_config.get_footer_config()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"""
    <div class="footer">
        <div class="footer-links">
            <a href="#" onclick="window.location.reload()">Refresh Page</a>
        </div>
        <div>
            <strong>Manufacturing Predictive Maintenance AI {footer_config['app_version']}</strong> | 
            {footer_config['powered_by']} | 
            Last Updated: {current_time}
        </div>
    </div>
    """, unsafe_allow_html=True)


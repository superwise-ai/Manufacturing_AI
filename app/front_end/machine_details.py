"""
Machine Details Component
Handles the display of detailed machine information, status, and historical data.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import sys
import os

# Add the parent directory to the path to import data_loader
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.data_loader import DataLoader
from utils.logger_config import get_logger
from config.front_end_config import frontend_config
from services.machines_service import machines_service, ServiceException
from client.swe_client import SuperwiseRequest

# Initialize logger
logger = get_logger(__name__)

# Initialize data loader
data_loader = DataLoader()

def get_service_data(method_name, *args, **kwargs):
    """
    Get data from service method.
    
    Args:
        method_name (str): The service method to call
        *args: Arguments to pass to the service method
        **kwargs: Keyword arguments to pass to the service method
    """
    try:
        method = getattr(machines_service, method_name)
        result = method(*args, **kwargs)
        return result
    except ServiceException as e:
        st.error(f"Service Error: {str(e)}")
        return None
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        return None

def show_custom_loader(message="Loading Machine Details", submessage="Please wait while we fetch machine data"):
    """Show custom loader with blue effect."""
    st.markdown(f"""
    <div class="custom-loader-container">
        <div class="custom-loader"></div>
        <div class="custom-loader-text">{message}</div>
        <div class="custom-loader-subtext">{submessage}</div>
    </div>
    """, unsafe_allow_html=True)

def show_machine_details_content(selected_machine):
    """Show detailed view for a specific machine."""
    if 'superwise_response' in st.session_state:
        del st.session_state['superwise_response']
    # Get machine details with loading spinner
    with st.spinner(f"📡 Loading details for machine {selected_machine}..."):
        machine_details = get_service_data("get_machine_details", selected_machine)
        if machine_details is None:
            st.error("Unable to load machine details")
            return


    st.subheader(f"Machine: {selected_machine}")
    
    # Load historical data
    history = data_loader.get_machine_history(selected_machine)
    # Load maintenance data for the selected machine
    maintenance_data = data_loader.get_machine_maintenance_data(selected_machine)
    service_notes = maintenance_data.get('service_notes', '') if maintenance_data else ''
    
    # Clear the loader
    loader_placeholder = st.empty()

    # Historical data visualization
    if not history.empty:
        # Create 2x2 grid layout for the 4 separate graphs
        col1, col2 = st.columns(2)
        
        with col1:
            # Vibration Chart
            fig_vibration = go.Figure()
            fig_vibration.add_trace(
                go.Scatter(
                    x=history['timestamp'], 
                    y=history['vibration'], 
                    name='Vibration',
                    line=dict(color='#8b5cf6', width=2),
                    mode='lines+markers'
                )
            )
            fig_vibration.update_layout(
                title="Vibration (g)",
                xaxis_title="Time",
                yaxis_title="Vibration (g)",
                height=300,
                margin=dict(t=40, b=20, l=20, r=20),
                plot_bgcolor='white',
                paper_bgcolor='white'
            )
            st.plotly_chart(fig_vibration, use_container_width=True)
            
            # Current Chart
            fig_current = go.Figure()
            fig_current.add_trace(
                go.Scatter(
                    x=history['timestamp'], 
                    y=history['current'], 
                    name='Current',
                    line=dict(color='#f59e0b', width=2),
                    mode='lines+markers'
                )
            )
            fig_current.update_layout(
                title="Current (A)",
                xaxis_title="Time",
                yaxis_title="Current (A)",
                height=300,
                margin=dict(t=40, b=20, l=20, r=20),
                plot_bgcolor='white',
                paper_bgcolor='white'
            )
            st.plotly_chart(fig_current, use_container_width=True)
        
        with col2:
            # Temperature Chart
            fig_temperature = go.Figure()
            fig_temperature.add_trace(
                go.Scatter(
                    x=history['timestamp'], 
                    y=history['temperature'], 
                    name='Temperature',
                    line=dict(color='#ef4444', width=2),
                    mode='lines+markers'
                )
            )
            fig_temperature.update_layout(
                title="Temperature (°C)",
                xaxis_title="Time",
                yaxis_title="Temperature (°C)",
                height=300,
                margin=dict(t=40, b=20, l=20, r=20),
                plot_bgcolor='white',
                paper_bgcolor='white'
            )
            st.plotly_chart(fig_temperature, use_container_width=True)
            
            # Pressure Chart
            fig_pressure = go.Figure()
            fig_pressure.add_trace(
                go.Scatter(
                    x=history['timestamp'], 
                    y=history['pressure'], 
                    name='Pressure',
                    line=dict(color='#10b981', width=2),
                    mode='lines+markers'
                )
            )
            fig_pressure.update_layout(
                title="Pressure (bar)",
                xaxis_title="Time",
                yaxis_title="Pressure (bar)",
                height=300,
                margin=dict(t=40, b=20, l=20, r=20),
                plot_bgcolor='white',
                paper_bgcolor='white'
            )
            st.plotly_chart(fig_pressure, use_container_width=True)
    else:
        st.info("No historical data available for this machine.")

    # Superwise Integration Section
    st.markdown("### 🤖 Superwise AI Assistant")

    # Question input
    question = f"Analyze maintenance records and all sensor data for CNC machine with machine_id as {selected_machine} and service_notes as {service_notes}. Please suggest failure rate, predicted days to failure and next recommended service date."

    # Create columns for Ask Superwise button and response
    col1, col2 = st.columns([1, 3])
    
    with col1:
        if st.button("Generate Machine Report", key="ask_superwise_btn", type="primary"):
            if question.strip():
                # Show loading state
                with st.spinner("Analyzing machine data with Superwise AI..."):
                    request = SuperwiseRequest(question=question, chat_history=[])
                    response = get_service_data("ask_superwise_ai", request)
                    
                    if response and hasattr(response, 'output'):
                        response = {'output': response.output}
                        st.session_state['superwise_response'] = response
                        st.success("Superwise AI analysis completed!")
                    else:
                        st.error("Failed to get Superwise AI response")
            else:
                st.warning("Please enter a question for Superwise AI")
    
    with col2:
        if 'superwise_response' in st.session_state:
            st.markdown("**Superwise Response:**")
            # Enhanced display using Streamlit components
            st.subheader("🤖 AI Analysis Summary")
            response = st.session_state['superwise_response']
            logger.debug(f"Superwise response: {response}")
            if 'output' in response:
                st.markdown(response['output'])
            elif 'error' in response:
                st.error(response['error'])
            else:
                st.json(response)

def show_machine_details_page():
    """Show the machine details page with back button."""
    logger.info("Machine details page started")
    
    # Page-level loading spinner
    with st.spinner("🔄 Loading Machine Details..."):
        logger.debug("Loading CSS styles for machine details page")
        # Load CSS styles
        from utils.css_styles import get_dashboard_styles
        st.markdown(get_dashboard_styles(), unsafe_allow_html=True)
        logger.debug("CSS styles loaded successfully")
        
        # Show machine details if a machine is selected
        if st.session_state.selected_machine:
            selected_machine = st.session_state.selected_machine
            logger.info(f"Showing details for selected machine: {selected_machine}")
            
            # Load maintenance data for the title card
            maintenance_data = data_loader.get_machine_maintenance_data(selected_machine)
            service_notes = maintenance_data.get('service_notes', '') if maintenance_data else ''
            
            st.markdown(f"""
            <div class="machine-details-title-card">
                <div class="section-heading">Machine Details</div>
                <div class="machine-info-section">
                    <div class="machine-name-info">Machine: {selected_machine}</div>
                    <div class="service-notes-info">
                        <span class="service-notes-label">Last Service Notes:</span>
                        <span class="service-notes-text">{service_notes if service_notes else 'No service notes available'}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            show_machine_details_content(selected_machine)
        else:
            logger.warning("No machine selected for details page")
            st.error("No machine selected. Please go back to the dashboard and select a machine.")

"""
Dashboard Page for Manufacturing Predictive Maintenance.

This page displays machine analytics with system overview cards and charts.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
from datetime import datetime, timedelta
import os
import sys
import time

# Import centralized logging and configuration
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.logger_config import get_logger
from config.front_end_config import frontend_config
logger = get_logger(__name__)

# Add the parent directory to the path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.data_loader import DataLoader
from utils.predictor import MaintenancePredictor
from utils.css_styles import get_dashboard_styles
from services.machines_service import machines_service, ServiceException
from machine_details import show_machine_details_content, show_machine_details_page
from header import create_header

# Initialize data loader and predictor
data_loader = DataLoader()
predictor = MaintenancePredictor()

@st.cache_data(ttl=frontend_config.CACHE_TTL)  # Cache for configured TTL
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

def show_custom_loader(message="Loading Dashboard", submessage="Please wait while we fetch your data"):
    """Show custom loader with blue effect."""
    st.markdown(f"""
    <div class="custom-loader-container">
        <div class="custom-loader"></div>
        <div class="custom-loader-text">{message}</div>
        <div class="custom-loader-subtext">{submessage}</div>
    </div>
    """, unsafe_allow_html=True)

def show_dashboard_page():
    """Show the dashboard page with analytics and system overview."""
    logger.info("Dashboard page started")

    # Load CSS styles
    st.markdown(get_dashboard_styles(), unsafe_allow_html=True)
    
    # Create a placeholder for the loader
    loader_placeholder = st.empty()
    
    # Page-level loading spinner
    with loader_placeholder.container():
        show_custom_loader("Loading Dashboard", "Fetching machine data and analytics...")

    # Get machine data
    logger.info("Loading machine data from service")
    machines_data = get_service_data("get_machines")
        
    if machines_data is None:
        st.error("Failed to load machine data")
        return
    
    machines = machines_data.get("machines", [])
    
    # Clear the loader
    loader_placeholder.empty()
    
    # System Overview Cards
    show_system_overview_cards(machines)
    
    # Machine Analytics Charts
    show_machine_analytics_charts(machines)
    
    # Risk Analysis
    show_risk_analysis(machines)
    
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


def show_system_overview_cards(machines):
    """Show system overview cards with key metrics."""
    
    # Calculate metrics
    total_machines = len(machines)
    high_risk = len([m for m in machines if m["status"] == "High"])
    medium_risk = len([m for m in machines if m["status"] == "Medium"])
    low_risk = len([m for m in machines if m["status"] == "Low"])
    
    # Calculate additional metrics
    avg_temperature = sum(m["temperature"] for m in machines) / len(machines) if machines else 0
    avg_vibration = sum(m["vibration"] for m in machines) / len(machines) if machines else 0
    avg_current = sum(m["current"] for m in machines) / len(machines) if machines else 0
    avg_pressure = sum(m["pressure"] for m in machines) / len(machines) if machines else 0
    
    # Calculate health percentage
    health_percentage = ((low_risk + medium_risk) / total_machines * 100) if total_machines > 0 else 0
    
    # Create professional cards using Streamlit columns and containers
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        with st.container():
            st.markdown("""
            <div class="professional-card total-machines-card">
                <div class="card-content">
                    <div class="card-title">TOTAL MACHINES</div>
                    <div class="card-value">{}</div>
                    <div class="card-subtitle">Active Equipment</div>
                </div>
                <div class="card-icon">
                    <div class="icon-circle blue">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                            <path d="M2 17L12 22L22 17" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                            <path d="M2 12L12 17L22 12" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                        </svg>
                    </div>
                </div>
            </div>
            """.format(total_machines), unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown("""
            <div class="professional-card high-risk-card">
                <div class="card-content">
                    <div class="card-title">HIGH RISK</div>
                    <div class="card-value">{}</div>
                    <div class="card-subtitle">Critical Alert</div>
                </div>
                <div class="card-icon">
                    <div class="icon-circle red">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 9V13" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M12 17H12.01" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            <path d="M10.29 3.86L1.82 18C1.64 18.37 1.64 18.8 1.82 19.17C2 19.54 2.33 19.75 2.69 19.75H21.31C21.67 19.75 22 19.54 22.18 19.17C22.36 18.8 22.36 18.37 22.18 18L13.71 3.86C13.53 3.49 13.2 3.28 12.84 3.28C12.48 3.28 12.15 3.49 11.97 3.86Z" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                        </svg>
                    </div>
                </div>
            </div>
            """.format(high_risk), unsafe_allow_html=True)
    
    with col3:
        with st.container():
            st.markdown("""
            <div class="professional-card medium-risk-card">
                <div class="card-content">
                    <div class="card-title">MEDIUM RISK</div>
                    <div class="card-value">{}</div>
                    <div class="card-subtitle">Maintenance Due</div>
                </div>
                <div class="card-icon">
                    <div class="icon-circle orange">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M13 2L3 14H12L11 22L21 10H12L13 2Z" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                        </svg>
                    </div>
                </div>
            </div>
            """.format(medium_risk), unsafe_allow_html=True)
    
    with col4:
        with st.container():
            st.markdown("""
            <div class="professional-card low-risk-card">
                <div class="card-content">
                    <div class="card-title">LOW RISK</div>
                    <div class="card-value">{}</div>
                    <div class="card-subtitle">Optimal Status</div>
                </div>
                <div class="card-icon">
                    <div class="icon-circle green">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M20 6L9 17L4 12" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </div>
                </div>
            </div>
            """.format(low_risk), unsafe_allow_html=True)
    
    with col5:
        with st.container():
            st.markdown("""
            <div class="professional-card temperature-card">
                <div class="card-content">
                    <div class="card-title">AVG TEMPERATURE</div>
                    <div class="card-value">{:.1f}°C</div>
                    <div class="card-subtitle">Thermal Status</div>
                </div>
                <div class="card-icon">
                    <div class="icon-circle red">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M14 4V10.5C14 11.3 14.3 12.1 14.9 12.6L16 13.5V16C16 17.1 15.1 18 14 18H10C8.9 18 8 17.1 8 16V13.5L9.1 12.6C9.7 12.1 10 11.3 10 10.5V4H14Z" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                            <path d="M10 2H14" stroke="white" stroke-width="2" stroke-linecap="round"/>
                            <path d="M12 18V20" stroke="white" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                    </div>
                </div>
            </div>
            """.format(avg_temperature), unsafe_allow_html=True)
    
    with col6:
        with st.container():
            st.markdown("""
            <div class="professional-card vibration-card">
                <div class="card-content">
                    <div class="card-title">AVG VIBRATION</div>
                    <div class="card-value">{:.1f}</div>
                    <div class="card-subtitle">Stability Index</div>
                </div>
                <div class="card-icon">
                    <div class="icon-circle purple">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M3 12H7L10 3L14 21L17 12H21" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </div>
                </div>
            </div>
            """.format(avg_vibration), unsafe_allow_html=True)
    
    # Second row for remaining sensor metrics - centered layout
    col1, col2, col3, col4 = st.columns([1, 1, 2, 2])
    
    with col1:
        with st.container():
            st.markdown("""
            <div class="professional-card current-card">
                <div class="card-content">
                    <div class="card-title">AVG CURRENT</div>
                    <div class="card-value">{:.1f}A</div>
                    <div class="card-subtitle">Power Consumption</div>
                </div>
                <div class="card-icon">
                    <div class="icon-circle yellow">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 2V6" stroke="white" stroke-width="2" stroke-linecap="round"/>
                            <path d="M12 18V22" stroke="white" stroke-width="2" stroke-linecap="round"/>
                            <path d="M4.93 4.93L7.76 7.76" stroke="white" stroke-width="2" stroke-linecap="round"/>
                            <path d="M16.24 16.24L19.07 19.07" stroke="white" stroke-width="2" stroke-linecap="round"/>
                            <path d="M2 12H6" stroke="white" stroke-width="2" stroke-linecap="round"/>
                            <path d="M18 12H22" stroke="white" stroke-width="2" stroke-linecap="round"/>
                            <path d="M4.93 19.07L7.76 16.24" stroke="white" stroke-width="2" stroke-linecap="round"/>
                            <path d="M16.24 7.76L19.07 4.93" stroke="white" stroke-width="2" stroke-linecap="round"/>
                            <circle cx="12" cy="12" r="3" stroke="white" stroke-width="2"/>
                        </svg>
                    </div>
                </div>
            </div>
            """.format(avg_current), unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown("""
            <div class="professional-card pressure-card">
                <div class="card-content">
                    <div class="card-title">AVG PRESSURE</div>
                    <div class="card-value">{:.1f} bar</div>
                    <div class="card-subtitle">System Pressure</div>
                </div>
                <div class="card-icon">
                    <div class="icon-circle green">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 2C13.1 2 14 2.9 14 4C14 5.1 13.1 6 12 6C10.9 6 10 5.1 10 4C10 2.9 10.9 2 12 2Z" stroke="white" stroke-width="2"/>
                            <path d="M21 9V7L19 5L17 7V9C17 10.1 17.9 11 19 11C20.1 11 21 10.1 21 9Z" stroke="white" stroke-width="2"/>
                            <path d="M3 9V7L5 5L7 7V9C7 10.1 6.1 11 5 11C3.9 11 3 10.1 3 9Z" stroke="white" stroke-width="2"/>
                            <path d="M12 8V18" stroke="white" stroke-width="2" stroke-linecap="round"/>
                            <path d="M8 12H16" stroke="white" stroke-width="2" stroke-linecap="round"/>
                        </svg>
                    </div>
                </div>
            </div>
            """.format(avg_pressure), unsafe_allow_html=True)
    
    # Place risk distribution pie chart spanning 2 columns (col3 and col4)
    with col3:
        # Create risk distribution data
        risk_data = {
            'Risk Level': ['Low Risk', 'Medium Risk', 'High Risk'],
            'Count': [low_risk, medium_risk, high_risk],
            'Color': ['#10b981', '#f97316', '#ef4444']
        }
        
        # Create pie chart
        import plotly.express as px
        fig = px.pie(
            values=risk_data['Count'], 
            names=risk_data['Risk Level'],
            color_discrete_sequence=risk_data['Color'],
            title="Risk Distribution"
        )
        
        fig.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>'
        )
        
        fig.update_layout(
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            height=350,
            margin=dict(t=10, b=10, l=10, r=10)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Place bar chart spanning 2 columns (col4)
    with col4:
        # Create bar chart data
        status_counts = pd.Series([m["status"] for m in machines]).value_counts()
        
        # Create bar chart
        fig = px.bar(
            x=status_counts.index,
            y=status_counts.values,
            color=status_counts.index,
            color_discrete_map={'Low': '#10b981', 'Medium': '#f97316', 'High': '#ef4444'},
            title="Machine Count by Status"
        )
        
        fig.update_layout(
            height=350,
            margin=dict(t=50, b=10, l=10, r=10),
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # # 3rd row for system health summary
    # col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])

    # with col1:
    #     with st.container():
    #         # System Health Summary
    #         st.markdown("""
    #         <div class="health-summary-card">
    #             <div class="health-header">
    #                 <h3>🏥 System Health Overview</h3>
    #                 <div class="health-percentage">{:.1f}%</div>
    #             </div>
    #             <div class="health-bar">
    #                 <div class="health-progress" style="width: {}%"></div>
    #             </div>
    #             <div class="health-status">
    #                 <span class="status-indicator {}">
    #                     {}
    #                 </span>
    #             </div>
    #         </div>
    #         """.format(
    #             health_percentage, 
    #             health_percentage,
    #             'excellent' if health_percentage >= 90 else 'good' if health_percentage >= 70 else 'warning',
    #             'Excellent' if health_percentage >= 90 else 'Good' if health_percentage >= 70 else 'Needs Attention'
    #         ), unsafe_allow_html=True)
    
    # # Leave col2, col3, col4, col5, col6 empty for spacing

def show_machine_analytics_charts(machines):
    """Show machine analytics charts."""
    
    # Get chart configuration
    chart_config = frontend_config.get_chart_config()
    chart_columns = frontend_config.get_layout_config()["chart_columns"]
    # Temperature and Vibration trends
    st.markdown("""
    <div class="sensor-trends-container">
        <div class="section-heading"> Sensor Data Trends</div>
        <div class="sensor-trends-content">
    """, unsafe_allow_html=True)
    
    col_chart3, col_chart4 = st.columns(chart_columns)
    
    with col_chart3:
        # Temperature Distribution Chart
        temperatures = [m["temperature"] for m in machines]
        fig = px.histogram(
            x=temperatures,
            nbins=20,
            title="Temperature Distribution",
            labels={'x': 'Temperature (°C)', 'y': 'Count'},
            color_discrete_sequence=['#ef4444']
        )
        fig.update_traces(
            hovertemplate='<b>Temperature: %{x}°C</b><br>Count: %{y}<extra></extra>'
        )
        fig.update_layout(
            height=chart_config["pie_chart_height"],
            margin=dict(t=40, b=10, l=10, r=10),
            showlegend=False,
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col_chart4:
        # Vibration Distribution Chart
        vibrations = [m["vibration"] for m in machines]
        fig = px.histogram(
            x=vibrations,
            nbins=20,
            title="Vibration Distribution",
            labels={'x': 'Vibration Level', 'y': 'Count'},
            color_discrete_sequence=['#8b5cf6']
        )
        fig.update_traces(
            hovertemplate='<b>Vibration: %{x}</b><br>Count: %{y}<extra></extra>'
        )
        fig.update_layout(
            height=chart_config["pie_chart_height"],
            margin=dict(t=40, b=10, l=10, r=10),
            showlegend=False,
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Close the sensor trends container
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_risk_analysis(machines):
    """Show risk analysis and recommendations."""
    # Calculate risk statistics
    high_risk_machines = [m for m in machines if m["status"] == "High"]
    medium_risk_machines = [m for m in machines if m["status"] == "Medium"]
    low_risk_machines = [m for m in machines if m["status"] == "Low"]
    
    # Create highlighted section wrapper with all content inside
    st.markdown("""
    <div class="risk-analysis-container">
        <div class="section-heading">Risk Analysis</div>
    """, unsafe_allow_html=True)
    st.markdown("""<div class="risk-analysis-content">""", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if high_risk_machines:
            st.markdown("""
            <div class="risk-analysis-section high-risk">
                <div class="risk-header">
                    <h3>
                        <div class="icon-circle red">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 9V13" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M12 17H12.01" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M10.29 3.86L1.82 18C1.64 18.37 1.64 18.8 1.82 19.17C2 19.54 2.33 19.75 2.69 19.75H21.31C21.67 19.75 22 19.54 22.18 19.17C22.36 18.8 22.36 18.37 22.18 18L13.71 3.86C13.53 3.49 13.2 3.28 12.84 3.28C12.48 3.28 12.15 3.49 11.97 3.86Z" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                            </svg>
                        </div>
                        High Risk Machines
                    </h3>
                    <span class="risk-count">{}</span>
                </div>
                <div class="risk-content">
                    <p class="risk-description">Immediate attention required:</p>
                    <div class="machine-list">
                        {}
                    </div>
                </div>
            </div>
            """.format(
                len(high_risk_machines),
                "".join([f'<div class="machine-item">• {machine["machine_id"]} - {machine["temperature"]:.1f}°C, {machine["vibration"]:.1f} vib</div>' for machine in high_risk_machines])
            ), unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="risk-analysis-section low-risk">
                <div class="risk-header">
                    <h3>
                        <div class="icon-circle green">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M20 6L9 17L4 12" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                        No High Risk Machines
                    </h3>
                    <span class="risk-count">0</span>
                </div>
                <div class="risk-content">
                    <p class="risk-description">All machines are operating within safe parameters</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        if medium_risk_machines:
            # Limit the number of machines shown to prevent overflow
            machines_to_show = medium_risk_machines[:5]  # Show max 5 machines
            remaining_count = len(medium_risk_machines) - len(machines_to_show)
            
            machine_list_html = "".join([f'<div class="machine-item">• {machine["machine_id"]} - {machine["temperature"]:.1f}°C, {machine["vibration"]:.1f} vib</div>' for machine in machines_to_show])
            if remaining_count > 0:
                machine_list_html += f'<div class="machine-item">... and {remaining_count} more</div>'
            
            st.markdown("""
            <div class="risk-analysis-section medium-risk">
                <div class="risk-header">
                    <h3>
                        <div class="icon-circle orange">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M13 2L3 14H12L11 22L21 10H12L13 2Z" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                            </svg>
                        </div>
                        Medium Risk Machines
                    </h3>
                    <span class="risk-count">{}</span>
                </div>
                <div class="risk-content">
                    <p class="risk-description">Schedule maintenance soon:</p>
                    <div class="machine-list">
                        {}
                    </div>
                </div>
            </div>
            """.format(
                len(medium_risk_machines),
                machine_list_html
            ), unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="risk-analysis-section low-risk">
                <div class="risk-header">
                    <h3>
                        <div class="icon-circle green">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M20 6L9 17L4 12" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                        No Medium Risk Machines
                    </h3>
                    <span class="risk-count">0</span>
                </div>
                <div class="risk-content">
                    <p class="risk-description">All machines are in good condition</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        if low_risk_machines:
            # Limit the number of machines shown to prevent overflow
            machines_to_show = low_risk_machines[:3]  # Show max 3 machines
            remaining_count = len(low_risk_machines) - len(machines_to_show)
            
            machine_list_html = "".join([f'<div class="machine-item">• {machine["machine_id"]} - {machine["temperature"]:.1f}°C, {machine["vibration"]:.1f} vib</div>' for machine in machines_to_show])
            if remaining_count > 0:
                machine_list_html += f'<div class="machine-item">... and {remaining_count} more</div>'
            
            st.markdown("""
            <div class="risk-analysis-section low-risk">
                <div class="risk-header">
                    <h3>
                        <div class="icon-circle green">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M20 6L9 17L4 12" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                        Low Risk Machines
                    </h3>
                    <span class="risk-count">{}</span>
                </div>
                <div class="risk-content">
                    <p class="risk-description">Operating normally:</p>
                    <div class="machine-list">
                        {}
                    </div>
                </div>
            </div>
            """.format(
                len(low_risk_machines),
                machine_list_html
            ), unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="risk-analysis-section low-risk">
                <div class="risk-header">
                    <h3>
                        <div class="icon-circle green">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M20 6L9 17L4 12" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                        No Low Risk Machines
                    </h3>
                    <span class="risk-count">0</span>
                </div>
                <div class="risk-content">
                    <p class="risk-description">All machines require attention</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Close the highlighted section wrapper
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

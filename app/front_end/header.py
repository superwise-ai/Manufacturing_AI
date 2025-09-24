"""
Header Component for Manufacturing Predictive Maintenance Dashboard

This component creates the main header with SUPERWISE™ logo and title.
"""

import streamlit as st
import base64
import os
import sys

# Import centralized configuration
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.front_end_config import frontend_config
from utils.css_styles import get_common_styles

def create_header():
    """
    Creates the main header component with SUPERWISE™ logo and title.
    
    Returns:
        None: Renders the header directly to the Streamlit app
    """
    try:
        # Load common CSS styles
        st.markdown(get_common_styles(), unsafe_allow_html=True)
        
        # Read and encode image as base64
        logo_path = frontend_config.get_asset_path("superwise_logo")
        with open(logo_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        
        # Enhanced Header with SUPERWISE™ Logo and Navigation
        current_page = st.session_state.get('current_page', 'dashboard')
        # If current_page is 'machine_details', show 'machines' as active
        active_dashboard = current_page == 'dashboard'
        active_machines = current_page == 'machines' or current_page == 'machine_details'
        st.markdown(f"""
        <div class="header-container">
            <div class="header-left">
                <img src="data:image/svg+xml;base64,{encoded}" alt="SUPERWISE Logo">
                <span class="header-title">Manufacturing AI</span>
            </div>
            <div class="header-right">
                <div class="header-navigation">
                    <a href="?page=dashboard" target="_self" class="nav-link {'active' if active_dashboard else ''}">
                        Dashboard
                    </a>
                    <a href="?page=machines" target="_self" class="nav-link {'active' if active_machines else ''}">
                        Machines
                    </a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Handle page navigation from URL parameters
        if 'page' in st.query_params:
            page = st.query_params['page']
            if page in ['dashboard', 'machines', 'machine_details'] and st.session_state.get('current_page') != page:
                st.session_state.current_page = page
                # Handle machine details page with machine_id parameter
                if page == 'machine_details' and 'machine_id' in st.query_params:
                    st.session_state.selected_machine = st.query_params['machine_id']
                st.rerun()
        
    except Exception as e:
        # Fallback header without logo
        current_page = st.session_state.get('current_page', 'dashboard')
        # If current_page is 'machine_details', show 'machines' as active
        active_dashboard = current_page == 'dashboard'
        active_machines = current_page == 'machines' or current_page == 'machine_details'
        
        st.markdown(f"""
        <div class="header-container">
            <div class="header-left">
                <span class="header-title">Manufacturing AI</span>
            </div>
            <div class="header-right">
                <div class="header-navigation">
                    <a href="?page=dashboard" target="_self" class="nav-link {'active' if active_dashboard else ''}">
                        Dashboard
                    </a>
                    <a href="?page=machines" target="_self" class="nav-link {'active' if active_machines else ''}">
                        Machines
                    </a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Handle page navigation from URL parameters
        if 'page' in st.query_params:
            page = st.query_params['page']
            if page in ['dashboard', 'machines', 'machine_details'] and st.session_state.get('current_page') != page:
                st.session_state.current_page = page
                # Handle machine details page with machine_id parameter
                if page == 'machine_details' and 'machine_id' in st.query_params:
                    st.session_state.selected_machine = st.query_params['machine_id']
                st.rerun()

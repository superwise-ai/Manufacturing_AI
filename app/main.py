"""
Main Application for Manufacturing Predictive Maintenance Dashboard

This is the main entry point that handles navigation between different pages.
"""

import streamlit as st
import sys
import os

# Add the front_end directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'front_end'))

from front_end.dashboard import show_dashboard_page
from front_end.machines import show_machines_page
from front_end.machine_details import show_machine_details_page
from front_end.header import create_header
from config.front_end_config import frontend_config
from utils.css_styles import get_dashboard_styles
from utils.logger_config import get_logger

# Initialize logger
logger = get_logger(__name__)

# Page configuration
st.set_page_config(
    page_title=frontend_config.PAGE_TITLE,
    page_icon=frontend_config.get_asset_path("favicon"),
    layout=frontend_config.LAYOUT,
    initial_sidebar_state="collapsed"  # Hide sidebar since navigation is in header
)

def main():
    """Main application function that handles page navigation."""
    logger.info("=== Manufacturing AI Dashboard Application Started ===")
    
    try:
        # Application-level loading spinner
        with st.spinner("🚀 Initializing Manufacturing AI Dashboard..."):
            logger.debug("Loading CSS styles")
            # Load CSS styles
            st.markdown(get_dashboard_styles(), unsafe_allow_html=True)
            logger.debug("CSS styles loaded successfully")
            
            # Initialize session state for page navigation
            if 'current_page' not in st.session_state:
                st.session_state.current_page = "dashboard"
                logger.debug("Initialized session state with default page: dashboard")
            else:
                logger.debug(f"Current page from session state: {st.session_state.current_page}")
            
            # Initialize selected_machine if not set
            if 'selected_machine' not in st.session_state:
                st.session_state.selected_machine = None
                logger.debug("Initialized selected_machine to None")
            else:
                logger.debug(f"Selected machine from session state: {st.session_state.selected_machine}")

            # Create header with navigation in main content area
            logger.debug("Creating header component with navigation")
            create_header()
            logger.debug("Header component with navigation created successfully")
            
            # Get current page from session state
            current_page = st.session_state.current_page
        
        # Route to appropriate page based on current_page
        logger.info(f"Routing to page: {st.session_state.current_page}")
        if st.session_state.current_page == "dashboard":
            logger.debug("Loading dashboard page")
            show_dashboard_page()
        elif st.session_state.current_page == "machines":
            logger.debug("Loading machines page")
            show_machines_page()
        elif st.session_state.current_page == "machine_details":
            logger.debug("Loading machine details page")
            show_machine_details_page()
        else:
            # Default to dashboard
            logger.warning(f"Unknown page '{st.session_state.current_page}', defaulting to dashboard")
            st.session_state.current_page = "dashboard"
            show_dashboard_page()
        
        logger.debug("Page rendering completed successfully")
        
    except Exception as e:
        logger.error(f"Error in main application: {str(e)}", exc_info=True)
        st.error(f"Application error: {str(e)}")
        raise

if __name__ == "__main__":
    main()

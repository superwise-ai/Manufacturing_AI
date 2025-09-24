"""
Common CSS Styles for Manufacturing AI Portal

This module contains all the common CSS styles used across components
to avoid code duplication and maintain consistency.
"""

def get_common_styles():
    """
    Returns the common CSS styles used across all components.
    
    Returns:
        str: CSS styles as a string
    """
    return f"""
    <style>
    /* ===== GLOBAL FONT IMPORTS ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    /* ===== GLOBAL BACKGROUND COLOR ===== */
    .stApp {{
        background-color: #f5f6f8;
        background-image: none;
    }}
    
    /* ===== GLOBAL FONT FAMILY ===== */
    * {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif !important;
    }}
    
    /* ===== STREAMLIT SPECIFIC FONT OVERRIDES ===== */
    .stApp, .stApp > div, .main .block-container, .stSidebar, .stSidebar > div {{
        font-family: 'Inter', sans-serif !important;
    }}
    
    /* Override Streamlit default fonts */
    .stText, .stMarkdown, .stSelectbox, .stTextInput, .stTextArea, .stNumberInput, 
    .stSlider, .stCheckbox, .stRadio, .stButton, .stFileUploader, .stDateInput, 
    .stTimeInput, .stColorPicker, .stMultiselect, .stSelectbox, .stExpander,
    .stTabs, .stContainer, .stColumns, .stColumn, .stMetric, .stAlert,
    .stSuccess, .stError, .stWarning, .stInfo, .stException, .stToast {{
        font-family: 'Inter', sans-serif !important;
    }}
    
    /* Override specific Streamlit elements */
    h1, h2, h3, h4, h5, h6, p, span, div, label, input, textarea, select, button {{
        font-family: 'Inter', sans-serif !important;
    }}
    
    /* ===== COMMON CARD STYLES ===== */
    .common-card {{
        background: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }}
    
    .common-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    
    /* ===== PROFESSIONAL CARDS ===== */
    .professional-card {{
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        border: 2px solid rgba(255, 255, 255, 0.9);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        height: 140px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}
    
    
    .professional-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
        border-color: rgba(59, 130, 246, 0.5);
        background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
    }}
    
    .professional-card .card-icon {{
        font-size: 2.5rem;
        padding: 0.75rem;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        min-width: 4rem;
        height: 4rem;
        margin-bottom: 1rem;
    }}
    
    .professional-card .card-icon svg {{
        width: 2.5rem;
        height: 2.5rem;
        color: inherit;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
    }}
    
    /* ===== ICON CIRCLES ===== */
    .icon-circle {{
        width: 4rem;
        height: 4rem;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }}
    
    .icon-circle.blue {{
        background: linear-gradient(135deg, #3b82f6, #1d4ed8);
    }}
    
    .icon-circle.red {{
        background: linear-gradient(135deg, #ef4444, #dc2626);
    }}
    
    .icon-circle.orange {{
        background: linear-gradient(135deg, #f97316, #ea580c);
    }}
    
    .icon-circle.green {{
        background: linear-gradient(135deg, #10b981, #059669);
    }}
    
    .icon-circle.purple {{
        background: linear-gradient(135deg, #8b5cf6, #7c3aed);
    }}
    
    .icon-circle.yellow {{
        background: linear-gradient(135deg, #eab308, #ca8a04);
    }}
    
    
    .professional-card .card-content {{
        text-align: left;
        flex: 1;
    }}
    
    .professional-card .card-icon {{
        margin-bottom: 0;
        margin-left: 1rem;
    }}
    
    .professional-card .card-title {{
        font-size: 0.875rem;
        font-weight: 700;
        color: #374151;
        margin: 0 0 0.5rem 0;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
    }}
    
    .professional-card .card-value {{
        font-size: 1.8rem;
        font-weight: 900;
        color: #111827;
        margin: 0 0 0.25rem 0;
        line-height: 1;
        text-shadow: 0 2px 4px rgba(255, 255, 255, 0.8);
    }}
    
    .professional-card .card-subtitle {{
        font-size: 0.75rem;
        color: #6b7280;
        margin: 0;
        font-weight: 600;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
    }}
    
    
    /* System Health Summary */
    .health-summary-card {{
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        border-radius: 16px;
        padding: 2rem;
        color: white;
        margin-top: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }}
    
    .health-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }}
    
    .health-header h3 {{
        margin: 0;
        font-size: 1.25rem;
        font-weight: 600;
    }}
    
    .health-percentage {{
        font-size: 2rem;
        font-weight: 800;
        color: #60a5fa;
    }}
    
    .health-bar {{
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        height: 8px;
        margin-bottom: 1rem;
        overflow: hidden;
    }}
    
    .health-progress {{
        background: linear-gradient(90deg, #10b981, #34d399);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }}
    
    .health-status {{
        text-align: center;
    }}
    
    .status-indicator {{
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}
    
    .status-indicator.excellent {{
        background: rgba(16, 185, 129, 0.2);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }}
    
    .status-indicator.good {{
        background: rgba(59, 130, 246, 0.2);
        color: #60a5fa;
        border: 1px solid rgba(59, 130, 246, 0.3);
    }}
    
    .status-indicator.warning {{
        background: rgba(217, 119, 6, 0.2);
        color: #fbbf24;
        border: 1px solid rgba(217, 119, 6, 0.3);
    }}
    
    /* ===== PAGE TITLE AND HEADINGS ===== */
    .main-title {{
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        color: #1e293b !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 0 2px 4px rgba(255, 255, 255, 0.9) !important;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(248, 250, 252, 0.8)) !important;
        padding: 1rem 1.5rem !important;
        border-radius: 12px !important;
        border: 2px solid rgba(255, 255, 255, 0.8) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
    }}
    
    
    /* ===== SECTION STYLES ===== */
    .section-container {{
        background: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }}
    
    .section-header {{
        display: flex;
        justify-content: flex-start;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 1.5rem;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid #e5e7eb;
    }}
    
    .section-title {{
        font-size: 1.25rem;
        font-weight: 600;
        color: #1e293b;
        margin: 0;
    }}
    
    .section-icon {{
        font-size: 1.25rem;
        color: #6b7280;
    }}
    
    /* ===== STATUS BADGE STYLES ===== */
    .status-badge {{
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.75rem;
        font-weight: 500;
        text-transform: uppercase;
    }}
    
    .status-active {{
        background-color: #d1fae5;
        color: #047857;
    }}
    
    .status-followup {{
        background-color: #fef3c7;
        color: #d97706;
    }}
    
    .status-violation {{
        background-color: #fef2f2;
        color: #dc2626;
    }}
    
    .status-clear {{
        background-color: #d1fae5;
        color: #047857;
    }}
    
    /* ===== HEADER STYLES ===== */
    .header-container {{
        background: white;
        padding: 1rem 1rem 1rem 1rem;
        border-radius: 0;
        margin: 0;
        margin-bottom: 2rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border-bottom: 1px solid #e5e7eb;
        position: relative;
        top: 0;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}
     
    .header-content {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
    }}
     
    .header-left {{
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    .header-left img {{
        height: 37px;
        width: 160px;
        filter: none;
    }}

    .header-title {{
        font-size: 1.5rem;
        font-weight: 700;
        color: #2c2f38;
        font-family: 'Inter', sans-serif;
    }}
    
    .header-right {{
        display: flex;
        align-items: center;
    }}
    
    .header-navigation {{
        display: flex;
        gap: 0.5rem;
    }}
    
    .nav-link {{
        background: transparent !important;
        border: none !important;
        color: black !important;
        padding: 0.75rem 1.5rem !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        font-family: 'Inter', sans-serif !important;
        text-decoration: none !important;
        display: inline-block !important;
    }}
    
    .nav-link:hover {{
        background: red !important;
        color: white !important;
        text-decoration: none !important;
    }}
    
    .nav-link.active {{
        background: transparent !important;
        border: none !important;
        color: #ff0000 !important;
        text-decoration: none !important;
    }}
    
    .nav-link.active:hover {{
        background: red !important;
        color: white !important;
        text-decoration: none !important;
    }}
    
    .title {{
        color: black;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 0;
        font-family: 'Inter', sans-serif;
    }}
    
    .logout-button {{
        background-color: #ef4444;
        color: white !important;
        border: none;
        padding: 0.4rem 1rem;
        border-radius: 0.375rem;
        font-size: 0.9rem;
        font-weight: 600;
        cursor: pointer;
        transition: background-color 0.2s ease;
        margin-left: auto;
    }}
    
    .logout-button:hover {{
        background-color: #dc2626;
    }}
    
    /* ===== BUTTON STYLES ===== */
    .btn-primary {{
        background-color: #3b82f6;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 0.375rem;
        font-size: 0.875rem;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.2s ease;
    }}
    
    .btn-primary:hover {{
        background-color: #2563eb;
    }}
    
    .btn-secondary {{
        background-color: #6b7280;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 0.375rem;
        font-size: 0.875rem;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.2s ease;
    }}
    
    .btn-secondary:hover {{
        background-color: #4b5563;
    }}
    
    .btn-danger {{
        background-color: #ef4444;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 0.375rem;
        font-size: 0.875rem;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.2s ease;
    }}
    
    .btn-danger:hover {{
        background-color: #dc2626;
    }}
    
    /* ===== FORM STYLES ===== */
    .form-container {{
        background: white;
        padding: 2rem;
        border-radius: 0.75rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        max-width: 400px;
        width: 100%;
    }}
    
    .form-title {{
        font-size: 1.5rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1.5rem;
        text-align: center;
    }}
    
    .form-group {{
        margin-bottom: 1.5rem;
    }}
    
    .form-label {{
        display: block;
        font-size: 0.875rem;
        font-weight: 500;
        color: #374151;
        margin-bottom: 0.5rem;
    }}
    
    .form-input {{
        width: 100%;
        padding: 0.75rem;
        border: 1px solid #d1d5db;
        border-radius: 0.375rem;
        font-size: 1rem;
        transition: border-color 0.2s ease;
    }}
    
    .form-input:focus {{
        outline: none;
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    }}
    
    /* ===== RISK ANALYSIS CONTAINER ===== */
    .risk-analysis-container {{
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.95) 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
        border: 3px solid rgba(59, 130, 246, 0.2);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }}
    
    .risk-analysis-container::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #ef4444, #f97316, #10b981);
        z-index: 1;
    }}
    
    .risk-analysis-container .section-heading {{
        font-size: 1.5rem !important;
        font-weight: 800 !important;
        color: #1e293b !important;
        margin-bottom: 2rem !important;
        text-align: center !important;
        background: none !important;
        padding: 0 !important;
        border: none !important;
        box-shadow: none !important;
        
    }}
    
    .risk-analysis-container .section-heading .icon-circle {{
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 3rem !important;
        height: 3rem !important;
        margin: 1rem !important;
    }}
    
    .risk-analysis-content {{
        position: relative;
        z-index: 2;
    }}

    div[data-testid="stColumns"] {{
        gap: 1.5rem !important;
    }}
    
    /* ===== SENSOR TRENDS CONTAINER ===== */
    .sensor-trends-container {{
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(248,250,252,0.95) 100%);
        border: 2px solid rgba(59, 130, 246, 0.2);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }}
    
    .sensor-trends-container::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        z-index: 1;
    }}
    
    .sensor-trends-container .section-heading {{
        font-size: 1.5rem !important;
        font-weight: 800 !important;
        color: #1e293b !important;
        margin-bottom: 2rem !important;
        text-align: center !important;
        background: none !important;
        padding: 0 !important;
        border: none !important;
        box-shadow: none !important;
    }}
    
    .sensor-trends-content {{
        position: relative;
        z-index: 2;
    }}
    
    /* ===== RISK ANALYSIS SECTIONS ===== */
    .risk-analysis-section {{
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        border: 2px solid rgba(255, 255, 255, 0.9);
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        min-height: 300px;
        max-height: 400px;
        display: flex;
        flex-direction: column;
    }}
    
    .risk-analysis-section:hover {{
        transform: translateY(-2px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
    }}
    
    .risk-analysis-section.high-risk {{
        border-left: 4px solid #ef4444;
        background: linear-gradient(135deg, #fef2f2 0%, #ffffff 100%);
    }}
    
    .risk-analysis-section.medium-risk {{
        border-left: 4px solid #f97316;
        background: linear-gradient(135deg, #fff7ed 0%, #ffffff 100%);
    }}
    
    .risk-analysis-section.low-risk {{
        border-left: 4px solid #10b981;
        background: linear-gradient(135deg, #f0fdf4 0%, #ffffff 100%);
    }}
    
    .risk-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    }}
    
    .risk-header h3 {{
        margin: 0;
        font-size: 1.125rem;
        font-weight: 700;
        color: #1e293b;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}
    
    .risk-header h3 .icon-circle {{
        width: 2rem;
        height: 2rem;
        margin: 0;
    }}
    
    .risk-count {{
        background: linear-gradient(135deg, #3b82f6, #1d4ed8);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 700;
        min-width: 2rem;
        text-align: center;
    }}
    
    .risk-content {{
        color: #374151;
        flex: 1;
        display: flex;
        flex-direction: column;
    }}
    
    .risk-description {{
        font-size: 0.875rem;
        color: #6b7280;
        margin-bottom: 0.75rem;
        font-weight: 500;
    }}
    
    .machine-list {{
        flex: 1;
        overflow-y: auto;
        min-height: 0;
        max-height: 120px;
        padding-right: 0.5rem;
    }}
    
    .machine-item {{
        font-size: 0.875rem;
        color: #374151;
        margin-bottom: 0.5rem;
        padding: 0.25rem 0;
        border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    }}
    
    .machine-item:last-child {{
        border-bottom: none;
        margin-bottom: 0;
    }}
    
     .machine-item:hover {{
         background: rgba(59, 130, 246, 0.05);
         border-radius: 4px;
         padding: 0.25rem 0.5rem;
         margin: 0.25rem -0.5rem;
     }}
     
     /* ===== CUSTOM LOADER STYLES ===== */
     .custom-loader-container {{
         position: fixed;
         top: 0;
         left: 0;
         width: 100%;
         height: 100%;
         background: rgba(245, 246, 248, 0.95);
         backdrop-filter: blur(10px);
         -webkit-backdrop-filter: blur(10px);
         display: flex;
         flex-direction: column;
         justify-content: center;
         align-items: center;
         z-index: 9999;
         transition: opacity 0.5s ease, visibility 0.5s ease;
     }}
     
     .custom-loader-container.hidden {{
         opacity: 0;
         visibility: hidden;
     }}
     
     .custom-loader {{
         width: 80px;
         height: 80px;
         border: 4px solid rgba(59, 130, 246, 0.2);
         border-top: 4px solid #3b82f6;
         border-radius: 50%;
         animation: spin 1s linear infinite;
         margin-bottom: 2rem;
         box-shadow: 0 8px 32px rgba(59, 130, 246, 0.3);
     }}
     
     .custom-loader-text {{
         font-size: 1.25rem;
         font-weight: 600;
         color: #1e293b;
         text-align: center;
         margin-bottom: 0.5rem;
         font-family: 'Inter', sans-serif;
     }}
     
     .custom-loader-subtext {{
         font-size: 0.875rem;
         color: #6b7280;
         text-align: center;
         font-family: 'Inter', sans-serif;
     }}
     
     @keyframes spin {{
         0% {{ transform: rotate(0deg); }}
         100% {{ transform: rotate(360deg); }}
     }}
     
     .loader-dots {{
         display: inline-block;
         animation: dots 1.5s infinite;
     }}
     
     @keyframes dots {{
         0%, 20% {{ content: ''; }}
         40% {{ content: '.'; }}
         60% {{ content: '..'; }}
         80%, 100% {{ content: '...'; }}
     }}
     
     /* ===== MACHINES TABLE STYLES ===== */
     .machines-table-container {{
         background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.95) 100%);
         border: 2px solid rgba(59, 130, 246, 0.2);
         border-radius: 16px;
         padding: 1.5rem;
         margin: 2rem 0;
         box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
         backdrop-filter: blur(10px);
         -webkit-backdrop-filter: blur(10px);
         position: relative;
         overflow: hidden;
     }}
     
     .machines-table-container .stButton > button {{
         background: linear-gradient(135deg, #ef4444, #dc2626) !important;
         color: white !important;
         border: none !important;
         padding: 0.5rem 1rem !important;
         border-radius: 8px !important;
         font-size: 0.75rem !important;
         font-weight: 600 !important;
         font-family: 'Inter', sans-serif !important;
         text-transform: uppercase !important;
         letter-spacing: 0.05em !important;
         transition: all 0.3s ease !important;
     }}
     
    .machines-table-container .stButton > button:hover {{
        background: linear-gradient(135deg, #dc2626, #b91c1c) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3) !important;
    }}
    
    /* Ensure Streamlit columns align with table header */
    .machines-table-container .stColumns {{
        display: grid !important;
        grid-template-columns: 1.5fr 1fr 1.2fr 1fr 1fr 1fr 1fr 1.2fr !important;
        gap: 1rem !important;
        align-items: center !important;
        margin-bottom: 0.5rem !important;
    }}
    
    .machines-table-container .stColumns > div {{
        padding: 0 !important;
        margin: 0 !important;
    }}
     
     .machines-table-container::before {{
         content: '';
         position: absolute;
         top: 0;
         left: 0;
         right: 0;
         height: 4px;
         background: linear-gradient(90deg, #3b82f6, #8b5cf6);
         z-index: 1;
     }}
     
     .machines-table-container .section-heading {{
         font-size: 1.5rem !important;
         font-weight: 800 !important;
         color: #1e293b !important;
         margin-bottom: 1.5rem !important;
         text-align: center !important;
         background: none !important;
         padding: 0 !important;
         border: none !important;
         box-shadow: none !important;
     }}
     
     .machines-table-header {{
         background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
         border-radius: 12px;
         padding: 1rem;
         margin-bottom: 1rem;
         box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
     }}
     
     .table-header-row {{
         display: grid;
         grid-template-columns: 1.5fr 1fr 1.2fr 1fr 1fr 1fr 1fr 1.2fr;
         gap: 1rem;
         align-items: center;
         border: 1px solid rgba(0, 0, 0, 0.1);
         border-radius: 8px;
     }}
     
     .table-header-cell {{
         font-size: 0.875rem;
         font-weight: 700;
         color: #374151;
         text-transform: uppercase;
         letter-spacing: 0.05em;
         text-align: center;
         padding: 0.75rem 0.5rem;
         border-right: 1px solid rgba(0, 0, 0, 0.1);
     }}
     
     .table-header-cell:last-child {{
         border-right: none;
     }}
     
    .machines-table-row {{
        display: grid;
        grid-template-columns: 1.5fr 1fr 1.2fr 1fr 1fr 1fr 1fr 1.2fr;
        gap: 1rem;
        align-items: center;
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        border: 1px solid rgba(0, 0, 0, 0.1);
        border-top: 1px solid rgba(0, 0, 0, 0.1);
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        border-left: 1px solid rgba(0, 0, 0, 0.1);
        border-right: 1px solid rgba(0, 0, 0, 0.1);
    }}
     
     .machines-table-row.even {{
         background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
     }}
     
     .machines-table-row.odd {{
         background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
     }}
     
     .machines-table-row:hover {{
         transform: translateY(-2px);
         box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
         border-color: rgba(59, 130, 246, 0.3);
     }}
     
    .table-cell {{
        text-align: center;
        padding: 0.5rem;
        border-right: 1px solid rgba(0, 0, 0, 0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 2.5rem;
        width: 100%;
        box-sizing: border-box;
    }}
    
    .table-cell:last-child {{
        border-right: none;
    }}
     
     .machine-id-text {{
         font-size: 0.875rem;
         font-weight: 700;
         font-family: 'Inter', sans-serif;
     }}
     
     .status-badge {{
         display: inline-flex;
         align-items: center;
         gap: 0.25rem;
         padding: 0.25rem 0.75rem;
         border-radius: 20px;
         font-size: 0.75rem;
         font-weight: 600;
         text-transform: uppercase;
         letter-spacing: 0.05em;
     }}
     
     .status-badge.status-high {{
         background: rgba(239, 68, 68, 0.1);
         border: 1px solid rgba(239, 68, 68, 0.3);
     }}
     
     .status-badge.status-medium {{
         background: rgba(249, 115, 22, 0.1);
         border: 1px solid rgba(249, 115, 22, 0.3);
     }}
     
     .status-badge.status-low {{
         background: rgba(16, 185, 129, 0.1);
         border: 1px solid rgba(16, 185, 129, 0.3);
     }}
     
     .reading-text {{
         font-size: 0.875rem;
         color: #6b7280;
         font-family: 'Inter', sans-serif;
     }}
     
     .metric-value {{
         font-size: 0.875rem;
         font-weight: 600;
         color: #374151;
         font-family: 'Inter', sans-serif;
     }}
     
     .temperature-value {{
         color: #ef4444;
     }}
     
     .vibration-value {{
         color: #8b5cf6;
     }}
     
     .current-value {{
         color: #eab308;
     }}
     
     .pressure-value {{
         color: #10b981;
     }}
     
    .view-details-link {{
        background: linear-gradient(135deg, #ef4444, #dc2626);
        color: white !important;
        text-decoration: none !important;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        font-family: 'Inter', sans-serif;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        width: 100%;
        max-width: 120px;
        display: inline-block;
        text-align: center;
    }}
    
    .view-details-link:hover {{
        background: linear-gradient(135deg, #dc2626, #b91c1c);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
        color: white !important;
        text-decoration: none !important;
    }}
    
    .view-details-link:visited {{
        color: white !important;
        text-decoration: none !important;
    }}
    
    .view-details-link:active {{
        color: white !important;
        text-decoration: none !important;
    }}
    
    /* Machine Details Title Card */
    .machine-details-title-card {{
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(0, 0, 0, 0.1);
        position: relative;
        overflow: hidden;
    }}
    
    .machine-details-title-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    }}
    
    .machine-details-title-card .section-heading {{
        color: #1e293b;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0 0 1rem 0;
        text-align: center;
        font-family: 'Inter', sans-serif;
    }}
    
    .machine-info-section {{
        padding: 0.5rem 0;
    }}
    
    .machine-name-info {{
        color: #1e293b;
        font-size: 1.125rem;
        font-weight: 600;
        margin: 0 0 0.75rem 0;
        text-align: center;
        font-family: 'Inter', sans-serif;
    }}
    
    .service-notes-info {{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }}
    
    .service-notes-label {{
        color: #1e293b;
        font-size: 0.875rem;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
    }}
    
    .service-notes-text {{
        color: #64748b;
        font-size: 0.875rem;
        line-height: 1.5;
        font-family: 'Inter', sans-serif;
    }}
    
    /* Combined Machine Details Card */
    .machine-details-card {{
        background: white;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(0, 0, 0, 0.1);
        position: relative;
        overflow: hidden;
        max-width: 600px;
    }}
    
    .machine-details-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    }}
    
    .machine-details-header {{
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 0.75rem;
        margin-bottom: 1rem;
    }}
    
    .machine-details-header h3 {{
        color: #1e293b;
        font-size: 1.25rem;
        font-weight: 700;
        margin: 0;
        text-align: left;
        font-family: 'Inter', sans-serif;
    }}
    
    .machine-details-content {{
        padding: 0;
    }}
    
    .service-notes-section {{
        background: transparent;
        border-radius: 0;
        padding: 0;
        border-left: none;
    }}
    
    .service-notes-section h4 {{
        color: #1e293b;
        font-size: 1rem;
        font-weight: 600;
        margin: 0 0 0.25rem 0;
        font-family: 'Inter', sans-serif;
    }}
    
    .service-notes-section p {{
        color: #64748b;
        font-size: 0.875rem;
        line-height: 1.5;
        margin: 0;
        font-family: 'Inter', sans-serif;
    }}
     
     /* Responsive design for smaller screens */
     @media (max-width: 1200px) {{
         .table-header-row,
         .machines-table-row {{
             grid-template-columns: 1.2fr 0.8fr 1fr 0.8fr 0.8fr 0.8fr 0.8fr 1fr;
             gap: 0.5rem;
         }}
         
         .table-header-cell,
         .table-cell {{
             font-size: 0.75rem;
             padding: 0.25rem;
         }}
     }}
     </style>
     """

def get_dashboard_styles():
    """
    Returns dashboard-specific CSS styles for the Manufacturing Predictive Maintenance application.
    
    Returns:
        str: Dashboard CSS styles as a string
    """
    return """
    <style>
    /* ===== INTER FONT FOR DASHBOARD ===== */
    .main-header, .header-subtitle, .stat-number, .stat-label, .company-logo, 
    .last-updated, .footer, .footer-links, .footer-links a {
        font-family: 'Inter', sans-serif !important;
    }
    
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .header-subtitle {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
        font-style: italic;
    }
    .header-stats {
        display: flex;
        justify-content: space-around;
        margin-top: 1rem;
        flex-wrap: wrap;
    }
    .stat-item {
        text-align: center;
        color: #333;
        margin: 0.5rem;
    }
    .stat-number {
        font-size: 1.5rem;
        font-weight: bold;
        display: block;
        color: #1f77b4;
    }
    .stat-label {
        font-size: 0.9rem;
        color: #666;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .alert-high {
        background-color: #ffebee;
        border-left: 4px solid #f44336;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .alert-medium {
        background-color: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .alert-low {
        background-color: #e8f5e8;
        border-left: 4px solid #4caf50;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .company-logo {
        font-size: 1.5rem;
        margin-right: 10px;
    }
    .last-updated {
        font-size: 0.8rem;
        color: rgba(255, 255, 255, 0.7);
        text-align: center;
        margin-top: 0.5rem;
    }
    .footer {
        background-color: #f8f9fa;
        padding: 1rem;
        border-top: 1px solid #dee2e6;
        margin-top: 2rem;
        text-align: center;
        color: #6c757d;
        font-size: 0.9rem;
    }
    .footer-links {
        margin: 0.5rem 0;
    }
    .footer-links a {
        color: #1f77b4;
        text-decoration: none;
        margin: 0 1rem;
    }
    .footer-links a:hover {
        text-decoration: underline;
    }
    </style>
    """


def get_component_specific_styles(component_name):
    """
    Returns component-specific CSS styles.
    
    Args:
        component_name (str): Name of the component
        
    Returns:
        str: Component-specific CSS styles
    """
    styles = {
        'landing_page': """
        <style>
        .landing-header {
            background: white;
            padding: 1rem 1rem 1rem 1rem;
            border-radius: 0;
            margin: 0;
            margin-bottom: 2rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border-bottom: 1px solid #e5e7eb;
            position: relative;
            top: 0;
        }
        
        .landing-header-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }
        
        .landing-header-left {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .landing-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 60vh;
            text-align: center;
            padding: 2rem;
        }
        
        .welcome-title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #1e293b;
            margin-bottom: 1rem;
        }
        
        .welcome-subtitle {
            font-size: 1.25rem;
            color: #64748b;
            margin-bottom: 2rem;
            max-width: 600px;
        }
        </style>
        """,
        
        'login_page': """
        <style>
        .login-header {
            background: white;
            padding: 1rem 1rem 1rem 1rem;
            border-radius: 0;
            margin: 0;
            margin-bottom: 2rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border-bottom: 1px solid #e5e7eb;
            position: relative;
            top: 0;
        }
        
        .login-header-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }
        
        .login-header-left {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .login-container {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 60vh;
            padding: 2rem;
        }
        
        .login-form-subtitle {
            font-size: 1rem;
            color: #64748b;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        .forgot-password {
            text-align: center;
            margin-top: 1rem;
        }
        
        .forgot-password a {
            color: #3b82f6;
            text-decoration: none;
            font-size: 0.875rem;
        }
        
        .forgot-password a:hover {
            text-decoration: underline;
        }
        </style>
        """,
        
        'sidebar': """
        <style>
        .sidebar .sidebar-content {
            background-color: #f8fafc;
            padding: 0rem 1rem 1rem 1rem;
        }
        
        .stSidebar button[data-testid="baseButton-secondary"] {
            background-color: transparent !important;
            border: none !important;
            padding: 0.75rem 1rem !important;
            margin: 0.25rem 0 !important;
            border-radius: 0.5rem !important;
            transition: all 0.2s ease !important;
            width: 100% !important;
            font-size: 1rem !important;
        }
        
        .stSidebar button[data-testid="baseButton-secondary"]:hover {
            background-color: #e2e8f0 !important;
            transform: translateX(4px) !important;
        }
        </style>
        """
    }
    
    return styles.get(component_name, "")
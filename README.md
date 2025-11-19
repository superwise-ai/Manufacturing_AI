<div align="left">



<a href="https://superwise.ai/" target="_blank">
<img src="https://superwise.ai/wp-content/uploads/2024/05/Superwise-logo.svg" alt="SUPERWISE® Logo" width="350"/></a>

**Powered by SUPERWISE® — Leading Agentic Governance & Operations Solutions**

[![Powered by SUPERWISE®](https://img.shields.io/badge/Powered%20by-SUPERWISE®-0052CC?style=for-the-badge&logo=superuser)](https://superwise.ai)
[![AI Manufacturing](https://img.shields.io/badge/AI%20Manufacturing-Management-00A86B?style=for-the-badge&logo=manufacturing)](https://superwise.ai)
[![Enterprise Ready](https://img.shields.io/badge/Enterprise-Ready-gold?style=for-the-badge&logo=enterprise)](https://superwise.ai)

</div>

# 🤖 Manufacturing AI

**Manufacturing AI** is an intelligent predictive maintenance platform that leverages artificial intelligence to optimize manufacturing operations, prevent equipment failures, and reduce maintenance costs through real-time monitoring and predictive analytics.

The system uses synthetic machine sensor data — including timestamp, machine ID, vibration, temperature, current, pressure, and operating hours — along with sensor risk guides and maintenance records to simulate real-world industrial environments.

The project uses simulated datasets containing **timestamp, machine ID, vibration, temperature, current, pressure, and operating hours**, along with **sensor risk guides** and **maintenance records**.  
This data is stored as **Knowledge in Superwise AI**, where a configured **Superwise agent** performs continuous analysis and prediction based on three core tasks:

1. **Data Analysis**
   - Reviews maintenance history to identify overdue services or recurring issues.  
   - Detects anomalies in sensor trends, such as:  
     - Increasing vibration → possible motor or bearing wear.  
     - Rising temperature → potential overheating.  
     - Higher current draw → motor or load issues.  
     - Abnormal pressure → hydraulic or pneumatic faults.  

2. **Failure Risk Assessment**
   - Classifies each machine’s health as:  
     - **Low** — Normal condition, no issues detected.  
     - **Medium** — Early warnings, maintenance required soon.  
     - **High** — Critical anomalies, failure imminent.  

3. **Remaining Useful Life (RUL) Prediction**
   - Estimates **predicted days to failure** based on trends and severity.  
   - Recommends **next maintenance date** to avoid unplanned downtime.  

By combining historical maintenance records with sensor data, **Manufacturing_AI** helps companies move from **reactive repairs** to **predictive maintenance**, minimizing downtime and maintenance costs.

### **Key Benefits**
- Detects early machine failure signs through AI-based analysis.  
- Helps maintenance teams prioritize critical equipment.  
- Reduces unplanned downtime and maintenance expenses.  
- Demonstrates industrial AI capabilities using synthetic datasets.  

## 🏢 **Ready for Business?**

**Transform your business operations with Superwise AI**: [Get Started with Superwise](https://docs.superwise.ai/docs/introduction-to-superwise) - Enterprise-grade AI governance, risk & compliance solutions for manufacturing and other businesses.

[![Docker](https://img.shields.io/badge/Docker-Enabled-blue)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-green)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.43+-red)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Quick Start

### Prerequisites
- **Superwise Account**: Create account and application (see [Superwise Agent Setup Guide](docs/SUPERWISE_AGENT_SETUP_GUIDE.md#prerequisites--account-setup))
- Web browser 
- Git

**Option 1: Docker (Recommended)**
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

**Option 2: Local Python Installation**
- Python 3.11 or higher
- pip (Python package manager)

### Running the Application

#### Option 1: Docker (Recommended)

1. **Clone, configure, and run:**
   ```bash
   git clone <repository-url>
   cd manufacturing_ai
   cp .env.example .env
   # Edit .env file with your configuration
   docker-compose up --build
   ```

2. **Access the application:**
   - **Dashboard:** http://localhost:8501

#### Option 2: Local Python Installation

1. **Clone, configure, and run:**
   ```bash
   git clone <repository-url>
   cd manufacturing_ai
   cp .env.example .env
   # Edit .env file with your configuration
   ```

2. **Run the application:**
   
   ```bash
   streamlit run app/main.py --server.port 8501 --server.address 0.0.0.0
   ```

3. **Access the application:**
   - **Dashboard:** http://localhost:8501

## 📊 Features

### 🤖 AI-Powered Predictions
- **Real-time Risk Assessment:** Multi-parameter failure prediction
- **Risk Classification:** Low, Medium, High risk levels with confidence scores
- **Failure Timeline:** Predicted days to failure with recommendations
- **Cost Analysis:** ROI calculations and savings projections

### 📈 Interactive Dashboard
- **Live Machine Status:** Real-time monitoring of all equipment
- **Interactive Visualizations:** Charts and graphs for trend analysis
- **Maintenance Scheduling:** Automated maintenance recommendations
- **Alert System:** Visual alerts for high-risk machines

### 🔌 RESTful API
- **Complete API:** Full REST API for system integration
- **Real-time Predictions:** POST endpoints for instant failure predictions
- **Machine Management:** CRUD operations for machine data
- **Maintenance Tracking:** Schedule and history management

## 🛡️ Guardrails & Telemetry

### AI Safety Guardrails

#### Machine Lifecycle Guardrails
- **End-of-Service Life Detection:** Prevents analysis of machines that have reached their end-of-service life based on maintenance records
- **Irreversible Wear Detection:** Prevents analysis of machines with documented irreversible wear conditions
- **Non-Functional Machine Filtering:** Blocks AI analysis for machines that are effectively non-functional and no longer generating valid sensor data
- **Maintenance Status Validation:** Ensures only operational machines are included in predictive analysis

### Guardrail Benefits
- **Prevents False Predictions:** Avoids AI analysis on non-functional machines
- **Ensures Data Quality:** Validates input data before processing
- **Reduces Maintenance Costs:** Prevents unnecessary actions on end-of-life equipment
- **Improves Reliability:** Ensures only valid, operational machines are analyzed

### Telemetry & Monitoring
- **Application Logs:** Located in `/logs` directory with daily rotation
- **Streamlit Health:** Built-in Streamlit health endpoint at `/_stcore/health`
- **Real-time Monitoring:** Live machine status and sensor data visualization
- **Error Tracking:** Comprehensive error logging and reporting
- **Performance Metrics:** Real-time dashboard metrics and system overview

### Where to Find Telemetry
- **Log Files:** `logs/manufacturing_ai_YYYYMMDD.log` (daily rotation)
- **Streamlit Health:** http://localhost:8501/_stcore/health
- **System Status:** Dashboard footer shows real-time system status and last update time
- **Error Reports:** Available in application logs and console output
- **Docker Health Check:** Container health monitoring via Docker Compose

## 📁 Project Structure

```
manufacturing_ai/
├── app/                        # Main application directory
│   ├── front_end/              # Streamlit frontend
│   │   ├── dashboard.py        # Main dashboard page
│   │   ├── machines.py         # Machines overview page
│   │   ├── machine_details.py  # Individual machine details
│   │   └── header.py           # Dashboard header component
│   ├── config/                 # Configuration management
│   │   ├── app_config.py       # Application configuration settings
│   │   └── front_end_config.py # Frontend configuration
│   ├── client/                 # External API clients
│   │   └── swe_client.py       # Superwise AI client
│   ├── services/               # Business logic services
│   │   ├── __init__.py
│   │   └── machines_service.py # Machine management service
│   ├── utils/                  # Utility functions
│   │   ├── __init__.py
│   │   ├── data_loader.py      # Data loading utilities
│   │   ├── predictor.py        # AI prediction algorithms
│   │   ├── logger_config.py    # Logging configuration
│   │   └── css_styles.py       # Custom CSS styles
│   ├── assets/                 # Static assets
│   │   ├── superwise_logo.svg  # Company logo
│   │   └── Group 11.svg        # App icon
│   ├── __init__.py
│   └── main.py                 # Streamlit main application
├── synthetic-data/             # Sample data files
│   ├── synthetic_sensor_data.csv
│   ├── synthetic_sensor_data.json
│   ├── synthetic_sensor_data.txt
│   ├── synthetic_maintenance_records.csv
│   ├── synthetic_maintenance_records.json
│   ├── synthetic_maintenance_records.txt
│   └── CNC Machine Sensor Risk Guide.pdf
├── tests/                      # Test suite
│   ├── __pycache__/
│   ├── test_api.py            # API tests
│   └── test_front_end.py      # Frontend tests
├── docs/                       # Documentation
│   ├── DOCKER_README.md       # Docker setup and deployment guide
│   ├── SUPERWISE_AGENT_SETUP_GUIDE.md # Superwise AI integration guide
│   └── USAGE.md               # User guide
├── logs/                       # Application logs (daily rotation)
│   ├── manufacturing_ai_YYYYMMDD.log
├── Dockerfile                  # Docker configuration
├── docker-compose.yml         # Docker Compose setup
├── cloudbuild.yaml            # Google Cloud Build configuration
├── requirements.txt           # Python dependencies
├── pytest.ini               # Pytest configuration
├── LICENSE                   # MIT License
└── README.md                 # This file
```

## 🛠️ Technology Stack

### Core Technologies
- **Frontend:** Streamlit 1.43.2 for interactive web dashboards and data visualization
- **Data Processing:** Pandas 2.2.2 and NumPy 2.0.0 for data manipulation and analysis
- **Visualization:** Plotly 5.20.0 for interactive charts and graphs
- **AI Integration:** Superwise AI API for advanced machine learning predictions
- **Python Runtime:** Python 3.11+ (slim Docker image)

### Development & Deployment
- **Containerization:** Docker and Docker Compose for easy deployment
- **Testing:** Pytest with coverage reporting (HTML, XML, terminal output)
- **Configuration:** Environment-based configuration with python-dotenv 1.0.1
- **HTTP Client:** Requests 2.32.0 for external API communication
- **Data Validation:** Pydantic 2.5.3 for data models and validation
- **Cloud Deployment:** Google Cloud Build (cloudbuild.yaml)
- **Version Control:** Git for source code management

## 🌐 Application Interface

### Web Application Access
- **Main Dashboard:** http://localhost:8501
- **Machine Overview:** Accessible through the web interface
- **Machine Details:** Individual machine analysis pages
- **Superwise AI Chat:** Built-in AI assistant interface

### Example Usage

**Access the Application:**
- **Dashboard:** http://localhost:8501
- **Streamlit Health:** http://localhost:8501/_stcore/health

**Superwise AI Integration:**
The application includes built-in Superwise AI integration accessible through the web interface. No separate API calls are needed - simply use the chat interface in the application.

## ⚙️ Configuration

### Environment Variables Setup

1. **Copy the environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file with your configuration:**
   ```bash   
   # Superwise AI Integration
   SUPERWISE_BASE_URL=https://api.superwise.ai/v1
   SUPERWISE_APP_ID=your_superwise_app_id_here
   
   # Data Configuration
   DATA_DIR=synthetic-data
   
   # Logging Configuration
   LOG_LEVEL=INFO
   LOG_DIR=   
   
   # API Timeouts and Caching
   REQUEST_TIMEOUT=30
   CACHE_TTL=60
   ```

### Required Environment Variables
- `SUPERWISE_APP_ID` - Your Superwise AI application ID

### Optional Environment Variables
- `LOG_LEVEL` - Logging level (default: INFO)
- `DATA_DIR` - Data directory path (default: synthetic-data)

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage (HTML, XML, and terminal reports)
python -m pytest tests/ --cov=app --cov-report=html --cov-report=xml --cov-report=term-missing

# Run specific test files
python -m pytest tests/test_front_end.py -v

# Run tests with markers (slow, integration, unit)
python -m pytest tests/ -m "not slow" -v

# Run tests with verbose output and short traceback
python -m pytest tests/ -v --tb=short
```

### Test Structure
- **Frontend Tests:** Streamlit component and service layer testing (`test_front_end.py`)
- **Data Tests:** Data loading and processing validation
- **Prediction Tests:** AI algorithm accuracy and edge case testing
- **Service Tests:** Business logic and machine management testing

### Test Coverage
- **Data Loading:** Sensor data and maintenance records validation
- **Predictive Analytics:** Failure risk calculation and cost savings
- **Service Layer:** Machine management and health monitoring
- **Edge Cases:** Extreme values and boundary condition testing
- **Data Consistency:** Cross-component data validation

### Available Test Categories
- **Unit Tests:** Individual component testing
- **Integration Tests:** Cross-component interaction testing
- **Data Tests:** Data processing and validation
- **Prediction Tests:** AI algorithm accuracy testing

## 🔒 Data Privacy & Compliance

### **Important Disclaimers**

⚠️ **This application uses SYNTHETIC DUMMY DATA for demonstration purposes only.**

- **No Real Machine Data**: All machine and sensor information in this application is artificially generated
- **Educational Purpose**: This is a demonstration/educational project, not a production machine monitoring system
- **Data Sources**: Machine and sensor data comes from `synthetic_maintenance_records.csv` and `synthetic_sensor_data.csv`

🚨 **CRITICAL SECURITY LIMITATIONS - NOT PRODUCTION READY:**

- **No Authentication**: Application has no user login or authentication system
- **No Authorization**: No access controls or user permission management
- **No Data Encryption**: Machine data is stored and transmitted without encryption
- **No Session Management**: No secure session handling or user state management
- **No Access Logging**: No audit trails for data access or user activities
- **No Input Validation**: Limited input sanitization and validation
- **No HTTPS Enforcement**: No SSL/TLS encryption for data transmission

**⚠️ DO NOT USE WITH REAL MANUFACTURING MACHINE DATA - FOR DEMONSTRATION ONLY**

### Data Handling
- **Local Processing:** All data processing occurs locally on your infrastructure
- **No External Data Sharing:** Data is not transmitted to external services (except Superwise AI with explicit consent)
- **Data Retention:** Logs and data are stored locally with configurable retention policies
- **Access Control:** Environment-based configuration for secure access

### Compliance Features
- **GDPR Ready:** Data processing follows privacy-by-design principles
- **Audit Logging:** Comprehensive logging for compliance tracking
- **Secure Configuration:** Environment variables for sensitive data management

### GDPR Considerations
- **Local Processing:** All data processing occurs locally on user infrastructure
- **Synthetic Data:** Uses only synthetic/demo data for demonstration purposes
- **No Personal Data:** The system processes only machine sensor data (vibration, temperature, current, pressure) and maintenance records
- **Clear Purpose:** Data processing is limited to predictive maintenance analysis
- **Environment Variables:** Sensitive configuration stored in environment variables
- **Local Storage:** Data stored locally with no external transmission (except optional Superwise AI integration)
- **Input Validation:** Comprehensive data validation and sanitization
- **Error Handling:** Secure error messages without data exposure
- **Clear Documentation:** Comprehensive privacy and compliance documentation
- **Data Sources:** Clearly documented data sources and processing purposes
- **Configuration:** Transparent configuration management
- **Comprehensive Logging:** Detailed audit logs for all operations
- **Compliance Tracking:** Logging specifically designed for compliance tracking
- **Data Processing Records:** Complete records of data processing activities

### Data Sources
- **Synthetic Data:** Pre-loaded sample data for demonstration
- **Data Validation:** Input validation and sanitization
- **Error Handling:** Secure error messages without data exposure

**For Production Use:**
- **GDPR Compliance**: Ensure proper GDPR compliance before handling real machine data
- **Data Encryption**: Use encryption for data at rest and in transit
- **Access Controls**: Implement proper user authentication and authorization
- **Audit Logging**: Maintain comprehensive audit trails for all data access
- **Business Associate Agreements**: Ensure all third-party services (like Superwise API) have proper BAAs

**Current Implementation:**
- ✅ **Synthetic Data Only**: No real machine data is processed
- ✅ **Local Processing**: Data stays within your local environment
- ✅ **No External Storage**: No data is sent to external databases
- ⚠️ **API Integration**: Superwise API calls may transmit synthetic data (configure accordingly)

**Note**: This application is for educational/demonstration purposes. For production applications, consult with legal and compliance experts regarding GDPR requirements.

## 📊 Demo Data

The application comes with pre-loaded simulated data:

- **7 Manufacturing Machines:** CNC_1 through CNC_7
- **Sensor Parameters:** Vibration, temperature, current, pressure
- **Maintenance Records:** Service history and scheduling
- **Risk Levels:** Low, Medium, High risk classifications

## 🎯 Use Cases

### Manufacturing Operations
- **Predictive Maintenance:** Prevent equipment failures before they occur
- **Cost Optimization:** Reduce unplanned downtime and maintenance costs
- **Resource Planning:** Optimize maintenance schedules and resource allocation
- **Quality Assurance:** Maintain consistent production quality

### Integration Scenarios
- **ERP Integration:** Connect with existing enterprise systems
- **IoT Integration:** Real-time sensor data processing
- **Reporting Systems:** Automated maintenance reporting
- **Alert Systems:** Email/SMS notifications for critical alerts

## 🔍 Code Quality & Linting

### Code Standards
- **PEP 8 Compliance:** Python code follows PEP 8 style guidelines
- **Type Hints:** Comprehensive type annotations for better code maintainability
- **Documentation:** Inline documentation and docstrings for all functions
- **Error Handling:** Robust error handling throughout the application

### Linting Tools
```bash
# Run linting checks
flake8 app/ --max-line-length=88 --extend-ignore=E203,W503
black app/ --check
```

### Code Quality Features
- **Modular Design:** Clean separation of concerns
- **Configuration Management:** Centralized configuration system
- **Logging:** Comprehensive logging throughout the application
- **Testing:** High test coverage with unit and integration tests

## 📚 Documentation

### Available Documentation
- **[Docker Setup Guide](docs/DOCKER_README.md)** - Complete Docker deployment and configuration guide
- **[Superwise Agent Setup](docs/SUPERWISE_AGENT_SETUP_GUIDE.md)** - AI agent configuration and integration guide
- **[User Guide](docs/USAGE.md)** - Step-by-step user walkthrough and features
- **[Application Interface](http://localhost:8501)** - Interactive web application
- **[Environment Setup](.env.example)** - Environment variables configuration template
- **[Youtube Video](https://www.youtube.com/watch?v=9fYt_X5hz-c)** - Manufacturing AI Demo: Predictive Maintenance & Risk Assessment with SUPERWISE® Platform

### Documentation Structure
- **Technical Docs:** Docker deployment, Superwise AI integration, and API specifications
- **User Guides:** Dashboard usage, feature explanations, and troubleshooting
- **Configuration:** Environment setup and customization options
- **Examples:** Code examples and integration patterns

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Getting Help
- **Documentation:** Check the comprehensive guides in the `docs/` folder
- **Application Interface:** Visit http://localhost:8501 for the interactive web application

### Troubleshooting
- **Common Issues:** Check the [User Guide](docs/USAGE.md) for troubleshooting steps
- **Configuration:** Verify your `.env` file matches the `.env.example` template
- **Logs:** Check the `logs/` directory for detailed error information
- **Health Check:** Visit http://localhost:8501/_stcore/health to verify system status


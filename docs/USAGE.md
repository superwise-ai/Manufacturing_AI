# User Guide and Demo Walkthrough

## 🎯 Getting Started

This guide will walk you through the Manufacturing Predictive Maintenance AI system, demonstrating all features and capabilities.

## 📋 Prerequisites

Before starting, ensure you have:
- **Option 1 (Docker):** Docker and Docker Compose installed
- **Option 2 (Local Python):** Python 3.11+ and pip installed
- Web browser (Chrome, Firefox, Safari, or Edge)
- Basic understanding of manufacturing operations

## 🚀 Quick Start

### Option 1: Docker Deployment (Recommended)

1. **Start the services:**
   ```bash
   docker-compose up --build
   ```

2. **Wait for services to be ready:**
   - Look for "Application startup complete" in the logs
   - Dashboard should be running

3. **Access the dashboard:**
   - Open your browser to http://localhost:8501
   - The Streamlit dashboard should load automatically

### Option 2: Local Python Installation

1. **Clone and configure:**
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

3. **Access the dashboard:**
   - Open your browser to http://localhost:8501
   - The Streamlit dashboard should load automatically

**Note:** The startup scripts automatically create and activate a virtual environment, install dependencies, and start the services.

### Step 2: Verify System Health

1. **Access the application:**
   - **Dashboard:** http://localhost:8501

2. **Check system logs:**
   - Review logs in the `/logs` directory
   - Look for any guardrail triggers or system warnings

## 📊 Dashboard Walkthrough

### Overview Page

The **Overview** page provides a high-level view of your manufacturing operations:

#### Key Metrics
- **Total Machines:** Number of monitored equipment
- **High Risk Machines:** Equipment requiring immediate attention
- **Medium Risk Machines:** Equipment needing scheduled maintenance
- **Low Risk Machines:** Equipment operating normally

#### Machine Status Distribution
- **Pie Chart:** Visual representation of risk distribution
- **Color Coding:**
  - 🟢 Green: Low risk (normal operation)
  - 🟡 Yellow: Medium risk (attention needed)
  - 🔴 Red: High risk (immediate action required)

#### Machine Status Table
- **Real-time Data:** Synthetic sensor readings for each machine 
- **Status Indicators:** Current risk level for each machine
- **Last Reading:** Timestamp of most recent sensor data

### Machine Details Page

The **Machine Details** page provides in-depth analysis for individual machines:

#### Machine Selection
1. **Select Machine:** Click on "View Details" button to choose a specific machine
2. **Real-time Status:** View current risk assessment and recommendations

#### Maintenance Information Section
- **Machine:** Machine Id
- **Service Notes:** Detailed maintenance history and notes

#### Historical Data Visualization
- **Multi-parameter Charts:** Vibration, temperature, current, and pressure trends
- **Time Series Analysis:** Historical data patterns and trends
- **Interactive Graphs:** Zoom and pan capabilities for detailed analysis

#### Superwise AI Assistant
- **AI Analysis:** Ask questions about machine maintenance and predictions
- **Contextual Questions:** Pre-configured questions with maintenance data context
- **Service Notes Integration:** AI has access to complete maintenance history
- **Professional Analysis:** AI provides detailed analysis with tables and recommendations

## 🛡️ AI Safety Guardrails

The system includes comprehensive AI safety guardrails to ensure reliable and safe operation:

### Machine Lifecycle Guardrails
- **End-of-Service Life Detection:** Automatically prevents analysis of machines that have reached their end-of-service life
- **Irreversible Wear Detection:** Blocks AI analysis for machines with documented irreversible wear conditions

### Guardrail Benefits
- **Prevents False Predictions:** Avoids AI analysis on non-functional machines
- **Ensures Data Quality:** Validates input data before processing
- **Reduces Maintenance Costs:** Prevents unnecessary actions on end-of-life equipment
- **Improves Reliability:** Ensures only valid, operational machines are analyzed

## 🤖 Superwise AI Integration

The system includes advanced AI integration through Superwise AI for enhanced predictive maintenance analysis:

### AI Assistant Features
- **Contextual Analysis:** AI has access to complete machine maintenance history
- **Service Notes Integration:** AI can analyze service notes and maintenance records
- **Professional Recommendations:** AI provides detailed analysis with tables and formatting
- **Risk Assessment:** AI evaluates machine health based on multiple data sources

### Using the AI Assistant
1. **Navigate to Machine Details:** Select a specific machine from the dashboard
2. **View Pre-configured Question:** The system automatically generates a contextual question
3. **Click "Ask Superwise":** Submit the question to the AI for analysis
4. **Review AI Response:** Get detailed analysis with recommendations

### AI Question Examples
- **Maintenance Analysis:** "Analyze maintenance records and all sensor data for CNC machine with machine_id as CNC_1 and service_notes as Regular maintenance - replaced filters. Please suggest failure rate, predicted days to failure and next recommended service date."
- **Risk Assessment:** "Evaluate the current risk level for machine CNC_2 based on recent sensor readings and maintenance history."
- **Predictive Insights:** "Based on the maintenance schedule and current sensor data, predict potential issues for the next 30 days."

### AI Response Features
- **Professional Formatting:** Responses include tables, headers, and structured data
- **Actionable Recommendations:** Specific maintenance actions and timelines
- **Risk Analysis:** Detailed risk assessment with confidence levels
- **Cost-Benefit Analysis:** Financial impact of maintenance decisions

## 🚨 Troubleshooting

### Common Issues

#### Dashboard Not Loading
1. **Check Docker Status:** Ensure containers are running
2. **Verify Ports:** Check if ports 8501 are available
3. **Check Logs:** Review container logs for errors
4. **Restart Services:** Try `docker-compose restart`

#### Data Not Updating
1. **Refresh Dashboard:** Reload the browser page
2. **Check Data Files:** Verify CSV files are present and readable
3. **Restart Services:** Restart all containers
4. **Check Logs:** Review application logs for errors

#### Superwise AI Not Responding
1. **Check API Configuration:** Verify SUPERWISE_APP_ID has set
2. **Check Network:** Ensure internet connection for Superwise AI API calls
3. **Review Logs:** Check for API timeout or authentication errors
4. **Test API:** Use the health check endpoint to verify API connectivity

#### Virtual Environment Issues (Local Installation)
1. **Check Python Version:** Ensure Python 3.11+ is installed
2. **Check Dependencies:** Verify all packages are installed correctly
3. **Check Permissions:** Ensure write permissions for the project directory

### Performance Optimization

#### For Large Datasets
1. **Increase Memory:** Allocate more RAM to Docker
2. **Optimize Data:** Use data sampling for large datasets
3. **Caching:** Enable data caching for better performance
4. **Database:** Consider migrating to a proper database

#### For High Traffic
1. **Load Balancing:** Use multiple API instances
2. **Caching:** Implement Redis caching
3. **CDN:** Use content delivery network for static assets
4. **Monitoring:** Set up performance monitoring

## 📚 Advanced Features

### Custom Data Integration

#### Adding New Machines
1. **Update CSV Files:** Add new machine data to sensor_data.csv
2. **Update Maintenance Records:** Add maintenance history
3. **Restart Services:** Reload the application
4. **Verify Integration:** Check dashboard for new machine

#### Custom Risk Thresholds
1. **Modify Predictor:** Update thresholds in predictor.py
2. **Restart API:** Restart the FastAPI service
3. **Test Changes:** Verify new thresholds work correctly
4. **Monitor Results:** Check prediction accuracy

### Integration with External Systems

#### ERP Integration
1. **API Endpoints:** Use REST API for data exchange
2. **Data Mapping:** Map ERP data to system format
3. **Scheduled Updates:** Set up automated data synchronization
4. **Error Handling:** Implement robust error handling

#### IoT Sensor Integration
1. **Data Format:** Ensure sensor data matches expected format
2. **API Integration:** Use prediction endpoints for real-time data
3. **Data Validation:** Implement data quality checks
4. **Monitoring:** Set up continuous monitoring

## 🎓 Best Practices

### Data Management
1. **Regular Backups:** Backup CSV files regularly
2. **Data Validation:** Validate sensor data quality
3. **Historical Data:** Maintain sufficient historical data
4. **Data Cleaning:** Remove outliers and invalid data

### Maintenance Scheduling
1. **Proactive Approach:** Schedule maintenance based on predictions
2. **Resource Planning:** Allocate maintenance resources efficiently
3. **Cost Optimization:** Balance maintenance costs with downtime costs
4. **Documentation:** Maintain detailed maintenance records

### System Monitoring
1. **Health Checks:** Monitor system health regularly
2. **Performance Metrics:** Track system performance
3. **Alert Management:** Set up appropriate alerts
4. **Log Analysis:** Regular log analysis for issues

## 📞 Support and Resources

### Getting Help
1. **Documentation:** Check this guide and architecture docs
2. **Logs:** Review application logs for error details
3. **Community:** Check project repository for issues and discussions

### Additional Resources
- **Streamlit Documentation:** https://docs.streamlit.io/
- **Docker Documentation:** https://docs.docker.com/
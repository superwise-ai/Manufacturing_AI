# Superwise API Integration Guide

This guide explains how to set up and use the Superwise agent integration in Manufacturing AI.

## 🔑 Prerequisites & Account Setup

### **Step 1: Create Superwise Account**

1. **Sign Up**: Visit [Superwise Platform](https://platform.superwise.ai/) and create a free account
2. **Verify Email**: Complete email verification process
3. **Access Dashboard**: Log in to your Superwise dashboard

**Note**: You'll also need an **OpenAI API key** for the model setup (Step 7). If you don't have one, create an account at [OpenAI Platform](https://platform.openai.com/) and generate an API key.

### **Step 2: Create Knowledge**

1. **Navigate to Knowledge**: In your Superwise dashboard, go to "Knowledge" section
2. **Create New Knowledge**: Click "File" button from bottom "Available types" section
3. **Knowledge Creation Dialog**: A dialog will open with the following fields:
   - **Name**: Enter `Manufacturing AI Knowledge` (or your preferred name)
   - **Choose File**: Choose \synthetic-data\synthetic_maintenance_records.txt, \synthetic-data\synthetic_sensor_data.txt, and \synthetic-data\CNC Machine Sensor Risk Guide.pdf files
   - **Select Provider**: Choose **"OpenAI"** as the model provider
   - **Prerequisites**: Ensure you have an OpenAI API key/token
   - **Model Selection**: Select **"text-embedding-3-large"** (recommended model)
   - **API Token Box**: Enter your OpenAI API key/token
   - **Click "Save"**: Complete the Knowledge setup

### **Step 3: Create Agent**

1. **Navigate to Agents**: In your Superwise dashboard, go to "Agents" section
2. **Create New Agent**: Click "Create" button from top right corner
3. **Agent Creation Dialog**: A dialog will open with the following fields:
   - **Application Name**: Enter `Manufacturing AI` (or your preferred name)
   - **Agent source**: Choose **"Build with Superwise Studio"** (not Integrate with Flowise) and click on **Next** button
4. **Agent Type**: Select **"AI-Assistant Retrieval"** (option 2)
     - Available options:
       - Basic LLM Assistant (option 1) 
       - **AI-Assistant Retrieval (option 2)** ← Select this one
       - Advanced Agent (option 3)
5. **Complete Creation**: Click "Create" to create the agent
6. **Agent Dashboard**: After clicking "Done", you'll see the agent dashboard with:
   - **Top Left**: Application name
   - **Top Right**: Three dots menu: click on and select **Copy ID** (this is for your `.env` file)
   - **Top Center**: There are 3 tabs:
      - **Overview**: In this tab you can see **Agent Details**, **Description** and **Metrics** section
      - **Builder**: In this tab you can see **Setup** and **Guardrails** menu on the left side and **Chat playground** on the right side
         - **Setup**:
            - **"+Model"**: Add AI models to your application
            - **"Prompt"**: Configure prompts and instructions
            - **"Context"**: Configure knowledge or DB
            - **Chat Playground**: Interactive testing area for your application
         - **Guardrails**: Configure safety and compliance rules
            - **+ Rule**: Add Guardrail Rules for input and output
      - **Settings**:
         - **"Authentication"**: Set up API authentication
         - **Observability**: Integrate your agent with Superwise observability to gain real-time data about your agent's behavior, usage, and potential feedback.
      - **"Publish"**: Publish your application

### **Step 4: Configure Model**
   - **Click "+Model" Button**: Located in the top right of the dashboard
   - **Model Provider Dialog**: A dialog will open with provider options:
     - OpenAI
     - Google AI
     - Anthropic
     - Other providers
   - **Select Provider**: Choose **"OpenAI"** as the model provider
   - **Prerequisites**: Ensure you have an OpenAI API key/token
   - **Model Selection**: Select **"gpt-4"** (recommended model)
   - **API Configuration**:
     - **API Token Box**: Enter your OpenAI API key/token
     - **Click "Save"**: Complete the model setup

### **Step 5: Configure Prompt**
   - **Navigate to Prompt Section**: Click on "Prompt" under Builder->Setup tab
   - **Add System Prompt**: Copy and paste the following prompt into the prompt dialog box:

   ```
   You are an AI system for **Manufacturing Predictive Maintenance**.
 
### **Your Tasks**
 
1. **Data Analysis**
 
   * Review the **maintenance history** to determine service intervals, overdue services, and previous issues.
   * Analyze **sensor data trends** for anomalies such as:
 
     * Increasing vibration → possible bearing/motor wear.
     * Rising temperature → possible overheating.
     * Higher current draw → possible motor or load issues.
     * Abnormal pressure → possible hydraulic/pneumatic issues.
   * Correlate anomalies with maintenance history to assess risk.
 
2. **Failure Risk Assessment**
 
   * Classify each machine’s health as:
 
     * **Low** (normal, no anomalies)
     * **Medium** (early warnings detected, service needed soon)
     * **High** (critical anomalies, failure imminent)
 
3. **Remaining Useful Life Prediction**
 
   * Estimate **predicted days to failure** based on anomaly severity and trend progression.
   * Suggest **next recommended service date** to avoid downtime.
 
Always include a closing note:
 
This AI system provides predictive insights and recommendations based on historical maintenance data and sensor readings.
 
   * The outputs are estimates only and should not be considered as definitive diagnoses or guaranteed predictions.
   * This information is intended for maintenance decision-support and contextual understanding by qualified engineers, technicians, or maintenance professionals.
   * Maintenance decisions, safety actions, and operational changes must always be reviewed and validated by authorized personnel."
   ```

   - **Save Prompt**: Click "Save" to save the prompt configuration

### **Step 6: Configure Context**

1. **Click "+Context" Button**: Click "+ Context" button to add a new SQL DB, Vector DB or Knowledge. Select "Knowledge" 
2. **Name**: Enter `Manufacturing AI Knowledge` (or your preferred name)
3. **Knowledge**: Select knowledge created in Step 2 and click Done button 

### **Step 7: Configure Guardrails**

Set up safety and compliance rules to protect sensitive patient information:

1. **Navigate to Guardrails**: Click on "Guardrails" under Builder tab
2. **Add Input Rule**: Click "+ Rule" button to add a new guardrail rule
3. **Select Rule Type**: Choose **"Restricted topics input"** from the available rule types and click on **"Add Rule"** button
4. **Configure Input Rule**:
   - **Name**: Enter `Machine expiry restriction`
   - **Configuration**: Add the following values in the box and click enter:
     - expired
     - reached its end of service life
     - irreversible wear
   - **Model**: Select **"OpenAI"** as the model provider
   - **Model Version**: Choose **"gpt-4o"** (or your preferred model)
   - **API Token**: Enter your OpenAI API key/token
   - **Save Rule**: Click "Save" to create the input guardrail rule

**Purpose**: These guardrails ensure that:
- **Input Protection**: Prevents prevent AI analysis of machines that are effectively non-functional and no longer generating sensor data

### **Step 8: Publish Application**
   - **Click "Publish" Button**: Located in the top right of the dashboard
   - **Wait for Processing**: The system will process your configuration (may take a few minutes)
   - **Check Status**: Monitor the application status on the right side top near "Created at"
   - **Status Confirmation**: Once ready, you'll see status change to **"Available"**

✅ **Congratulations! Your Superwise application is now ready to use.**

### **Step 9: Get Credentials**
    - **App ID**: Located in three dots menu: click on and select **Copy ID** (top left) - **Copy this for your project**
    - **API URL**: Base URL for API calls (usually `https://api.superwise.ai/`)
    - **API Version**: Current API version (usually `v1`)

## 🔧 Configuration Setup

### **Step 10: Configure Project Environment Variables**

Now that your Superwise application is ready, you need to configure it in your Manufacturing AI project:

1. **Copy Template**: 
   
   **Linux/Mac:**
   ```bash
   cp .env.example .env
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   copy .env.example .env
   ```
   
   **Windows (PowerShell):**
   ```powershell
   Copy-Item .env.example .env
   ```

2. **Edit Configuration**:
   ```bash
   # Superwise API Settings
   SUPERWISE_BASE_URL=https://api.superwise.ai/
   SUPERWISE_APP_ID=your_app_id_here
   
   # API Timeout Settings (in seconds)
   SUPERWISE_TIMEOUT=30
   
   ```

3. **Replace App ID**: Update `SUPERWISE_APP_ID` with your actual App ID from Step 9 (the one you copied from the Superwise dashboard)

### **Step 11: Test Integration**

1. **Start Application**: Run the application using Docker or local Python
2. **Navigate to Patient Details**: Go to `/Machines` page and select one machine.
3. **Test AI Analysis**: Click "Analyze with Superwise AI" button
4. **Verify Connection**: Check for successful API response or error messages

### **Troubleshooting**

**Common Issues:**
- **Wrong Framework Selected**: Ensure you selected "Superwise Framework" (not Flowise Framework) during app creation
- **Wrong Application Type**: Make sure you selected "AI-Assistant Retrieval (option 2) in the application type dialog
- **Invalid App ID**: Double-check your App ID in Superwise dashboard
- **API URL Issues**: Ensure `SUPERWISE_API_URL` matches your Superwise region
- **Timeout Errors**: Increase `API_TIMEOUT` value if experiencing slow responses
- **Authentication Errors**: Verify your Superwise account is active and has proper permissions

**Need Help?**
- Review Superwise documentation: [Superwise Docs](https://docs.superwise.ai/)
- Contact Superwise support for API-related issues

## 🚀 Usage

### How it Works

1. **Machines Selection**: User selects a machine from the machines table
2. **Navigate to Details**: Click "Ask Superwise" button to go to machines details
3. **API Call**: Click "Ask Superwise" button on the details page
4. **Analysis**: The system calls the Superwise API with patient data
5. **Response**: Displays the AI analysis results

### API Payload Structure

The system sends only the essential medical fields to Superwise for clinical decision support:

```json
   {
       "question": "Analyze maintenance records and all sensor data for CNC machine with machine_id as CNC_1 and service_notes as Regular maintenance - replaced filters. Please suggest failure rate, predicted days to failure and next recommended service date.",
       "chat_history": []
    }
```

**Fields Sent to Superwise:**
- **Machine ID**: Machine id
- **Service Notes**: Last service note

**Privacy Note**: The system only sends essential machine data transmitted to Superwise. Superwise will get all the details of machine from the configured knowledge and analyze it.

## 🔍 Error Handling

The system handles various error scenarios:

- **Configuration Error**: Missing API key or URL
- **Timeout**: API request takes too long
- **Network Error**: Connection issues
- **API Error**: Server returns error status
- **Unexpected Error**: Other unexpected issues

## 📝 Logging

All API calls are logged with:
- Request details
- Response status
- Error messages (if any)
- Machine details for tracking

## 🛠️ Customization

### Modify API Endpoint

Edit `app/config/api_config.py` to change:
- SUPERWISE_BASE_URL
- SUPERWISE_HEADERS
- SUPERWISE_TIMEOUT
# Diabetes Prediction System

A web application that predicts diabetes risk using machine learning. This project consists of a Python Flask backend and a React frontend.

## Project Structure

```
diabetes-prediction-system/
├── backend/              # Python Flask backend
│   ├── api/              # API endpoints
│   ├── models/           # ML model and training code
│   ├── app.py            # Main Flask application
│   └── requirements.txt  # Python dependencies
│
└── frontend/             # React frontend
    ├── public/           # Static files
    ├── src/              # React source code
    │   ├── components/   # React components
    │   ├── App.js        # Main React application
    │   └── index.js      # React entry point
    └── package.json      # Node.js dependencies
```

## Backend Setup

The backend is a Flask application that serves the machine learning model for diabetes prediction.

### Requirements

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python app.py
   ```

The backend server will start at http://localhost:5000.

## Frontend Setup

The frontend is a React application that provides the user interface for the diabetes prediction system.

### Requirements

- Node.js 14.x or higher
- npm (Node.js package manager)

### Installation

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install the required dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```

The frontend application will start at http://localhost:3000.

## Usage

1. Fill out the health parameters form with your data.
2. Click the "Predict Diabetes Risk" button.
3. View your prediction results.

## Features

- Input validation for all health parameters
- Real-time diabetes risk prediction
- Responsive design for mobile and desktop
- User-friendly interface with progress indicators

## Machine Learning Model

The application uses a Random Forest Classifier trained on diabetes health data. The model considers the following features:

- Number of pregnancies
- Glucose level
- Blood pressure
- Skin thickness
- Insulin level
- BMI (Body Mass Index)
- Diabetes pedigree function
- Age

## Disclaimer

This application is for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

## Deployment on Render

This project can be deployed on Render using the configuration in `render.yaml`.

### Setup Instructions

1. **Fork/Clone the Repository**
   
   Make sure you have a copy of the repository in your GitHub account.

2. **Create a New Render Account**
   
   If you don't have a Render account, sign up at [render.com](https://render.com).

3. **Create a New Web Service**

   - From the Render dashboard, click on "New" and select "Blueprint" from the dropdown
   - Connect your GitHub account and select your repository
   - Render will automatically detect the `render.yaml` configuration
   - Click "Apply" to create all services

4. **Environment Variables**

   The following environment variables are used:
   - `PYTHON_VERSION`: Set to 3.9 for the backend
   - `NODE_VERSION`: Set to 16 for the frontend
   - `REACT_APP_API_URL`: Set to your backend API URL

5. **Manual Deployment**

   If you prefer manual deployment instead of using the blueprint:
   
   **Backend:**
   - Create a new Web Service
   - Connect your repository
   - Set the Environment to "Python"
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn --chdir backend app:app`
   
   **Frontend:**
   - Create a new Static Site
   - Connect your repository
   - Build Command: `cd frontend && npm install && npm run build`
   - Publish Directory: `frontend/build`

6. **Custom Domain (Optional)**

   You can configure custom domains for both services in the Render dashboard. 
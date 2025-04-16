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
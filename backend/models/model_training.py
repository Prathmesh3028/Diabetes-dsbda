import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os

def load_data():
    """
    If dataset doesn't exist, create sample data.
    In a real scenario, you would download the actual dataset.
    """
    try:
        # In a real scenario, you would use an actual dataset like:
        # data = pd.read_csv('path/to/diabetes-dataset.csv')
        
        # For demo purposes, we'll generate synthetic data
        # Based on Pima Indians Diabetes Dataset features
        np.random.seed(42)
        n_samples = 768
        
        # Generate synthetic data
        data = pd.DataFrame({
            'Pregnancies': np.random.randint(0, 17, n_samples),
            'Glucose': np.random.randint(50, 200, n_samples),
            'BloodPressure': np.random.randint(30, 120, n_samples),
            'SkinThickness': np.random.randint(0, 100, n_samples),
            'Insulin': np.random.randint(0, 850, n_samples),
            'BMI': np.random.uniform(15, 50, n_samples),
            'DiabetesPedigreeFunction': np.random.uniform(0.05, 2.5, n_samples),
            'Age': np.random.randint(21, 81, n_samples)
        })
        
        # Create target based on features (simplified model)
        # Higher glucose and BMI increase likelihood of diabetes
        probs = 1 / (1 + np.exp(-(data['Glucose']/100 + data['BMI']/25 - 3)))
        data['Outcome'] = (np.random.random(n_samples) < probs).astype(int)
        
        return data
        
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def train_model():
    """Train the diabetes prediction model"""
    # Ensure models directory exists
    os.makedirs('models', exist_ok=True)
    
    # Load data
    data = load_data()
    if data is None:
        print("Failed to load data. Cannot train model.")
        return False
    
    # Split features and target
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Preprocess data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print(f"Model Metrics:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    
    # Save model and scaler
    joblib.dump(model, 'models/diabetes_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    
    return True

if __name__ == "__main__":
    train_model() 
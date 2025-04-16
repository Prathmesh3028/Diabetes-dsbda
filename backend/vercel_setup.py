import os
import sys
import subprocess
import pkg_resources

# Define required packages
required_packages = [
    'flask==2.2.3',
    'flask-cors==3.0.10',
    'scikit-learn==1.2.2',
    'pandas==1.5.3',
    'numpy==1.24.2',
    'joblib==1.2.0'
]

def install_requirements():
    """Install required packages"""
    print("Checking and installing required packages...")
    
    # Check if packages are already installed
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = []
    
    for package in required_packages:
        package_name = package.split('==')[0]
        if package_name.lower() not in installed:
            missing.append(package)
    
    if missing:
        print(f"Installing missing packages: {', '.join(missing)}")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing)
    else:
        print("All required packages are already installed.")

def train_model():
    """Import and run model training"""
    try:
        print("Setting up model training...")
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        # Import model training module
        from models.model_training import train_model as train
        
        # Train the model
        print("Starting model training...")
        train()
        print("Model training complete!")
        
    except Exception as e:
        print(f"Error during model training: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("Starting Vercel setup...")
    install_requirements()
    train_model()
    print("Vercel setup complete!") 
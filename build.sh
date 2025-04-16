#!/bin/bash

# Print Python version
echo "Python version:"
python --version

# Install requirements using python -m pip
echo "Installing requirements..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Build frontend
echo "Building frontend..."
cd frontend
npm install
npm run build
cd ..

echo "Build completed successfully!" 
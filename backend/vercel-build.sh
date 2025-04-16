#!/bin/bash

# Install dependencies
pip install -r ../requirements.txt

# Run model training script
python -c "from models.model_training import train_model; train_model()"

echo "Model training completed for Vercel deployment" 
#!/usr/bin/env bash
# Exit on error
set -e

# Install Python dependencies
pip install -r requirements.txt

# Check if models directory exists, create if not
if [ ! -d "backend/models" ]; then
  mkdir -p backend/models
fi

# Train the model if needed
python -c "from backend.models.model_training import train_model; train_model()"

# Output build completed message
echo "Backend build completed successfully!" 
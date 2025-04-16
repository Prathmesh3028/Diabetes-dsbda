#!/bin/bash

# This script helps to diagnose and execute commands in the Vercel environment

# Print environment info
echo "Environment information:"
echo "======================="
pwd
ls -la
echo "Node version: $(node -v)"
echo "NPM version: $(npm -v)"
echo "Python version: $(python --version 2>&1)"
echo "Shell: $SHELL"
echo "PATH: $PATH"
echo "======================="

# Execute the command provided as argument
"$@" 
#!/usr/bin/env bash
# Quick setup script for Unix-like systems

set -e

echo "======================================================================"
echo "OpenEnv Course - Quick Setup"
echo "======================================================================"

# Check Python version
python_version=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
required_version="3.10"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "Error: Python 3.10+ is required (found $python_version)"
    exit 1
fi

echo "Python version: $(python3 --version)"

# Create virtual environment
echo ""
echo "======================================================================"
echo "Creating virtual environment..."
echo "======================================================================"

if [ -d "venv" ]; then
    echo "Virtual environment already exists"
    read -p "Recreate? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf venv
        python3 -m venv venv
    fi
else
    python3 -m venv venv
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "======================================================================"
echo "Upgrading pip..."
echo "======================================================================"
python -m pip install --upgrade pip

# Install requirements
echo ""
echo "======================================================================"
echo "Installing dependencies..."
echo "======================================================================"
pip install -r requirements.txt

# Success
echo ""
echo "======================================================================"
echo "Setup Complete!"
echo "======================================================================"
echo ""
echo "To activate the virtual environment:"
echo "  source venv/bin/activate"
echo ""
echo "To run Jupyter notebooks:"
echo "  jupyter notebook"
echo ""
echo "To start a module:"
echo "  cd module-1"
echo "  jupyter notebook notebook.ipynb"
echo ""
echo "======================================================================"

#!/bin/bash
# Script Name: setup.sh
# Description: Setup pip env environment for development
# Author: Mohamed Lamine KARTOBI
# Date: 20/07/2025
# Version: 1.0

export REQS_FILE="requirements.txt"
export UTILS="scripts/linux/utils.sh"

echo $UTILS

# Source external utilities
if ! source $UTILS; then
    print_err "Failed to source environment"
    exit 1
else
    print_success "Sourced environment successfully"
fi

# Check Python3 installation
print_info "Checking Python installation..."
python3 --version > /dev/null 2>&1
chkerr "Python is not installed or not found"
print_success "Python3 is installed."

# Create and activate venv
print_info "Creating venv environment..."
python3 -m pip install --upgrade pip
python3 -m venv venv
source venv/bin/activate
chkerr "Environment activation failed"
print_success "Environement was activated"

# Upgrade pip3 to avoid requirements installation issues
pip3 install --upgrade pip

# Install pip3 requirements
if [ -f $REQS_FILE ]; then
    print_info "Installing requirements..."
    pip3 install -r requirements.txt
else
    print_warning "The requirements.txt file does not exist."
fi

deactivate
#!/bin/bash
# Script Name: utils.sh
# Description: Include function for logs
# Author: Mohamed Lamine KARTOBI
# Date: 17/01/2025
# Version: 1.0

# === COLORS ===
RED='\033[31m'
GREEN='\033[32m'
YELLOW='\033[33m'
CYAN='\033[36m'
RESET='\033[0m'

# === FUNCTIONS ===
print_info() {
    echo -e "${CYAN}[INFO]${RESET} $1"
}

# Print a success message
print_success() {
    echo -e "${GREEN}[SUCCESS]${RESET} $1"
}

# Print an error message and exit
print_err() {
    echo -e "${RED}[ERROR]${RESET} $1" >&2
    exit 1
}

# Print a warning message
print_warning() {
    echo -e "${YELLOW}[WARNING]${RESET} $1"
}

chkerr () {
    if [ $? -ne 0 ]; then
        if [ "$1" != "" ]; then
            print_err "$1" >&2
        else
            print_err "failed." >&2
        fi
        exit 1
    fi
    if [ "$1" = "" ]; then
        print_success "done."
    fi
}
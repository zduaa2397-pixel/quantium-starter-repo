#!/bin/bash

# Step 1: Activate the virtual environment
source venv/Scripts/activate

# Step 2: Run the test suite
pytest test_app.py

# Step 3: Capture pytest's exit code and exit with it
if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
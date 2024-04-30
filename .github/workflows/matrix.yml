
name: Python Script Workflow

on:
  push:
    branches:
      - main

jobs:
  run_python_script:
    name: Run juesttingcode.py
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2
      
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.12' # Use the Python version you need

    - name: Install dependencies
      run: python -m pip install --upgrade pip && python -m pip install -r requirements.txt

    - name: Run juesttingcode.py
      run: python juesttestingcode.py

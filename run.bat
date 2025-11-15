@echo off
echo Testing Python in Jenkins...
python --version
pip install pytest
python -m pytest -v -s .\testCases -m "sanity"

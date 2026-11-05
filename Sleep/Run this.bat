@echo off
cd /d "%~dp0"

python -m pip install -r requirements.txt --quiet
python gbye2.py
python gbye.py

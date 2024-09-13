@echo off
cd /d "C:\Experiment Tool"       
python -m venv .venv
call .\.venv\Scripts\activate          
pip install -r requirements.txt
python Main.py
deactivate                           
pause

@echo off

:: Create the main project folder
mkdir basic_framework

:: Create the framework folder and its files
mkdir basic_framework\framework
echo. > basic_framework\framework\__init__.py
echo. > basic_framework\framework\routing.py
echo. > basic_framework\framework\templates.py
echo. > basic_framework\framework\static.py
echo. > basic_framework\framework\security.py
echo. > basic_framework\framework\session.py
echo. > basic_framework\framework\request.py

:: Create the templates folder and index.html file
mkdir basic_framework\templates
echo. > basic_framework\templates\index.html

:: Create the static folder and style.css file
mkdir basic_framework\static
echo. > basic_framework\static\style.css

:: Create the requirements.txt file
echo. > basic_framework\requirements.txt

:: Confirmation message
echo Directory structure and files created successfully!
pause

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')  #this will generate logging info and format as the current time of executing the code with the message you want to put


project_name = "cknClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src{project_name}/__init__.py",
    f"src{project_name}/components/__init__.py",
    f"src{project_name}/utils/__init__.py",
    f"src{project_name}/config/__init__.py",
    f"src{project_name}/config/configuration.py",
    f"src{project_name}/pipeline/__init__.py",
    f"src{project_name}/entity/__init__.py",
    f"src{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "parameters.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    
]


for filepath in list_of_files:   #this loop is for handling path issues mainly here is slash
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":  #this if statement is for creating file directories
        os.makedirs(filedir, exist_ok=True)  #if exist_ok=True it won't create again as it is already present
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
        
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):    
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
            
    else:
        logging.info(f"{filename} is existing")
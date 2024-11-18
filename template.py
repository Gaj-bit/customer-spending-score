import os
from pathlib import Path

project_name = "customer_spending_score"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/main.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/data/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/tools.py",
    f"src/{project_name}/utils/metrics.py",
    f"src/{project_name}/pipline/__init__.py",
    f"src/{project_name}/pipline/training_pipline.py",
    f"src/{project_name}/pipline/predicting_pipline.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/exception/__init__.py",
    "setup.py",
    f"config",
    f"notebooks/EDA.ipynb",
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
  
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass

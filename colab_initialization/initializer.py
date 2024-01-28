import os
import wrds
from google.colab import drive

def initialize_colab(capstone_project_path = '/content/drive/MyDrive/capstone/'):

    drive.mount('/content/drive', force_remount=True)

    if not os.path.exists(capstone_project_path):

        os.mkdir(capstone_project_path)
        print(f"""Top level project directory 'capstone' has been created on Google drive.
        This directory will be used to store and access data and code for use in this project.
        It is accessible at the following path via Colab: {capstone_project_path}
        """)
    else:
        print(f"""Top level project directory 'capstone' already exists on Google drive.
        This directory will be used to store and access data and code for use in this project.
        It is accessible at the following path via Colab: {capstone_project_path}
        """)

    os.chdir(capstone_project_path)
    print(f"""Current working directory is now the top-level capstone project directory. 
    It is located in the mounted Google Drive and accessible at the following 
    path via Colab: {capstone_project_path}
    """)

    print("""Connecting to WRDS.""")
    
    db = wrds.Connection(wrds_username='thowley3')
    db.create_pgpass_file()
    
    print(f"""Colab successfully initialized.""")
    return None

def initialize_wrds_connection():
    print("""Initializing connection to WRDS.""")
    
    db = wrds.Connection(wrds_username='thowley3')
    db.create_pgpass_file()

    print("""WRDS connection successfully initialized.""")

    return db

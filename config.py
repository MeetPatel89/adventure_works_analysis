import os 
from dotenv import load_dotenv

# load the .env file
load_dotenv()

# get root directory based on location of config.py
def func_get_root_dir():
    return os.path.abspath(os.curdir)
ROOT_DIR = func_get_root_dir()

SQL_USER=os.getenv("SQL_USER")
SQL_PWD=os.getenv("SQL_PWD")
SQL_SERVER=os.getenv("SQL_SERVER")
SQL_DRIVER=os.getenv("SQL_DRIVER")
SQL_DB=os.getenv("SQL_DB")
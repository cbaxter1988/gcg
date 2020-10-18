import os
from distutils.util import strtobool

APP_PORT = os.getenv("APP_PORT", 5000)
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
DB_HOST = os.getenv("DB_HOST", "192.168.1.182")
DB_PORT = os.getenv("DB_PORT", 27017)
DB = os.getenv("DB", "LCG_API")
DEBUG = strtobool(os.getenv("DEBUG", "false"))

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

TEMPLATE_FOLDER = os.getenv('TEMPLATE_FOLDER', 'template')

TEMP_FOLDER = os.getenv("TEMP_FOLDER", '../gcg/.tmp')
LOG_DIR = os.getenv("LOG_DIR", "/var/logs")

from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST", "undefined")
DB_PORT = os.environ.get("DB_PORT", "undefined")
DB_NAME = os.environ.get("DB_NAME", "undefined")
DB_USER = os.environ.get("DB_USER", "undefined")
DB_PASS = os.environ.get("DB_PASS", "undefined")

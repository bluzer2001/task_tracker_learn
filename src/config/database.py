__all__ = ["DB_URL"]

import os

from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_CONN_STRING")

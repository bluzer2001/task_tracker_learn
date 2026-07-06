__all__ = ["DB_URL"]

import os

from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_CONN_STRING")
DB_TEST_URL = os.getenv("DB_TEST_CONN_STRING")

import dotenv
import os

dotenv.load_dotenv()

PRODUCT=os.getenv("PRODUCT")

EMAIL_ADDRESS=os.getenv("EMAIL_ADDRESS")
EMAIL_PASS=os.getenv("EMAIL_PASS")

SMTLIB_SERVER=os.getenv("SMTLIB_SERVER")
SMTLIB_PORT=os.getenv("SMTLIB_PORT")
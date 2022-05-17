import os

BASE_DIR=os.path.dirname(__file__)
DB_PATH=os.path.join(BASE_DIR, "main.db")
SQLALCHEMY_DATABASE_URI="sqlite:///"+DB_PATH
SQLALCHEMY_TRACK_MODIFICATIONS=False
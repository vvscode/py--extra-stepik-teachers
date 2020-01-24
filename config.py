import os

CSRF_ENABLED = True
SECRET_KEY = os.environ.get("SECRET_KEY", 'DEFAULT_SECRET_KEY')

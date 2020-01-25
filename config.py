import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "DEFAULT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(basedir, "teachers.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

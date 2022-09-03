
class Config:
    """Base config."""
    SECRET_KEY = 'vsw_sseXkAAs'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_DATABASE_URI = 'mysql://vsw:1234@localhost:3306/virtual_studio'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

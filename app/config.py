
class Config:
  DEBUG = False
  TESTING = False
  SECRET_KEY = "secret"
  SESSION_COOKIE_SECURE = True # Only send cookies if the connection is secure
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  FLASK_RUN_PORT=8000

class DevelopmentConfig(Config):
    
    # SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{dbUser}:{dbPassword}@localhost/{dbName}"
    SQLALCHEMY_DATABASE_URI = "sqlite:///news.db"
    DEBUG = True
    SESSION_COOKIE_SECURE = False 

class TestingConfig(Config):
    # SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{dbUser}:{dbPassword}@localhost/{dbName}"
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    DEBUG = True
    TESTING = True
    SESSION_COOKIE_SECURE = False 

class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{dbUser}:{dbPassword}@localhost/{dbName}"
    SQLALCHEMY_DATABASE_URI = "sqlite:///production.db"
  


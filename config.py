import os 

class BaseConfig(object):
    DEBUG = False 
    TESTING = False 
    PRODUCTION = False 

    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(
    os.environ.get("POSTGRES_USER"), 
    os.environ.get("POSTGRES_PASSWORD"), 
    os.environ.get("POSTGRES_SERVER"), 
    os.environ.get("POSTGRES_PORT"), 
    os.environ.get("POSTGRES_DATABASE")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    PRODUCTION = True 
    HOST = os.environ.get("HOST")
    PORT = os.environ.get("PORT")
    SECRET_KEY = os.environ.get("SECRET_KEY")

class DevelopmentConfig(BaseConfig):
    DEVELOPTMENT = True
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = "8080"
    SECRET_KEY = "zjphgoufhsojgqfowrgwntwr24qfjaqnfoqjr214"
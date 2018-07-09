db_uri ='postgres://papaya:greenpink@project-papaya.cab8do2hlpay.us-east-1.rds.amazonaws.com:5432/papaya'
class BaseConfig:
    """Base configuration"""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = db_uri
class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = db_uri
class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = db_uri
class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = db_uri

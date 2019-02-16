import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    #JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'
    SQLALCHEMY_DATABASE_URI = 'postgres://interview:uo4uu3AeF3@candidate.suade.org/suade'

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgres://interview:uo4uu3AeF3@candidate.suade.org/suade'
    #JWT_SECRET_KEY = hhgaghhgsdhdhdd

class Testing(object):
    """
    Testing environment configurations
    """
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgres://interview:uo4uu3AeF3@candidate.suade.org/suade'
    #JWT_SECRET_KEY = hhgaghhgsdhdhdd

app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
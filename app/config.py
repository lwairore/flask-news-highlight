class Config:
    """
    Config class will contain all(general) configurations/optimization
    that will will be used in Development stage and Production class.
    """
    pass


class ProdConfig(Config):
    """
    
    This sub-class will also contain all the other configurations to
    facilitate the production class. 
    Args:
        Config: This sub-class will inherit all configurations from Config, base class.
    """
    pass


class DevConfig(Config):
    """
    Sub-class contains all configurations that will facilate the development stage.
    
    Args:
        Config: Sub-class also inherits all the configurations from Config, base-class.        
    """
    # To enable debug mode.
    DEBUG = True

    
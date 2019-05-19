class Config:
    """
    Config class will contain all(general) configurations/optimization
    that will will be used in Development stage and Production class.
    """
    pass


class ProdConfig(Config):
    """
    This sub-class will inherit all configurations from Config, base class.
    This sub-class will also contain all the other configurations to
    facilitate the production class. 
    """
    pass
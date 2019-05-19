class Sources:
    """
    This class helps to design all its instance to have:
        1. id
        2. name
        3. url
        4. country
        5. description
    """
    def __init__(self, id, name, url, country, description):
        """
        This method allows us to instantiate an instance.
        """
        self.id = id
        self.name = name
        self.url = url
        self.country = country
        self.description = description
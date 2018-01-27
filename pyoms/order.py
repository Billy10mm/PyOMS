from pyoms import config

class Order:

    """This class creates a single order"""

    id = 0
    PROPERTIES = ['symbol', 'side', 'quantity', 'price', 'destination']

    def __init__(self):
        self.myConfig = config.Config().get_config_section(self.__class__.__name__)
        [setattr(self, property, None) for property in self.PROPERTIES]
        self.__class__.id += 1
        self.id = self.__class__.id

    def set_property(self, property, value):
        """Allows you to set any single property of the order"""
        setattr(self, property, value)

    def set_properties_dict(self, property_dict):
        """Provided a dictionary, assigns all key/value pairs as properties/values of the order"""
        [setattr(self, property, property_dict[property]) for property in property_dict]

    def get_property(self, property):
        """Returns a single property of the order"""
        return getattr(self, property)

    def get_properties_dict(self):
        """Returns all properties/values of the order in a dictionary"""
        return vars(self)

class CellPhone:
    def __init__(self, manufact, model, price):
        
        self.__manufact=manufact
        self.__model= model
        self.__price=price
    def set_manufact(self, manufact):
        self.__manufact==manufact
    def set_model(self, model):
        self.__model==model
    def set_retail_price(self, price):
        self.__price==price
    # The get_manufact method returns the
    # phone's manufacturer.
    def get_manufact(self):
        return self.__manufact
# The get_model method returns the
# phone's model number.
    def get_model(self):
        return self.__model
# The get_retail_price method returns the
# phone's retail price.
    def get_retail_price(self):
        return self.__price
    
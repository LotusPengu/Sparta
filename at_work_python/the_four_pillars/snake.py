from reptile import Reptile


class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self._cold_blooded = True    # example of shadowing, can write attributes that are already in prev. classes, _ adds protected access
        self.__venom = None           # None is its own type ('NoneType'), __ adds private access

    @property           # Adds another layer of protection, a getter
    def cold_blooded(self):
        return self._cold_blooded

    @cold_blooded.setter        # Allows us to set exactly how the data will be modified
    def cold_blooded(self, value):
        self._cold_blooded = value


""" underscore provides a layer of encapsulation to reduce the chance of data being changed unwillingly """

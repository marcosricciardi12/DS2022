import abc

class AbstractShapeFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_shape(self, name):
        pass
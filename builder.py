from abc import ABC, abstractmethod


class AbstractHomeBuilder(ABC):
    """
        Interface for builders
    """
    pass

    @property
    @abstractmethod
    def home(self):
        """
            Property for Product
        """
        pass

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_garage(self):
        pass


class ConcreteHomeBuilder(AbstractHomeBuilder):
    def __init__(self):
        self._home = None
        self.reset()

    @property
    def home(self):
        """
        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        home = self._home

        self.reset()

        return home

    def reset(self):
        self._home = Home1()

    def build_walls(self):
        self._home.add_part('Walls')

    def build_doors(self):
        self._home.add_part('Doors')

    def build_windows(self):
        self._home.add_part('Windows')

    def build_garage(self):
        self._home.add_part('Garage')


class Home1:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def show_parts(self):
        """
        'Get result' method
        """
        print(f"Home parts: {', '.join(self.parts)}")

        return self.parts


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: AbstractHomeBuilder):
        self._builder = builder

    def build_min_house(self):
        self._builder.build_walls()
        self._builder.build_doors()
        self._builder.build_windows()

    def build_big_house(self):
        self._builder.build_walls()
        self._builder.build_doors()
        self._builder.build_windows()
        self._builder.build_garage()


def client_code():
    director = Director()
    builder = ConcreteHomeBuilder()
    director.builder = builder

    print('Minimal house:')
    director.build_min_house()
    builder.home.show_parts()

    print('Big house:')
    director.build_big_house()
    builder.home.show_parts()

    # build house without director
    print('Custom house built without director')
    builder.build_walls()
    builder.build_doors()
    builder.home.show_parts()


if __name__ == '__main__':
    client_code()

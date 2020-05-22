from abc import ABC, abstractmethod
import random


class Product(ABC):
    """
        Interface of the Product
    """

    @abstractmethod
    def work(self):
        pass


class ConcreteProduct1(Product):
    name = 'Product 1'

    def work(self):
        print(f'Do something for {self.name}')


class ConcreteProduct2(Product):
    name = 'Product 2'

    def work(self):
        print(f'Do something for {self.name}')


class Creator(ABC):
    """
        Interface of the factory
    """

    @abstractmethod
    def factory_method(self):
        pass

    def create_product(self) -> Product:
        """
            It's an optional method. The implementation can be in `factory_method`.
            There can be additional logic here
        """
        product = self.factory_method()

        print(f'{product.name} is created')

        return product


class ConcreteCreator1(Creator):
    def factory_method(self) -> ConcreteProduct1:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> ConcreteProduct2:
        return ConcreteProduct2()


def client_code(creator: Creator):
    """
        Function to work with an concrete instance of Creator
    """
    print(f'Client gets creator {type(creator).__name__}')

    product = creator.create_product()
    product.work()


if __name__ == '__main__':
    if random.random() < 0.5:
        client_code(ConcreteCreator1())
    else:
        client_code(ConcreteCreator2())



class Target:
    """
    This class defines interface used by the client code
    """

    def __init__(self):
        self.diameter = 10

    def circumference(self) -> float:
        return self.diameter * 3.14


class Service:
    """
    The Service contains some useful behavior needed by the client code
    """

    def __init__(self):
        self.radius = 5

    def useful_logic(self):
        pass


class Adapter(Target, Service):
    def __init__(self):
        Service.__init__(self)

    def circumference(self) -> float:
        return 2 * self.radius * 3.14


class Adapter2:
    def __init__(self, s: Service):
        self.service = s

    def circumference(self) -> float:
        return 2 * self.service.radius * 3.14


if __name__ == '__main__':
    target = Target()
    adapter = Adapter()

    service = Service()
    adapter2 = Adapter2(service)

    print(target.circumference())
    print(adapter.circumference())
    print(adapter2.circumference())


class Foo:
    def __init__(self, y=None):
        self._x = y

    @property
    def x(self):
        return self._x or 0

    #temos que tratar como propriedade.
    @x.setter
    def x(self, value):
        self._x += value

foo = Foo(10)
print(foo.x)
#foo.x = 10
#print(foo.x)

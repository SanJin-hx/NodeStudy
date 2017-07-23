_author_ = 'SanJin'
class Hello:
    def __init__(self,name):
        self._name = name
    def sayHello(self):
        print("Hello {0}".format(self._name))

class Hi(Hello):
    def __init__(self,name):
        Hello.__init__(self,name)
    def sayHi(self):
        print("Hi {0}".format(self._name))

h = Hello("love styudy")
h.sayHello()

h1 = Hi("lisi")
h1.sayHi()
class Larry:

    def __init__(self):
        self.name = 'larry'
        self.age = 100
        self.family = 'wall'

    def getter(self):

        name = self.name
        age = self.age
        return [name, age]
    def setter(self, name, age):
        self.name = name
        self.age = age




obj = Larry()
obj.setter('wall', 100)
print(obj.getter())
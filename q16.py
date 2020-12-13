# imagine you are creating a Super Mario game. You need to define a class to represent Mario. What would it look like? If you aren't familiar with SuperMario, use your own favorite video or board game to model a player.

class Model:
    def __init__(self, name, health, level):
        self.name = name 
        self.health = health
        self.level = level

    def getProfile(self):
        return f'Name: {self.name}   Health: {self.health}   Level: {self.level}'

m = Model('Mario', '98%', 'Novice')
print(m.getProfile())
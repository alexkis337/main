poke_types = {
    'fire':  {
        'fire': 0.5,
        'water': 0.5,
        'grass': 2,
    },
    'water': {
        'fire': 2,
        'water': 0.5,
        'grass': 0.5
    },
    'grass': {
        'fire': 0.5,
        'water': 2,
        'grass': 1
    },
}
class Pokemon:
    def __init__(self, name, type, level, max_health, current_health, ko_status):
        self.name = name
        self.type = type
        self.level = level
        self.max_health = max_health
        self.current_health = current_health
        self.ko_status = ko_status

        if self.type in ['fire', 'water', 'grass']:
            pass
        else:
            print('Please change the type')

    def __repr__(self):
        return f"""
    Pokemon: {self.name}
    Type: {self.type}
    Level: {self.level}
    Current HP: {self.current_health}
    """

    def lose_health(self, amount):
        self.current_health -= amount
        print(f"After receiving damage {self.name} has {self.current_health} HP")
        self.ko()
        return self.current_health

    def gain_health(self, amount):
        self.current_health += amount
        print(f"After receiving healing {self.name} has {self.current_health} HP")
        return self.current_health

    def ko(self):
        if self.current_health == 0:
            self.ko_status = True
            print(f"{self.name} is knocked out")
            return True
        else:
            print(f"{self.name} is conscious")
            return False

    def attack(self, def_pokemon):
        damage = self.level * poke_types[self.type][def_pokemon.type]
        print(f'{self.name} attacked {def_pokemon.name} with {damage} damage')
        if poke_types[self.type][def_pokemon.type] == 2:
            print('It\'s supper effective')
        if poke_types[self.type][def_pokemon.type] == 0.5:
            print('It\'s not very effective')
        if poke_types[self.type][def_pokemon.type] == 0:
            print('Attack has no effect')
        def_pokemon.lose_health(damage)



charmander = Pokemon('Charmander', 'fire', 13, 100, 100, False)
print(charmander)

squirtle = Pokemon('Squirtle', 'water', 12, 100, 100, False)
print(squirtle)

squirtle.attack(charmander)

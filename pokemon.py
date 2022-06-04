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

potion_list = {
    's_potion': 10,
    'm_potion': 25,
    'b_potion': 50,
    'sup_potion': 100,
    'revival_potion': True
}

class Pokemon:
    def __init__(self, name, type, level, max_health, current_health, ko_status = False):
        self.name = name
        self.type = type
        self.level = level
        self.max_health = max_health
        self.current_health = current_health
        self.ko_status = ko_status

        if self.type in ['fire', 'water', 'grass']:
            pass
        else:
            self.name = None
            self.type = None
            self.level = None
            self.max_health = None
            self.current_health = None
            self.ko_status = None

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
        if self.current_health > self.max_health:
            self.current_health = self.max_health
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


class Trainer:
    def __init__(self, name, current_poke, pokemons = [], potions = []):
        self.name = name
        self.current_poke = pokemons[0]
        self.pokemons = pokemons
        self.potions = potions

    def __repr__(self):
        return f"""
    Trainer: {self.name}
    Current Pokemon: {self.current_poke}
    Available pokemons: {self.pokemons[1:]}
    Potions: {self.potions}
    """

    def use_potion(self, potion):
        self.current_poke.gain_health(potion_list[potion])
        self.potions[potion] -= 1

    def swap(self, poke_to_swap):
        if poke_to_swap not in self.pokemons:
            print("Pokemon is not available")
        if self.current_poke == poke_to_swap:
            print("Pokemon is already on battlefield")
        else:
            self.current_poke = poke_to_swap
            print(f"{poke_to_swap.name} is coming to the battlefield")


 #   def use_potion(self, potion):
 #       self.current_poke.current_health += potion_list[potion]
 #       self.potions[potion] -= 1


charmander = Pokemon('Charmander', 'fire', 13, 100, 100)
print(charmander)

squirtle = Pokemon('Squirtle', 'water', 12, 100, 100)
print(squirtle)

Ash = Trainer('Ash', 'Charmander', [charmander, squirtle], {'s_potion': 2, 'm_potion': 3})


print(Ash.current_poke.current_health)
squirtle.attack(charmander)
print(Ash.current_poke.current_health)
#print(type(potion_list['s_potion']))
print(Ash.potions)
Ash.use_potion('m_potion')
print(Ash.current_poke.current_health)
print(Ash.potions)
print(Ash.current_poke)
Ash.swap(squirtle)
print(Ash.current_poke)
Ash.swap(squirtle)

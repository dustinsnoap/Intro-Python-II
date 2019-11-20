# Write a class to hold player information, e.g. what room they are in
# currently.
import random

class Item:
    def __init__(self, name, attributes, description, equipped=None):
        self.name = name
        self.description = description
        self.equipped = equipped
        self.attributes = {
            'weight': 1,
            'damage': 0,
            'range': 0,
            'defense': 0,
        }
        for attribute in attributes:
            if attribute in self.attributes:
                self.attributes[attribute] = attributes[attribute]
        
    def __repr__(self):
        return f'{self.name}: attributes: {self.attributes} equippable: {self.equipped}'
    def get_name(self):
        return self.name
    def get_attributes(self):
        return self.attributes
    def get_equippable(self):
        return self.equipped
    def equippable(self):
        if self.equipped != None:
            return True
        return False
class Player:
    def __init__(self, name, attributes, x=0, y=0, z=1):
        self.name = name
        self.location = [x, y, z]
        self.equipped = {
            'head': None,
            'torso': None,
            'left_hand': None,
            'right_hand': None,
            'legs': None,
            'feet': None,
        }
        self.items = []
        self.attributes = {
            'strength': 10,
            'constitution': 10,
            'defense': 10,
            'dexterity': 10,
            'intelligence': 10,
            'charisma': 10,
            'wisdom': 10,
            'perception': 10,
            'luck': 10,
            'hunger': 10,
            'hitpoints': 10,
        }
        for attribute in attributes:
            if attribute in self.attributes:
                self.attributes[attribute] = attributes[attribute]

    def add_item(self, item):
        self.items.append(item)
        return self.items
    def equip_item(self, item_name):
        for item in self.items:
            if item.get_name() == item_name:
                if item.equippable():
                    if self.equipped[item.get_equippable()] != None:
                        current_item = self.equipped[item.get_equippable()]
                        self.items.append(current_item)
                    self.equipped[item.get_equippable()] = item
                    self.items.remove(item)

    def get_name(self):
        return self.name
    def get_location(self):
        return self.location
    def get_items(self):
        self.items
        return self.items
    def get_equipped(self, bodypart = None):
        if bodypart == None:
            return self.equipped
        else:
            return self.equipped[bodypart]
    def get_attr(self, name_of_attr):
        return self.attributes[name_of_attr]
    def get_attrs(self):
        return self.attributes

    def walk(self, direction):
        direction = direction.lower()
        if direction == 'north' or direction == 'n':
            self.location[1] += 1
        elif direction == 'east' or direction == 'e':
            self.location[0] += 1
        elif direction == 'south' or direction == 's':
            self.location[1] -= 1
        elif direction == 'west' or direction == 'w':
            self.location[0] -= 1
        elif direction == 'up' or direction == 'u':
            self.location[2] += 1
        elif direction == 'down' or direction == 'd':
            self.location[2] -= 1
        return self.location

    def take_damage(self, amt):
        self.attributes['hitpoints'] = max(0, self.attributes['hitpoints'] - amt)

    def attack(self, victim):
        #check if victim is alive
        if victim.get_attr('hitpoints') == 0:
            print(f"You poke {victim.get_name()} with a stick. Yup, it's dead.")
        else:
            weapon = self.equipped['left_hand']
            #figure out max damage
            damage = 1
            if weapon != None:
                x = list(map(int, weapon.get_attributes()['damage'].split('d')))
                for i in range(x[0]):
                    damage += random.randint(0, x[1])
            #subtract victim defense
            damage = max(1, damage - victim.get_attr('defense'))
            #figure out if it hit
            hit = False
            if random.randint(int(abs(self.attributes['dexterity'] / victim.get_attr('dexterity') - .5)), 100) > 50:
                hit = True
            #print result
            if hit:
                victim.take_damage(damage)
                print(f'You attacked {victim.get_name()} for {damage} hitpoints.')
            else:
                print(f'You missed!')
            #check if victim died
            if victim.get_attr('hitpoints') == 0:
                print(f'You killed {victim.get_name()}!')


my_stats = {
    "strength": 42,
    "constitution": 100
}
stick_attrs = {
    'weight': 1,
    'damage': '2d1',
    'range': 1
}
stick = Item('stick', stick_attrs, f"It's a stick.", 'left_hand')
stick2 = Item('stick2', stick_attrs, f"It's a stick.", 'left_hand')
stick3 = Item('stick3', stick_attrs, f"It's a stick.", 'left_hand')

me = Player('bob', my_stats)
me.add_item(stick)
me.add_item(stick2)
me.add_item(stick3)
me.equip_item('stick')
# me.equip_item('stick2')

victim = Player('bob', {})
# print('equipped:', me.get_equipped('left_hand'))
# print('items:', me.get_items())
# print(me.get_attrs())

me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
me.attack(victim)
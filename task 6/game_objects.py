import random


class Location:
    def __init__(self,name,description = None) -> None:
        self.name = name
        self.description=description
        self.monsters=None
        self.npcs = None
        self.locations=[]

    def upon_entrance(self):
        print(f'You entered [{self.name}]')
        if self.description is not None:
            print(self.description)

    def go_to(self):
        print('From here you can go to:')
        for i, el in enumerate(self.locations):
            print(i+1, '. ', el.name, sep='')
        print(f'Where do you want to go? 1-{i+1}')
        ans = input('> ')
        try:
            ans = int(ans)
            loc = self.locations[ans-1]
            print(f'You chose to go to {loc.name}')
            return loc
        except ValueError:
            print('Your answer must be the number of the location, silly')
        except IndexError:
            print('Something wrong with your number')

class Dungeon(Location):
    def __init__(self, name, description=None) -> None:
        super().__init__(name, description)
    def set_monsters(self, monsters):
        self.monsters=monsters
    def upon_entrance(self):
        super().upon_entrance()
        if self.monsters == []:
            print ('The dungeon is already cleaned')
            return None
        print('Careful, the dungeon is filled with monsters')
        print('Here you can see:')
        for i, el in enumerate(self.monsters):
            print(i+1, '. ', el.name, sep='')
        print(f'Which one will you fight first? 1-{i+1}')
        ans = input('> ')
        try:
            ans = int(ans)
            monster = self.monsters[ans-1]
            print(f'You chose to fight {monster.name}')
            return monster
        except ValueError:
            print('Your answer must be the number of the monster, silly')
        except IndexError:
            print('Something wrong with your number')

class Coridor(Location):
    def __init__(self, name, description=None) -> None:
        super().__init__(name, description)
    def set_link(self, locations):
        self.locations = locations
        for loc in locations:
            loc.locations.append(self)

class Room(Location):
    def __init__(self, name, description=None) -> None:
        super().__init__(name, description)
        self.item = None
        self.npc = None
    def set_npc(self, npc):
        self.npc = npc
    def upon_entrance(self):
        super().upon_entrance()
        if self.npc is not None:
            self.npc.approach()
            print('Do you want to interact with him? y/n')
            ans = input('> ')
            if ans== 'y':
                return self.npc
        if self.item is not None:
            print(f'You found {self.item.name} here. Do you want to take it? y/n')
            if ans== 'y':
                return self.item
    def set_item(self, item):
        self.item = item

class Item:
    def __init__(self, name) -> None:
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage) -> None:
        super().__init__(name)
        self.type = 'Weapons'
        self.damage = damage


class Potion(Item):
    def __init__(self, name, heal) -> None:
        super().__init__(name)
        self.type = 'Potions'
        self.heal = heal
    def use(self):
        return self.health


class Armor(Item):
    def __init__(self, name, protection) -> None:
        super().__init__(name)
        self.protection = protection
        self.type = 'Armor'
    def use(self):
        return self.protection


class MainCharacter:

    def __init__(self, name) -> None:
        self.name=name
        self.inventory={'Weapons':[], 'Potions':[], 'Armor':[]}
        self.health = 1000
        self.money = 50
        self.damage = 5
        self.protection = 0

    def take_item(self, objec:Item):
        self.inventory[objec.type].append(objec)

    def take_damage(self, damage:int)->bool:
        damage = int(damage*(1-self.protection/100))
        self.health -= damage
        if self.health>0:
            print(f'You were damaged by {damage} points. Your health: {self.health}')
            return True
        print('YOU DIED.')
        return False

    def restore_health(self, health:int):
        self.health+=health
        if self.health>=1000:
            print('your health is fully restored!')
            self.health = 1000
        print(f'Healing was succesful! Your health is {self.health}')

    def buy(self, trade_res):
        if self.money-trade_res[1]>=0:
            self.money-=trade_res[1]
            print(f'You succesfully bought a {trade_res[0].name}! You have {self.money} coins left')
            self.take_item(trade_res[0])
        else:
            print(f'You cannot buy that. Your {self.money} coins is not enough :(')

    def earn(self, coins):
        self.money += coins

    def change_armor(self):
        if self.inventory['Armor'] != []:
            print('You have these armors:')
            for i, el in enumerate(self.inventory['Armor']):
                print(i+1, '. ', el.name, sep='')
            print(f'Which one you choose? 1-{i+1}')
            ans = input('> ')
            try:
                ans = int(ans)
                new_armor = self.inventory['Armor'][ans-1]
                print(f'You wore {new_armor.name}. Now your protection is {new_armor.protection}')
                self.protection = new_armor.protection
            except ValueError:
                print('Your answer must be the number of the armor, silly')
            except IndexError:
                print('Something wrong with your number')

    def change_weapon(self):
        if self.inventory['Weapons'] != []:
            print('You have these weapons:')
            for i, el in enumerate(self.inventory['Weapons']):
                print(i+1, '. ', el.name, sep='')
            print(f'Which one you choose? 1-{i+1}')
            ans = input('> ')
            try:
                ans = int(ans)
                new_armor = self.inventory['Weapons'][ans-1]
                print(f'You chose {new_armor.name}. Now your attack is {new_armor.damage}')
                self.protection = new_armor.protection
            except ValueError:
                print('Your answer must be the number of the weapon, silly')
            except IndexError:
                print('Something wrong with your number')
    
    def attac(self):
        span1 = int(self.damage*0.95)
        span2 = int(self.damage*1.05)
        damage = random.randint(span1, span2)
        print(f'You attackad! You dealt {damage} hp!')
        return damage


class Enemy:

    def __init__(self, name, hp:int, killing:int, drop=None) -> None:
        self.name = name
        self.health = hp
        self.drop = drop
        self.reward = killing

    def take_damage(self, damage:int)->bool:
        self.health -= damage
        if self.health>0:
            print(f'You damaged {damage} hp. {self.name} health: {self.health}')
            return False
        print('Congratulations! You succefuly defeated {self.name}.')
        return self.reward, self.drop

    def attac(self, avg_damage:int):
        span1 = int(avg_damage*0.95)
        span2 = int(avg_damage*1.05)
        damage = random.randint(span1, span2)
        print(f'{self.name} attacks! He deals {damage} hp!')
        return damage


class FinalBoss(Enemy):

    def __init__(self, name, hp: int, killing: int, drop=None) -> None:
        super().__init__(name, hp, killing, drop)

    def restore(self):
        self.health+=10000

    def deceit(self):
        print('I am so sorry for everything I\'ve done...')
        ans = input('> ')
        print('I promise to be good in the future...')
        ans = input('> ')
        while True:
            print('Can you please spare me? y/n')
            ans = input('> ')
            if ans == 'y':
                self.restore()
                print('Hahahhahahhah, I fooled you! I will never change!')
                self.attac(500)
                return True
            elif ans == 'no':
                print('Well... godbye... ')
                print('You have successfully defeated the final boss!')
                return False
            else:
                print('I don\'t undersatnd you...')


class NPC:

    def __init__(self, name, phrase) -> None:
        self.name = name
        self.phrase = phrase
        self.trade_obj = None

    def approach(self):
        print(f'You encountered a {self.name}!')
        print(f'{self.name} says: {self.phrase}')

    def set_trade_object(self, obj, price):
        self.trade_obj = (obj, price)

    def trade(self):
        if self.trade_obj is None:
            print('I don\'t sale anything!')
            return None
        print(f'The {self.name} sells {self.trade_obj[0].name} for {self.trade_obj[1]}. Do you want to buy it? y/n')
        ans = input('> ')
        if ans=='y':
            return self.trade_obj
        else:
            print('Ok.')
            return None

import random
import sys


class MainCharacter:

    def __init__(self) -> None:
        self.inventory={'Weapons':[], 'Potions':[], 'Armor':[]}
        self.health = 1000
        self.money = 50
        self.damage = 5
        self.weapon = None
        self.armor=None
        self.protection = 0
        self.location = None

    def take_item(self, objec):
        print(f'You got {objec.name} - {objec.description}')
        self.inventory[objec.type].append(objec)

    def take_damage(self, damage:int)->bool:
        damage = int(damage*(1-self.protection/100))
        self.health -= damage
        if self.health>0:
            if self.armor is not None:
                if self.armor.durability>1:
                    self.armor.durability -= 1
                elif self.armor.durability == 1:
                    print(f'Your {self.armor.name} broke(')
                    self.inventory["Armor"].remove(self.armor)
                    self.armor = None
                    self.protection = 0
            print(f'You were damaged by {damage} points. Your health: {self.health}')
            return False
        print('YOU DIED.')
        return True
    
    def use_potion(self):
        if self.inventory['Potions'] != []:
            print('You have these potions:')
            for i, el in enumerate(self.inventory['Potions']):
                print(i+1, '. ', el.name, f' heals {el.heal} hp', sep='')
            print(f'Which one you choose? 1-{i+1}')
            ans = input('> ')
            if ans=='':
                print('You did not choose anything')
            else:
                try:
                    ans = int(ans)
                    self.restore_health(self.inventory['Potions'][ans-1].use())
                    del self.inventory['Potions'][ans-1]
                except ValueError:
                    print('Your answer must be the number of the weapon, silly')
                except IndexError:
                    print('Something wrong with your number')
        else:
            print('You have no potions')

    def restore_health(self, health:int):
        self.health+=health
        if self.health>=1000:
            print('your health is fully restored!')
            self.health = 1000
        print(f'Healing was succesful! Your health is {self.health}')

    def buy(self, trade_res):
        if self.money-trade_res[1]>=0:
            self.money-=trade_res[1]
            print(f'You have {self.money} coins left')
            self.take_item(trade_res[0])
        else:
            print(f'You cannot buy that. Your {self.money} coins is not enough :(')

    def earn(self, coins):
        print(f'You earned {coins} coins!')
        self.money += coins

    def change_armor(self):
        if self.inventory['Armor'] != []:
            if self.armor is None:
                print('Now you don\'t wear armor')
            else:
                print(f'Your current armor is {self.armor.name} - durability left: {self.armor.durability} protecton points: {self.armor.protection}')
            print('You have these armors:')
            for i, el in enumerate(self.inventory['Armor']):
                print(i+1, '. ', el.name, f' - durability left: {el.durability} protecton points: {el.protection}', sep='')
            print(f'Which one you choose? 1-{i+1}')
            ans = input('> ')
            if ans=='':
                print('You did not choose anything')
            else:
                try:
                    ans = int(ans)
                    new_armor = self.inventory['Armor'][ans-1]
                    print(f'You wore {new_armor.name}. Now your protection is {new_armor.protection}')
                    self.protection = new_armor.protection
                    self.armor = new_armor
                except ValueError:
                    print('Your answer must be the number of the armor, silly')
                except IndexError:
                    print('Something wrong with your number')
        else:
            print('You have no armors')

    def change_weapon(self):
        if self.inventory['Weapons'] != []:
            if self.weapon is None:
                print('Now you don\'t use any weapons')
            else:
                print(f'Your current weapon is {self.weapon.name} - durability left: {self.weapon.durability} damage: {self.weapon.damage}')
            print('You have these weapons:')
            for i, el in enumerate(self.inventory['Weapons']):
                print(i+1, '. ', el.name, f' - hits left: {el.durability}, damage points: {el.damage}',sep='')
            print(f'Which one you choose? 1-{i+1}')
            ans = input('> ')
            if ans=='':
                print('You did not choose anything')
            else:
                try:
                    ans = int(ans)
                    new = self.inventory['Weapons'][ans-1]
                    print(f'You chose {new.name}. Now your attack is {new.damage}')
                    self.damage = new.damage
                    self.weapon = new
                except ValueError:
                    print('Your answer must be the number of the weapon, silly')
                except IndexError:
                    print('Something wrong with your number')
        else:
            print('You have no weapons')
    
    def attac(self):
        span1 = int(self.damage*0.95)
        span2 = int(self.damage*1.05)
        damage = random.randint(span1, span2)
        if self.weapon is not None:
            if self.weapon.durability>1:
                self.weapon.durability -= 1
            elif self.weapon.durability == 1:
                print(f'Your {self.weapon.name} broke(')
                self.inventory["Weapons"].remove(self.weapon)
                self.weapon = None
                self.damage = 5
        print(f'You attacked! You dealt {damage} hp!')
        return damage
    
    def change_loc(self, loc):
        self.location = loc
        loc.upon_entrance(self)


class Location:

    def __init__(self,name,description = None) -> None:
        self.name = name
        self.description=description
        self.monsters=None
        self.npcs = None
        self.locations=[]

    def upon_entrance(self):
        print(f'You entered {self.name}')
        if self.description is not None:
            print(self.description)

    def go_to(self, me:MainCharacter):
        print('From here you can go to:')
        for i, el in enumerate(self.locations):
            print(i+1, '. ', el.name, sep='')
        print(f'Where do you want to go? 1-{len(self.locations)}')
        while True:
            ans = input('> ')
            try:
                ans = int(ans)
                loc = self.locations[ans-1]
                print(f'You chose to go to {loc.name}')
                me.change_loc(loc)
                break
            except ValueError:
                print('Your answer must be the number of the location, silly')
            except IndexError:
                print('Something wrong with your number')

class Dungeon(Location):

    def set_monsters(self, monsters):
        self.monsters=monsters

    def upon_entrance(self, me):
        super().upon_entrance()
        while True:
            if self.monsters == []:
                print('The dungeon is already cleaned')
                self.go_to(me)
                break
            else:
                print(f'Careful, there are monsters in {self.name}')
                print('Here you can see:')
                for i, el in enumerate(self.monsters):
                    print(i+1, '. ', el.name, ' - ', el.description, sep='')
                print('Do you want to fight or run? f/r')
                ans = input('> ')
                if ans == 'f':
                    print(f'Which one will you fight first? 1-{i+1}')
                    ans = input('> ')
                    try:
                        ans = int(ans)
                        monster = self.monsters[ans-1]
                        print(f'You chose to fight {monster.name}')
                        win = monster.fight(me)
                        if win:
                            self.monsters.remove(monster)
                    except ValueError:
                        print('Your answer must be the number of the monster, silly')
                    except IndexError:
                        print('Something wrong with your number')
                elif ans == 'r':
                    self.go_to(me)
                    break
                else:
                    print('answer as a man: f or r')

class Coridor(Location):
    def set_link(self, locations):
        self.locations = locations
        for loc in locations:
            loc.locations.append(self)
    def upon_entrance(self, me):
        super().upon_entrance()
        self.go_to(me)


class Room(Location):
    def __init__(self, name, description=None) -> None:
        super().__init__(name, description)
        self.item = None
        self.npc = None
    def set_npc(self, npc):
        self.npc = npc
    def upon_entrance(self, me:MainCharacter):
        super().upon_entrance()
        if self.npc is not None:
            self.npc.approach(me)
        if self.item is not None:
            print(f'You found {self.item.name} here. Do you want to take it? y/n')
            ans = input('> ')
            if ans== 'y':
                me.take_item(self.item)
                self.item=None
        self.go_to(me)
    def set_item(self, item):
        self.item = item

class Item:
    def __init__(self, name, descr) -> None:
        self.name = name
        self.description = descr


class Weapon(Item):
    def __init__(self, name, descr,damage,dur) -> None:
        super().__init__(name, descr)
        self.type = 'Weapons'
        self.damage = damage
        self.durability = dur


class Potion(Item):
    def __init__(self, name, descr, heal) -> None:
        super().__init__(name, descr)
        self.type = 'Potions'
        self.heal = heal
    def use(self):
        return self.heal


class Armor(Item):
    def __init__(self, name, descr, protection, dur) -> None:
        super().__init__(name, descr)
        self.protection = protection
        self.type = 'Armor'
        self.durability = dur
    def use(self):
        return self.protection

class Enemy:

    def __init__(self, name, descr, hp:int, dam:int, run:int, killing:int, drop=[]) -> None:
        self.name = name
        self.description = descr
        self.health = hp
        self.init_hp = hp
        self.drop = drop
        self.reward = killing
        self.avg_damage = dam
        self.run_chance = run
    
    def fight(self, me:MainCharacter):
        print('''You can heal yourself, change weapon, change armor or try to run duiring the fight.
To do that, print "heal", "weapon", "armor" or "run"
Press enter to deal the blow''')
        while True:
            ans = input('> ')
            if ans == 'heal':
                me.use_potion()
            elif ans == 'weapon':
                me.change_weapon()
            elif ans == 'armor':
                me.change_armor()
            elif ans == 'run':
                ran = random.randint(0,100)
                if ran<self.run_chance:
                    self.health=self.init_hp
                    print(f'You successfully escaped the {self.name}')
                    return False
                else:
                    print('Whoops, you did not manage to escape. Continue fighting :-)')
            elif ans == '':
                my_blow = me.attac()
                dies = self.take_damage(my_blow)
                if dies:
                    self.health=self.init_hp
                    me.earn(self.reward)
                    for item in self.drop:
                        me.take_item(item)
                    return True
                my_blow = self.attac()
                dies = me.take_damage(my_blow)
                if dies:
                    print(f'You were killed by{self.name} - {self.description}')
                    sys.exit()
            else:
                print('If you want to write something, write something smart ^.^')

    def take_damage(self, damage:int)->bool:
        self.health -= damage
        if self.health>0:
            print(f'You damaged {damage} hp. {self.name} health: {self.health}')
            return False
        print(f'Congratulations! You succefuly defeated {self.name}.')
        return True

    def attac(self):
        span1 = int(self.avg_damage*0.95)
        span2 = int(self.avg_damage*1.05)
        damage = random.randint(span1, span2)
        print(f'{self.name} attacks! He deals {damage} hp!')
        return damage


class FinalBoss(Enemy):

    def restore(self):
        self.health=3000
    
    def fight(self, me: MainCharacter):
        ded = super().fight(me)
        if ded:
            dec = self.deceit()
            if dec:
                super().fight(me)
        print('Today was totally a strange day...')
        input('> ')
        print('You stopped a zombie apocalypsis by yourself, just like that...')
        input('> ')
        print('But now, when all the city is praising you as a hero, it\'s time for you to know the truth...')
        input('> ')
        print('It is time for you to wake up')
        input('> ')
        print('THE END')

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
                self.attac()
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

    def approach(self, me:MainCharacter):
        print(f'You encountered a {self.name}!')
        print(f'{self.name} says: {self.phrase}')
        if self.trade_obj is None:
            print('This npc is here just for fun. It doesn\'t do anything. Just like you.')
        else:
            print('Do you want something from this person? y/n')
            ans = input('> ')
            if ans=='y':
                while True:
                    print(f'{self.name} sells {self.trade_obj[0].name} for {self.trade_obj[1]}. Do you want to buy it? y/n')
                    if isinstance(self.trade_obj[0].name, Weapon):
                        print(f'The weapon has {self.trade_obj[0].name.damage} damage and {self.trade_obj[0].name.durability} durability')
                    elif isinstance(self.trade_obj[0].name, Armor):
                        print(f'The armor has {self.trade_obj[0].name.protection} protection and {self.trade_obj[0].name.durability} durability')
                    if isinstance(self.trade_obj[0].name, Potion):
                        print(f'The potion heals {self.trade_obj[0].name.heal} hp')
                    print(f'(you have {me.money} coins)')
                    ans = input('> ')
                    if ans=='y':
                        print('Here you are!')
                        me.buy(self.trade_obj)
                        print('Do you want to go somewhere else now? y/n')
                        ans = input('> ')
                        if ans == 'y':
                            break
                    elif ans == 'n':
                        print('See you next time!')
                        break
                    else:
                        print('A strange answer, try again')

    def set_trade_object(self, obj, price):
        self.trade_obj = (obj, price)

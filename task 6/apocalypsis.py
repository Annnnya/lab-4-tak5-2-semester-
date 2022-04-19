from turtle import st
from game_objects import *

def main():
    print("""
One morning you woke up to the sound of the sirens.
You were confused why they were testing them so early, but suddenly your mom called.
She said: son, you won\'t believe me, but thouthands of monsters flooded the streets of our city.
Zombie apocalypsis began!

I laughed and hang up.
Firs april - the day of fools!
As if I woud belive her.
    """)
    my_room = Room('Your own room', "The room where you live")
    me = MainCharacter()

    broom = Weapon('Broom', "The broom like the one which you use to sweep the floor in your room", 15, 8)
    broom1 = Weapon('Broom', "The broom like the one which you use to sweep the floor in your room", 15, 8)
    broom2 = Weapon('Broom', "The broom like the one which you use to sweep the floor in your room", 15, 8)
    broom3 = Weapon('Broom', "The broom like the one which you use to sweep the floor in your room", 15, 8)
    broom4 = Weapon('Broom', "The broom like the one which you use to sweep the floor in your room", 15, 8)
    broom5 = Weapon('Broom', "The broom like the one which you use to sweep the floor in your room", 15, 8)

    beer = Potion('A bottle of Teteriv', 'A deafult drink of your neighbour', 100)
    room2=Room('The room of your loud neighbour',\
"That jerk always listens to the loud music and throws parties")
    room2.set_item(beer)
    svitlytsia = Dungeon('Svitlytsia', 'The common student space in your dormitory')
    zombie = Enemy('Student zombie', 'At first you confused it with the usual students, \
but upon closer examination it turned out that they eat brains', 40, 15, 50, 20, [broom])
    zombie1 = Enemy('Student zombie', 'At first you confused it with the usual students, \
but upon closer examination it turned out that they eat brains', 60, 15, 50, 25, [broom1])
    zombie3 = Enemy('Student zombie', 'At first you confused it with the usual students, \
but upon closer examination it turned out that they eat brains', 80, 15, 50, 35, [broom2])
    zombie4 = Enemy('Student zombie', 'At first you confused it with the usual students, \
but upon closer examination it turned out that they eat brains', 50, 15, 50, 30, [broom3])
    zombie5 = Enemy('Student zombie', 'At first you confused it with the usual students, \
but upon closer examination it turned out that they eat brains', 70, 15, 50, 20, [broom4])
    zombie6 = Enemy('Student zombie', 'At first you confused it with the usual students, \
but upon closer examination it turned out that they eat brains', 80, 15, 50, 45, [broom5])

    zombie2 = Enemy('Upgraded student zombie', 'At first you confused it with usual zombies, but it was a proffessor assistant', 120, 20, 50, 60)
    svitlytsia.set_monsters([zombie])

    stairs = Coridor('Collegium staircase', 'Using elevator might be dangerous, so you decided to use stairs')
    corid1 = Coridor('Corridor to your room')
    corid1.set_link([svitlytsia, room2, my_room])
    kozl_pl = Dungeon('The firs floor of the collegium', \
'Here you can encounter Kozlovskiy - not a person you want to meet, alive or dead')
    riasa = Armor("Black cassock", "Priests wear it to pray, you wear it not to be killed", 20, 12)
    kozl = Enemy('Kozlovskiy', 'Kollegium magister', 150, 25, 20, 240, [riasa])
    musiak = Enemy('Musiakovskiy', 'A very strict curator of the second floor', 50, 30, 5, 190)
    floor2 = Dungeon('Krylo Musiakovskoho', 'Krylo on second floor')
    floor2.set_monsters([musiak])
    kozl_pl.set_monsters([kozl, zombie1])
    stairs.set_link([kozl_pl, svitlytsia, floor2])

    campus = Coridor('Campus grounds')
    cafeteria = Room('Cafeteria K2', 'You could drink coffe here before')
    sister = NPC('Smiling nun', \
'Hello, are you a collegium studet? I have never seen you at tea with us, sisiters')
    tea = Potion('Tea', 'The tea sisters drink on meetings with the students tat you never attend', 65)
    sister.set_trade_object(tea, 50)
    cafeteria.set_npc(sister)
    coffe = Potion('An unfinished coffe', 'Soneone left in on the cafeteria table', 90)
    cafeteria.set_item(coffe)
    pasta = Potion('Unfinished lunch', 'Someone left half of the pasts on his plate. It\'s already cold', 170)
    trapezna= Room('Trapezna', 'The dining hall - a fafourite place of us, students')
    trapezna.set_item(pasta)
    trapezna_worker = NPC('A girl from the paydesk', 'Did you not forget your lokal card?')
    likal = Weapon('Lokal card', 'A discount card in trapezna', 500, 1)
    trapezna_worker.set_trade_object(likal, 150)
    trapezna.set_npc(trapezna_worker)
    csh = Dungeon('Sheptytskiy Centre')
    csh.set_monsters([zombie3, zombie4, zombie2, zombie5])
    campus.set_link([kozl_pl, cafeteria, trapezna, csh])

    stryiskiy_ent = Coridor('Entrance to the stryiskiy park')
    bush = Room('Bushes on the side of the pavement')
    one_shoe = Armor('One shoe', 'You found it without a pair in some bushes. It is dirty, eww', 15, 20)
    bush.set_item(one_shoe)
    semki = Armor('A pack of semki', 'It gives you almost absolute protection for one hit', 95, 1)
    lp = Dungeon('Lower part of the park', 'This part of the park is dangerous, but it is the only way to the city centre')
    knife = Weapon('A knife', 'A usual folding knife. Gopnics use it to stab you', 60, 25)
    knife2 = Weapon('A knife', 'A usual folding knife. Gopnics use it to stab you', 85, 23)
    gop1 = Enemy('A usual gopnic', 'These were quite aggresive even before they became zombies', 90, 120, 10, 20, [knife, semki])
    gop2 = Enemy('A usual gopnic', 'These were quite aggresive even before they became zombies', 90, 120, 10, 20, [knife2, semki])
    gop3 = Enemy('A usual gopnic', 'These were quite aggresive even before they became zombies', 100, 100, 10, 30, [semki])
    lp.set_monsters([gop3, gop1, gop2])
    icecream = Room('Ice cream lot', 'Their ice cream is horrible, but you still bought it a few times before')
    seller = NPC('Ice cream seller', 'What do you want from me? (I hate my job)')
    cone = Potion('Ice cream cone', 'Looks nice, tastes like sand', 220)
    seller.set_trade_object(cone, 150)
    icecream.set_npc(seller)
    fountain = Dungeon('A great old fountain', 'You always liked how it looked')
    small_zombie = Enemy('A zombie kid', 'It is heartbreking that kids might also be zombies', 50, 10, 100, 20)
    crown = Armor('The nymph\'s crown', 'It does not suit you, but looked wonderful on you', 45, 7)
    nymph = Enemy('A nymph', 'Something like a zombie, but she looks diffent. So beautiful... And dangerous.', 120, 600, 70, 460, [crown])
    fountain.set_monsters([nymph, small_zombie, small_zombie, small_zombie])
    stryiskiy_ent.set_link([bush, lp, campus])
    road = Coridor('A long park road')
    road.set_link([fountain, icecream, stryiskiy_ent])

    road_to_center = Coridor('A road to the city center')
    st_sh = Room('Stationery shop', 'Surprisingly, there is noone here')
    notebok = Armor('A large thik notebook', "Perfect for a discrete math semester", 30, 4)
    st_sh.set_item(notebok)
    wed_sh = Dungeon('Wedding shop', 'The door of this shop was wide open, but why did you come here?')
    fata = Armor('Bridal veil', 'Veil of the dead bride', 70, 4)
    bride = Enemy('Dead bride', 'She was fitting er dress when she became zombie', 300, 75, 50, 210, [fata])
    wed_sh.set_monsters([bride, small_zombie])
    centre = Coridor('City center')
    road_to_center.set_link([lp, st_sh, wed_sh, centre])

    port = Room('Port bar', 'You often came here to drink wine with your friens')
    wine = Potion('Glass of wine', 'Yummy', 300)
    port.set_item(wine)
    mac = Room('MacDonalds')
    menu = Potion('Mac Menu', 'With the cheese souce - the food of gods', 500)
    cashier = NPC('Mac Cashier', 'Good afernoon, what is your order?')
    cashier.set_trade_object(menu, 250)
    mac.set_npc(cashier)
    tray = Armor('A tray', 'Normal people carry food on it, but you might make a better use of a tray', 60, 5)
    mac.set_item(tray)
    opera = Dungeon('Opera house', 'You hear strange loud noises from there. Maybe here is where everything ends...')
    finbos = FinalBoss('A great zombie monster', \
'You have never seen anything so terrifying and big. This enormous glowing zombie is responsible for the chaos in the city.',\
    3000, 100, 2, 0)
    opera.set_monsters([zombie6, small_zombie, small_zombie, finbos])
    centre.set_link([port, mac, opera])

    me.change_loc(my_room)

if __name__=="__main__":
    main()

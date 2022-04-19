For this game I have two modules:

1) game_objects.py with all classes for everything i need in the game
2) apocalypsis.py with where I create objects of these classes, create links between them, and launch the game

Regarding classes:

I have class for the main character, which stores all info about current state of the character and has functions to change that state.
These functions are: init, func for taking item into inventory, for taking damage (here I take into account use of armor), using potion, healing, buying items from npcs, taking money, changing armor and weapon, attacking, and the function which takes part in the process of changing the location.

Then I have general class for locations, which I don't use in main loop, but all usable locations inherit it.
Of course, it has init, whic takes name and description of the location, welcomong message after entrance, and the go_to function, which is the key to moving through locations in this game.

Location Dungeon is location where you can enconter monsters. It has set_monsters func, which takes list of monsters thst will be present at that location, and upon entrance, which is the main loop of actions on that location. Later locations also have that loop, but everywhere it's different.
Location Coridor is a location that links together all locations. It has set_link funk, which links other location to this coridor. Because of this players can move through map.
Location Room is where you can find an nps and/of an item. Most important functions are: set npc, and set item to the room.

Class Item is like Location - only used for inheritance. It takes name and description of the item.

Weapon is an item, that has additional characteristic of damage an durability. Armor has protection and durability. Potions have only the amount of ph they restore and can be only used once.

Class Enemy is a class for all monsters in the game. The init takes name, description, hp of the monster, his damage in fight, chance of running from him duiring the battle, reward for the kill in coins and optional argument - drop that you can obtain from him. It has figth function, which is the main loop of fighting process. It also has functions for attac and taking damage.
FinalBoss class inherits Enemy class, but it can deceive the main character into sparing him, after which he restores health.

NPC class is class for npcs. They can sell items. The calass has init func and func which thakes trade object and price for which npc will sell it. Approach func is the main loop for buying process.




The playing process is launched from the apocalypsis.py module. It creates a number of objets of the classes above and starts a game.


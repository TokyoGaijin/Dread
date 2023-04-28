import random

items = [None, "potion", "charm", "quick"]

def dice(sides):
    return random.randrange(1, sides + 1)


class Player():
    def __init__(self, name, start=(4, 2)):
        self.name = name
        self.pos = start
        self.health = 100
        self.pouch = []
        self.bonus = 0
        self.isAlive = True

    def move(self, newX, newY):
        self.pos = (newX, newY)

    def heal_inflict(self, points):
        self.health += points

        if self.health <= 0:
            self.isAlive = False
        if self.health >= 100:
            self.health = 100

    def add_item(self, item):
        self.pouch.append(item)

    def use_item(self, item):
        if item in self.pouch:
            if item == "potion":
                self.heal_inflict(35)
            if item == "charm":
                self.bonus = 5
            if item == "quick":
                self.bonus = 4
            self.pouch.remove(item)

    def roll_dice(self, sides):
        return dice(sides)


class Enemy():
    def __init__(self, enemy_type, room):
        self.enemy_type = enemy_type
        self.room = room
        self.health = 100
        self.drop_item = items[random.randrange(0, len(items))]
        if enemy_type == "boss":
            self.health += random.randrange(50, 101)
        elif enemy_type == "mid":
            self.health += random.randrange(1, 26)

        self.isAlive = True

    def inflict(self, points):
        self.health -= points

        if self.health <= 0:
            self.isAlive = False

    def roll_dice(self, sides):
        return dice(sides)



class Room():
    def __init__(self, xCoord, yCoord, hasPrincess = False):
        self.x = xCoord
        self.y = yCoord
        self.room_name = (self.x, self.y)
        self.enemies = []
        self.chest = []
        self.room_beaten = False
        self.hasPrincess = hasPrincess

    def load_room(self):
        creature_roll = dice(4)
        if creature_roll == 2 or creature_roll == 3:
            self.enemies.append(Enemy("random creature", (self.x, self.y)))
        elif creature_roll == 4:
            self.enemies.append(Enemy("mid", (self.x, self.y)))

        chest_roll = dice(2)
        quantity = dice(4)
        if chest_roll == 2:
            for i in range(quantity):
                self.chest.append(items[random.randrange(1, len(items))])

    def check_clear(self):
        if len(self.enemies) == 0 and len(self.chest) == 0:
            self.room_beaten = True

    def ident(self):
        return self.room_name


game_lot = [["-----",
             "-----",
             "-----",
             "-----",
             "-----"],

            ["■■-■■",
             "■-■■",
             "■-■--",
             "■■■■■",
             "--■--"]
            ]

lair = []

roomX = 0
roomY = 0

for row in game_lot[1]:
    for col in row:
        if col == "■":
            lair.append(Room(roomX, roomY))

        roomX += 1
    roomY += 1
    roomX = 0

def init():
    for rooms in lair:
        rooms.load_room()



init()
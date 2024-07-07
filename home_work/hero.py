class superhero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return f"{self.nickname} has the superpowers {self.superpower} and {self.health_points} health points"

    def __len__(self):
        return len(self.catchphrase)

hero = superhero("murdoc niccals", "2d", "fly and super speed", 100, "смех, а потом погнали")
print(hero.get_name())
hero.double_health_points()
print(hero)
print(len(hero))

def __init__(self, name, nickname, superpower, health_points, catchphrase):
    self.name = name
    self.nickname = nickname
    self.superpower = superpower
    self.health_points = health_points
    self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return f"{self.nickname} has the superpowers {self.superpower} and {self.health_points} health points"

    def __len__(self):
        return len(self.catchphrase)


class air_hero(superhero):
    area = 'sky'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health_points(self):
        super().double_health_points()  # Call superclass method
        self.fly = True

    def true_in_true_phrase(self):
        print("true in the true_phrase")


class earth_hero(superhero):
    area = 'land'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health_points(self):
        super().double_health_points()  # Call superclass method
        self.fly = True

    def true_in_true_phrase(self):
        print("true in the true_phrase")


class villain(earth_hero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, damage):
        return damage ** 2


# Testing the classes
air_hero_obj = air_hero("storm", "ororo munroe", "control weather", 50, "weather the storm", 10)
air_hero_obj.double_health_points()
air_hero_obj.true_in_true_phrase()

earth_hero_obj = earth_hero("the thing", "ben grimm", "super strength and durability", 80, "it's clobberin' time", 15)
earth_hero_obj.double_health_points()
earth_hero_obj.true_in_true_phrase()

villain_obj = villain("dr. doom", "victor von doom", "genius intellect and armor", 200, "doom shall reign!", 20)
print(villain_obj.people)
print(villain_obj.crit(20))

print(earth_hero_obj)





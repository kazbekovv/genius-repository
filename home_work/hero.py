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

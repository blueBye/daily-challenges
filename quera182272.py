class Gun:
    def __init__(self, name, range, power, bullet_size):
        self.name = name
        self.range = range
        self.power = power
        self.bullet_size = bullet_size

class Bullet:
    def __init__(self, name, bullet_size, damage) -> None:
        self.name = name
        self.bullet_size = bullet_size
        self.damage = damage

guns = [
    Gun("Submachine Gun", 100, 10, 0.5),
    Gun("Assault Rifle", 200, 20, 1),
    Gun("Pistol", 80, 8, 0.5),
    Gun("Shotgun", 50, 40, 4),
    Gun("Sniper Rifle", 1000, 30, 3)
]

bullets = [
    Bullet("A", 0.5, 1),
    Bullet("B", 1, 1.5),
    Bullet("C", 3, 3),
    Bullet("D", 4, 2),
]

class Shooter:
    def __init__(self) -> None:
        self.gun = None
        self.bullet_count = 0
        self.bullet = None

    def set_gun_by_name(self, name: str) -> None:
        if name not in [gun.name for gun in guns]:
            raise Exception()
        self.gun = [gun for gun in guns if gun.name == name][0]
        self.bullet = [bullet for bullet in bullets if bullet.bullet_size == self.gun.bullet_size][0]

    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:
        if not self.gun:
            raise Exception()
        elif size != self.gun.bullet_size:
            raise Exception()
        elif count < 0:
            raise Exception()
        elif size not in [b.bullet_size for b in bullets]:
            raise Exception()
        self.bullet_count += count

    def shoot_to_target(self, target_x: int,  target_y: int,  target_distance: int,  aim_x: int,  aim_y: int) -> float:
        if target_distance > self.gun.range:
            return 0
        elif self.bullet_count <= 0:
            raise Exception()
        elif target_x + 10 < aim_x or aim_x < target_x:
            return 0
        elif target_y + 10 < aim_y or aim_y < target_y:
            return 0
        self.bullet_count -= 1
        return self.gun.power * self.bullet.damage


# shooter = Shooter()
# shooter.set_gun_by_name('Submachine Gun')
# shooter.add_bullet_of_given_size_to_gun(0.5, 1)
# result = shooter.shoot_to_target(1, 1, 20, 5, 4)
# result = shooter.shoot_to_target(1, 1, 20, 5, 4)
# print(result)
class Fire:
    title = "fire"

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Ground):
            return Burned_ground()


class Water:
    title = 'water'

    def __add__(self, other):
        if isinstance(other, Ground):
            return Dirt()

    def __radd__(self, other):
        return self + other

    def __str__(self):
        return self.title


class Air:
    title = 'air'

    def __str__(self):
        return self.title


class Ground:
    title = 'ground'

    def __str__(self):
        return self.title


class Steam:
    title = "steam"

    def __str__(self):
        return self.title


class Dirt():
    title = 'dirt'

    def __str__(self):
        return self.title

    def __sub__(self, other):
        if isinstance(other, Ground):
            return self - other


class Burned_ground():
    title = "сожженая земля"

    def __str__(self):
        return self.title


elements = {"огонь": Fire(), "вода": Water(), "земля": Ground(), "воздух": Air()}
while True:
    for i in elements:
        print(i)
    try:
        first_elm = elements[input("выберите первый элемент")]
        second_elm = elements[input("выберите второй элемент")]
        print(f"вы получили:{first_elm + second_elm}")
    except:
        print("такого элемента нет в словаре")
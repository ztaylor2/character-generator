"""A character generator."""


class Character(object):
    """A character."""

    def __init__(self):
        """Init character."""
        self.magica = 0
        self.destruction = 0
        self.alteration = 0
        self.health = 0
        self.handtohand = 0
        self.shield = 0
        self.sword = 0
        self.bow = 0

        self.gender = None
        self.eye_color = None
        self.hair_color = None
        self.height = None

        self.attributes = [
            (self.magica, 'magica'),
            (self.destruction, 'destruction'),
            (self.alteration, 'alteration'),
            (self.health, 'health'),
            (self.handtohand, 'handtohand'),
            (self.shield, 'shield'),
            (self.sword, 'sword'),
            (self.bow, 'bow'),
            (self.gender, 'gender'),
            (self.eye_color, 'eye_color'),
            (self.hair_color, 'hair_color'),
            (self.height, 'height'),
        ]

    def _init_race(self, race):
        """Init race."""
        if race == 'elf':
            self.magica += 10
            self.destruction += 10
            self.alteration += 10

        if race == 'nord':
            self.shield += 10
            self.bow += 10
            self.sword += 10

        if race == 'ork':
            self.health += 10
            self.handtohand += 10
            self.sword += 10

    def _init_attribute(self, attribute):
        """Init attributes."""
        if attribute == 'magica':
            self.magica += 10
        if attribute == 'destruction':
            self.destruction += 10
        if attribute == 'alteration':
            self.alteration += 10
        if attribute == 'health':
            self.health += 10
        if attribute == 'handtohand':
            self.handtohand += 10
        if attribute == 'shield':
            self.shield += 10
        if attribute == 'sword':
            self.sword += 10
        if attribute == 'bow':
            self.bow += 10

if __name__ == '__main__':
    new_character = Character()

    new_character.gender = input("Enter character gender: ")

    race = ''
    while race != 'elf' and race != 'nord' and race != 'ork':
        race = input("Enter character race (elf, nord, ork): ")
    new_character._init_race(race)

    new_character.hair_color = input("Enter character hair color: ")
    new_character.eye_color = input("Enter character eye color: ")
    new_character.height = input("Enter character height: ")

    print('Select three attributes to improve.')
    for i in range(3):
        attribute = ''
        while attribute != 'magica' and attribute != 'destruction' and attribute != 'alteration' and attribute != 'health' and attribute != 'handtohand' and attribute != 'shield' and attribute != 'sword' and attribute != 'bow':
            attribute = input("Enter attribute to enhance (magica, destruction, alteration, health, handtohand, shield, sword, or bow): ")
        new_character._init_attribute(attribute)

    # print is not displaying correct values but attributes are in character object

    print('Character complete.  Here are it\'s attributes:')
    for attribute in new_character.attributes:
        print('{} is at level {}'.format(attribute[1], attribute[0]))

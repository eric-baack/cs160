#!/usr/bin/env python3
"""
Exercise Zoo classes
"""
# February 20, 2019.  E Baack
# Key notes:  all functions end in (), including those inherited from super class
# Bobcat has different _str_  function that includes habitat (unlike all other animals)

from abc import ABC, abstractmethod


class Animal(ABC):
    """Class Animal"""

    @abstractmethod
    def __init__(self, spec_init, age_init, color_init):
        """Animal __init__"""
        self._spec = spec_init
        self._age = age_init
        self._color = color_init

    @abstractmethod
    def sound(self):
        """Make some noise"""
        pass

    def __str__(self):
        """__str__"""
        return "{} {} ({} yo)".format(self._color, self._spec, self._age)


class Bird(Animal):
    """Class Bird"""

    @abstractmethod
    def __init__(self, spec_init, age_init, color_init, flying_init):
        """Bird __init__"""
        super().__init__(spec_init, age_init, color_init)
        self._flying = flying_init

    def __str__(self):
        """___str__"""
        if self._flying:
            return "Flying " + super().__str__()
        return "Non-flying " + super().__str__()


class Mammal(Animal):
    """Class Mammal"""

    @abstractmethod
    def __init__(self, spec_init, age_init, color_init, habitat_init):
        """Mammal __init__"""
        super().__init__(spec_init, age_init, color_init)
        if habitat_init in ["Land", "Sea", "Air", "Tree"]:
            self._habitat = habitat_init
        else:
            raise ValueError("Incorrect habitat value")


class Parrot(Bird):
    """Parrot class"""

    def __init__(self, age_init, color_init, talking_init):
        """Parrot __init__"""
        super().__init__("Parrot", age_init, color_init, True)
        self._talking = talking_init

    def sound(self):
        """Making Parrot noise"""
        if self._talking:
            return "'Polly wants a cracker'"
        return "nothing"


class Penguin(Bird):
    """Penguin class"""

    def __init__(self, age_init, color_init):
        """Penguin __init__"""
        super().__init__("Penguin", age_init, color_init, False)

    def sound(self):
        """Making Penguin noise"""
        return "nothing"


class Canine(Mammal):
    """Class Canine"""

    @abstractmethod
    def __init__(self, spec_init, age_init, color_init, habitat_init):
        """Canine __init__"""
        super().__init__(spec_init, age_init, color_init, habitat_init)


class Feline(Mammal):
    """Class Feline"""

    @abstractmethod
    def __init__(self, spec_init, age_init, color_init, habitat_init):
        super().__init__(spec_init, age_init, color_init, habitat_init)

    def sound(self):
        """Making Feline noise"""
        return "Meow!"


class Dog(Canine):
    """Class Dog"""

    def __init__(self, age_init, color_init):
        """Dog __init__"""
        super().__init__("Dog", age_init, color_init, "Land")

    def sound(self):
        """Making Dog noise"""
        return "Woof!"


class HouseCat(Feline):
    """Class HouseCat"""

    def __init__(self, age_init, color_init):
        """HouseCat __init__"""
        super().__init__("House Cat", age_init, color_init, "Land")


class BobCat(Feline):
    """Class BobCat"""

    def __init__(self, age_, color_, habitat_):
        """BobCat __init__"""
        super().__init__("Bobcat", age_, color_, habitat_)

    def __str__(self):
        """BobCat __str__"""
        return "{} {} {} ({} yo)".format(self._color, self._habitat, self._spec, self._age)

#!/usr/bin/env python3
"""
Dice game(s) simulator
"""

import random
  # imports classes from dice.classes.py
## note change here - the path wasn't working.  Attempted other two solutions, but failed.


#!/usr/bin/env python3
"""
Dice game(s) simulator
"""

import random
from typing import Sequence

random.seed(42)


class Die:
    """Class Die"""

    def __init__(self, possible_values: Sequence) -> None:
        """Class Die constructor"""
        self._all_values = possible_values
        self._value = random.choice(self._all_values)

    @property
    def value(self):
        """Get the die value"""
        return self._value

    @value.setter
    def value(self, _):
        """Value property setter"""
        raise ValueError("You must roll the die to change its value")

    def __str__(self):
        """__str__ override"""
        return str(self._value)

        

    def roll(self):
        """Roll the die"""
        self._value = random.choice(self._all_values)
        


class FrozenDie(Die):   # inherits properties from die.
    """A die that cannot be rolled"""

    def __init__(self, possible_values: Sequence) -> None:
        """Class FrozenDie constructor"""
        super().__init__(possible_values)
        self._frozen = False

    @property
    def frozen(self) -> bool:
        """Frozen property getter"""
        return self._frozen

    @frozen.setter
    def frozen(self, new_value: bool) -> None:
        """Frozen property setter"""
        self._frozen = True

    def roll(self):
        """Roll the die"""
        if self._frozen == False:
            self._value = super.roll()

class Cup:  # does not inherit.  It has die, it is NOT die.
    """Class Cup"""

    def __init__(self, num_dice: int, num_sides: int = 6) -> None:
        """Class Cup constructor"""
        self._dice = [Die(range(1, num_sides + 1)) for _ in range(num_dice)]

    def __iter__(self):
        """Cup iterator"""
        return iter(self._dice)

    def __str__(self) -> str:
        """__str__ override"""
        dstr = ""
        for x in self._dice:  ## stuck.  how do I refer to numbered objects in dice class?
            dstr = dstr + super.__str__(x)
        return dstr



    def shake(self) -> None:  # roll all dice in cup.  Loop - iterate over dice.
        """Shake a cup"""
        raise NotImplementedError

    def add(self, die: object) -> None:  # append to list
        """Add a die to the cup"""
        raise NotImplementedError

    def remove(self, idx: int):    
        """Remove a die from the cup"""
        return self._dice.pop(idx)

    def roll(self, *args) -> None:    # challenging.  provide a list to be rolled.  
        """Roll specific dice"""      # look at *args.  Eg - which dice in cup will be rolled
        raise NotImplementedError     # differs from shake - in which all dice are rolled

random.seed(42)


def main():
    """Entry point"""
    print("Let's play a game!")
    print("Let's create a die")
    my_die = Die(range(1, 7))
    print("Rolling die 10 times")
    for i in range(10):
        my_die.roll()
        print(f"{i + 1:2}) {str(my_die):>2}")
    print(f"The last roll is {my_die.value}")
    print("Trying to assign a value to a die")
    try:
        my_die.value = 7
    except ValueError as die_exception:
        print(die_exception)
    print(f"The last roll is (still) {my_die.value}")
    print("Making a cup of 5 dice")
    my_cup = Cup(5)
    print(my_cup)
    print("Re-rolling dice 1, 2, and 3")
    my_cup.roll(1, 2, 3)
    print(my_cup)
    print("Re-rolling dice 2, 4, and 6")
    my_cup.roll(2, 4, 6)
    print(my_cup)
    print("Shaking and rolling")
    for _ in range(3):
        my_cup.shake()
        print(my_cup)
    print("Using the iterator to print dice values")
    for a_die in my_cup:
        print(a_die)
    print("Frozen die demo")
    frozen_die = FrozenDie(range(1, 7))
    print(frozen_die)
    print(frozen_die.frozen)
    frozen_die.roll()
    print(frozen_die)
    frozen_die.frozen = True
    print(frozen_die.frozen)
    for _ in range(3):
        frozen_die.roll()
        print(frozen_die)


if __name__ == "__main__":
    main()

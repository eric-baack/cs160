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
        return self._value


class FrozenDie(Die):  # inherits properties from die.
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
        if not self._frozen:
            self._value = super().roll()  # needed to add 'return self._value'

    def __str__(self):
        return str(self._value)


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
        die_list = []
        for die_obj in self._dice:  # Thanks, Isaac!
            die_list.append(die_obj.value)
        return f"{die_list}"  # better:  add to list, print list.

    def shake(self) -> None:  # roll all dice in cup.  Loop - iterate over dice.
        """Shake a cup"""
        for dice_list in self._dice:  # these are the values in the list
            dice_list.roll()

    def add(self, die: Die) -> None:  # append to list
        """Add a die to the cup"""
        self._dice.append(die)

    def remove(self, idx: int):
        """Remove a die from the cup"""
        return self._dice.pop(idx)

    def roll(self, *args) -> None:  # challenging.  provide a list to be rolled.
        """Roll specific dice"""  # look at *args.  Eg - which dice in cup will be rolled
        for dice_list in args:  # need to adjust - iterate with ctr.  This allows x
            idx = dice_list - 1
            if 0 <= idx < len(self._dice):
                self._dice[idx].roll()  ## it's a die - just roll it, don't set it!

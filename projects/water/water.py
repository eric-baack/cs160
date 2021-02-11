"""Water jugs project"""
#!/usr/bin/env python3
# encoding: UTF-8

# because lists are modifiable, lists are modified
# during function calls.  This means that it may be necessary to 'back out' lists
# if a particular search direction fails.
# Likewise, objects are mutable.  To avoid losing the original 'start state', create a clone.
# After a dead end, restore start_state to the clone.


JUG_1_MAX = 5
JUG_2_MAX = 3


class State:
    """State of the jugs"""

    def __init__(self, jug_1: int, jug_2: int):
        """__init__"""
        self._jug1 = jug_1
        self._jug2 = jug_2

    def __eq__(self, other: object):
        """__eq__"""
        eq_state = False
        if self._jug1 == other._jug1 and self._jug2 == other._jug2:
            eq_state = True
        return eq_state

    def __str__(self):
        """__str__"""
        state_str = f"Jug 1 = {self._jug1} & Jug 2 = {self._jug2}"
        return state_str

    def clone(self):
        """Copy a state"""
        # This is avoids the use of the copy module and deep copy
        # Makes a deep copy of the object, not a shallow copy (which is simply another pointer)
        # Alternative:  import copy.  Use old_state = copy.deepcopy(start_state)
        return State(self._jug1, self._jug2)

    def fill_jug_1(self):
        """Fill jug1 to capacity from the pump"""
        self._jug1 = JUG_1_MAX

    def fill_jug_2(self):
        """Fill jug2 to capacity from the pump"""
        self._jug2 = JUG_2_MAX

    def empty_jug_1(self):
        """Pour the water from jug1 onto the ground"""
        self._jug1 = 0

    def empty_jug_2(self):
        """Pour the water from jug2 onto the ground"""
        self._jug2 = 0

    def pour_jug_1_to_jug_2(self):
        """Pour as much water as you can from jug1 to jug2 without spilling"""
        jug2_cap = JUG_2_MAX - self._jug2
        if self._jug1 <= jug2_cap:
            self._jug2 = self._jug2 + self._jug1
            self._jug1 = 0
        else:
            self._jug2 = JUG_2_MAX
            self._jug1 = self._jug1 - jug2_cap

    def pour_jug_2_to_jug_1(self):
        """Pour as much water as you can from jug2 to jug1 without spilling"""
        jug1_cap = JUG_1_MAX - self._jug1
        if self._jug2 <= jug1_cap:
            self._jug1 = self._jug1 + self._jug2
            self._jug2 = 0
        else:
            self._jug1 = JUG_1_MAX
            self._jug2 = self._jug2 - jug1_cap


def search(start_state: object, goal: object, moves: list):
    """Find a sequence of states"""
    moves.append(start_state.__str__())
    old_state = start_state.clone()
  # make copy of initial start_state to restore after mutation
    for i in range(7):
        if i == 6:
            print("!")
            moves.pop()  # remove dead-end move from list of moves
        elif i == 0:
            start_state.fill_jug_2()
        elif i == 5:
            start_state.fill_jug_1()
        elif i == 2:
            start_state.empty_jug_1()
        elif i == 4:
            start_state.empty_jug_2()
        elif i == 3:
            start_state.pour_jug_1_to_jug_2()
        elif i == 1:
            start_state.pour_jug_2_to_jug_1()

        if i < 6:
            if start_state == goal:
                print("Goal!")
                moves.append(start_state.__str__())
                return
            elif start_state.__str__() in moves:
                start_state = old_state.clone()  # restore start_state after dead end
                pass
            else:
                search(start_state, goal, moves) # search recursively
                if str(goal) in moves:  #necessary to end program if search successful
                    return


def main():
    """Main function"""
    # goal = State(4,0)
    # js = State(0,0)
    # js.fill_jug_2()
    # js.pour_jug_2_to_jug_1()
    # print(js)
    # js.fill_jug_1()
    # js.pour_jug_1_to_jug_2()
    # print(js)
    # js.fill_jug_2()
    # js.pour_jug_2_to_jug_1()
    # js.empty_jug_1()
    # js.pour_jug_2_to_jug_1()
    # js.fill_jug_2()
    # js.pour_jug_2_to_jug_1()
    # if js == goal:
    #     print("goal!")
    # print(js)
    goal = State(4, 0)
    start = State(0, 0)
    moves = []
    search(start, goal, moves)
    print(", ".join([str(s) for s in moves]))


if __name__ == "__main__":
    main()

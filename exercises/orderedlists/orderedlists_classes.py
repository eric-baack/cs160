#!/usr/bin/env python3
"""Ordered List classes"""

import random
import typing

random.seed(42)


# Passing all tests.  Need to do pylint, mypy, black.
# Next, implement bank.  But must do grading as higher priority
# Due Mon 9 PM
# Bank due Wed 9 PM - work on Mon & at conference.


class Node:
    """Node of a linked list"""

    def __init__(self, init_data: typing.Any):
        """Initializer"""
        self._data = init_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, new_data: typing.Any) -> None:
        """Set node data"""
        self._data = new_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, new_next: object) -> None:
        """Set next node"""
        self._next = new_next

    next = property(get_next, set_next)

    def __str__(self) -> str:
        """Convert data to string"""
        return str(self._data)


class OrderedList:
    """Ordered Linked List class"""

    def __init__(self):
        """Initializer"""
        self._head = None
        self._count = 0

    def __getitem__(self, position: int):
        """Get item by its position

        Takes position (an int)

        Returns value from ordered list at that position, or -1 if position does not exist
        """
        idx = 0
        current = self._head
        if current is None:
            return -1
        while idx != position:
            if current.next is None:  # return last item if pos > length
                return current.data
            current = current.next
            idx += 1
        return current.data

    def __len__(self) -> int:
        """Get list size"""
        return self._count

    def __str__(self) -> str:
        """List as a string"""
        list_out = []
        current = self._head
        while current is not None:
            list_out.append(str(current.data))
            current = current.next
        return "[" + ", ".join(list_out) + "]"

    def is_empty(self) -> bool:
        """Check if the list is empty"""
        return self._head is None

    def size(self) -> int:
        """Get list size"""
        return self._count

    def add(self, value: typing.Any) -> None:
        """
        Add a new item to the list
        Takes a value of any type
        Finds location of that value in the list
        Adds node to list at that location, even if item is already present in the li
        """
        current = self._head
        self._count += 1
        new_node = Node(value)
        if current is None:
            self._head = new_node
        else:
            prior = None
            # Move through list, until value to add no longer exceeds current value
            while value > current.data:
                prior = current
                if current.next is None:
                    current.next = new_node
                    return
                else:
                    current = current.next
            # if value to add lies between prior and current, add node to list
            if prior is not None:
                prior.next = new_node
                new_node.next = current
            else:
                self._head = new_node
                new_node.next = current
        return

    def pop(self, position: int = None):
        """
        Remove at item (last one by default) and get its value

        Remove the last element if the provided position is greater than the length of the list
        Raise ValueError if the list is empty
        Raise IndexError if the provided position is negative
        """
        if self._count == 0:
            raise ValueError("List is empty")
        else:
            if (
                position is None
            ):  # if no position given, make position = last item in list
                position = self._count - 1
            elif position < 0:
                raise IndexError("Position must be a positive value")
                return -1
            current = self._head
            idx = 0
            prior = None
            while idx < position:
                prior = current
                if current.next is None:
                    prior.next = None
                    self._count -= 1
                    return current.data
                current = current.next
                idx += 1
            if prior is None:
                self._head = current.next
            else:
                prior.next = current.next
            self._count -= 1
            return current.data

    def append(self, value: typing.Any) -> None:
        """
        Append item to list - but as list is ordered, it is not necessarily at end

        Calls self.add
        """
        self.add(value)

    def insert(self, position: int, value: typing.Any) -> None:
        """Insert a new item into the list"""
        self.add(value)

    def search(self, value: typing.Any) -> bool:
        """Search for an item in the list"""
        current = self._head
        while current is not None:
            if current.data == value:
                return True
            if current.data > value:
                return False
            current = current.next
        return False

    def index(self, value: typing.Any) -> int:
        """Return position of an item in the list"""
        idx = 0
        current = self._head
        while current:
            if current.data == value:
                return idx
            current = current.next
            idx += 1
        return -1

#!/usr/bin/env python3
"""Banking classes implementation"""

from abc import ABC, abstractmethod

# Data members as properties.  As property of class needs its own set / get.
# Solution:  need to implement get / set for each property
# Address has four properties:  street, city, state, zip.  Need to get/ set each.

# Address, customer, account pass.
# Checking account currently fails.

# passes tests
class Address:
    """Address class"""

    def __init__(
        self, street_init: str, city_init: str, state_init: str, zip_init: str
    ):
        """__init__"""
        self._street = street_init
        self._city = city_init
        self._state = state_init
        self._zip = zip_init

    def get_street(self):
        """ getter for address.street"""
        return self._street

    def get_city(self):
        """getter for address.city"""
        return self._city

    def get_state(self):
        """ getter for address.state"""
        return self._state

    def get_zip(self):
        """ getter for addres.zip"""
        return self._zip

    def set_street(self, new_street):
        """setter for address.street"""
        self._street = new_street

    def set_city(self, new_city):
        """ setter for address.city"""
        self._city = new_city

    def set_state(self, new_state):
        """ setter for address.state """
        self._state = new_state

    def set_zip(self, new_zip):
        """ setter for address.zip"""
        self._zip = new_zip

    street = property(get_street, set_street)

    state = property(get_state, set_state)

    city = property(get_city, set_city)

    zip = property(get_zip, set_zip)

    def __eq__(self, other: object):
        """Compare 2 addresses"""
        address_ident = True
        if self.street != other.street:
            address_ident = False
        elif self.city != other.city:
            address_ident = False
        elif self.state != other.state:
            address_ident = False
        elif self.zip != other.zip:
            address_ident = False
        return address_ident

    def __str__(self):
        """__str method"""
        return "{}\n{}, {} {}".format(self._street, self._city, self._state, self._zip)


class Customer:
    """Customer class"""

    def __init__(self, name_init: str, dob_init: str, address_init: object):
        """Constructor"""
        self._name = name_init
        self._dob = dob_init
        self._address = address_init

    def get_name(self):
        """getter for customer.name"""
        return self._name

    def get_dob(self):
        """ getter for customer.dob"""
        return self._dob

    def get_address(self):
        """ getter for customer.address"""
        return self._address

    def set_name(self, new_name):
        """setter for customer.name"""
        self._name = new_name

    def set_dob(self, new_dob):
        """setter for customer.dob"""
        self._dob = new_dob

    def set_address(self, new_address):
        """setter for customer.address"""
        self._address = new_address

    name = property(get_name, set_name)

    dob = property(get_dob, set_dob)

    address = property(get_address, set_address)

    def move(self, new_address: object):
        """Change address"""
        self._address = new_address

    def __str__(self):
        """__str"""
        return "{} ({})\n{}".format(self._name, self._dob, self._address)


# passes tests
class Account(ABC):
    """Account class"""

    @abstractmethod
    def __init__(self, owner_init: object, balance_init: float = 0):
        """Constructor"""
        self._owner = owner_init
        self._balance = balance_init

    def get_owner(self):
        """ getter for account.owner"""
        return self._owner

    def get_balance(self):
        """getter for account.balance """
        return self._balance

    def set_owner(self, new_owner):
        """ setter for account.owner"""
        self._owner = new_owner

    def set_balance(self, new_balance):
        """ setter for account.balance"""
        self._balance = new_balance

    owner = property(get_owner, set_owner)

    balance = property(get_balance, set_balance)

    def deposit(self, amount: float):
        """Add money"""
        if amount < 0:
            raise ValueError("Must deposit positive amount")
        self._balance = self._balance + amount

    def close(self):
        """Close account"""
        self._balance = 0

    def __str__(self):
        """__str__"""
        return "{0}, {1:.2f}".format(self._owner, self._balance)


# Partial success.  Need to format balance with 2 decimal points.  Leave for Mon.


class CheckingAccount(Account):
    """CheckingAccount class"""

    def __init__(self, owner_init: object, fee_init: float, balance_init: float = 0):
        """Constructor"""
        super().__init__(owner_init, balance_init)
        self._fee = fee_init

    def process_check(self, amount: float):
        """Process a check"""
        if amount < 0:
            raise ValueError("Checks must be for positive values")
        elif self._balance > amount:
            self._balance = self._balance - amount
        # if insufficient funds, substract fee in addition.
        else:
            self._balance = self._balance - self._fee

    # format is incorrect here!
    def __str__(self):
        """__str__"""
        chk_owner = self._owner
        chk_balance = "Balance: %.2f" % (float(self._balance))
        return f"Checking account\nOwner: {self._owner}\n{chk_balance}"


class SavingsAccount(Account):
    """CheckingAccount class"""

    def __init__(
        self, owner_init: object, interest_rate_init: float, balance_init: float = 0
    ):
        """Constructor"""
        super().__init__(owner_init, balance_init)
        self._interest_rate = interest_rate_init

    def yield_interest(self):
        """Yield annual interest"""
        self._balance = self._balance + (self._balance * self._interest_rate / 100)

    def __str__(self):
        """__str__"""
        sav_balance = "Balance: %.2f" % self._balance
        return f"Savings account\nOwner: {self._owner}\n{sav_balance}"


def main():
    """Main"""
    address = Address("700 College Dr", "Decorah", "IA", "52101")
    print(address)
    print(address.street)


if __name__ == "__main__":
    main()

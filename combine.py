from typing import Protocol, runtime_checkable


@runtime_checkable
class Combinable(Protocol):

    def can_combine(self, other: "Combinable") -> bool:
        """return True only if other object meets the following conditions:
        It is an instance of Candy.
        It has the same name as self.
        It has the same price per pound as self.
        otherwise False"""

    def combine(self, other: "Combinable") -> "Combinable":
        """add the weight of other to the weight of self destructively"""

"""example module.

This module demonstrates docstrings and is used as an example for Sphinx autodoc.
"""
from typing import Any


class ExampleClass:
    """ExampleClass class.

    This class is a simple example for demonstrating Sphinx autodoc.
    """

    def __init__(self, value: Any) -> None:
        """
        Initilize ExampleClass
        :param value: Any value
        """
        self.value = value

    def get_value(self) -> Any:
        """
        Returns the `value` attribute.
        :return: Value
        """
        return self.value


def example_function_2(value: int):
    """Return input value (identity)
    
    :param value: Integer
    :return: Identity
    """

    return value

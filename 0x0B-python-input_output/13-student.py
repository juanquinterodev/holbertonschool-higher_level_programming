#!/usr/bin/python3
"""Define a student
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__

        s = {}

        for key in attrs:
            if key in self.__dict__:
                s[key] = self.__dict__[key]

        return s

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        """
        for keys in json:
            self.__dict__[keys] = json[keys]

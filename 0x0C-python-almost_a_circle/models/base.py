#!/usr/bin/python3
"""
Base class fo all other classes
methods:
def __init__(self, id=None):
"""
import json


class Base:
    """
    Private class atrribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method which checks and
        returns list of dictionaries to json strings
        :return:
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list or \
                not all(type(i) == dict for i in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        JSON Serialization of a list of objects
        :param list_objs:
        :return:
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as a_file:
            if list_objs is None or list_objs == []:
                a_file.write("[]")
            else:
                dict_list = [i.to_dictionary() for i in list_objs]
                a_file.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialization of JSON to string
        :param json_string:
        :return:
        """
        if json_string is None or json_string == []:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """

        :param dictionary:
        :return:
        """
        if not dictionary and dictionary == {}:
            return
        if cls.__name__ == "Rectangle":
            dummy = cls(1,1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

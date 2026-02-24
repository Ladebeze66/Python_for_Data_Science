#!/usr/bin/env python3
# tester.py

from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list) # List : <class 'list'>
all_thing_is_obj(ft_tuple) # Tuple : <class 'tuple'>
all_thing_is_obj(ft_set) # Set : <class 'set'>
all_thing_is_obj(ft_dict) # Dict : <class 'dict'>
all_thing_is_obj("Brian") # Brian is in the kitchen : <class 'str'>
all_thing_is_obj("Toto") # Toto is in the kitchen : <class 'str'>

print(all_thing_is_obj(10))

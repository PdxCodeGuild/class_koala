# filename: jackalopeTest2.py
import random

def name_generator():
    syllable_list = ["ma", "pa", "io", "al", "co", "ex", "fr", "jo", "sa", "ra", "ro", "el", "ti"]
    random_name = ""
    for i in range(3):
        random_name += random.choice(syllable_list)
    return random_name

def jackalope_dict(list, name):
    sex = ["m", "f"]
    jack = {"name": name, "age": 4, "sex": random.choice(sex), "pregnant": False, "viability": False}
    list.append(jack)
    return list

def viability(list):
    for jack in list:
        if jack["age"] >= 4 and jack["age"] <= 8:
            if list.index(jack) < len(list)-1:
                if jack["sex"] != list[list.index(jack)+1]["sex"]:
                    if list[list.index(jack)+1]["pregnant"] == False:
                        jack["viability"] = True
            if list.index(jack) > 0:
                if jack["sex"] != list[list.index(jack)-1]["sex"]:
                    if list[list.index(jack)-1]["pregnant"] == False:
                        jack["viability"] = True


jackalopes = []
jackalope_dict(jackalopes, name_generator())
jackalope_dict(jackalopes, name_generator())
jackalope_dict(jackalopes, name_generator())
jackalope_dict(jackalopes, name_generator())
jackalope_dict(jackalopes, name_generator())
jackalope_dict(jackalopes, name_generator())
jackalope_dict(jackalopes, name_generator())
jackalope_dict(jackalopes, name_generator())
jackalope_dict(jackalopes, name_generator())
viability(jackalopes)
print(jackalopes)








#

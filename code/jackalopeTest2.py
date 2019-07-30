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
    jack = {"name": name, "age": 0, "sex": random.choice(sex), "pregnant": False}
    list.append(jack)
    return list

def viability(list, jack):
    if jack["age"] >= 4 and jack["age"] <= 8:
        if list.index(jack) < len(list)-1:
            if jack["sex"] != list[list.index(jack)+1]["sex"]:
                if list[list.index(jack)+1]["pregnant"] == False:
                    return True
                else:
                    return False
        if list.index(jack) > 0:
            if jack["sex"] != list[list.index(jack)-1]["sex"]:
                if list[list.index(jack)-1]["pregnant"] == False:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False




jackalopes = []
jackalope_dict(jackalopes, name_generator())
jackalope_dict(jackalopes, name_generator())
years = 0
while years < 100:
    for jack in jackalopes:
        if jack["pregnant"] == True:
            jackalope_dict(jackalopes, name_generator())
            jackalope_dict(jackalopes, name_generator())
            jack["pregnant"] = False
        jack["age"] += 1
    for jack in jackalopes:
        if jack["age"]>10:
            jackalopes.remove(jack)
    random.shuffle(jackalopes)
    for jack in jackalopes:
        viable = viability(jackalopes, jack)
        if viable == True:
            if jack["sex"] == "f":
                jack["pregnant"] = True
    years += 1

    print(years, len(jackalopes))
print(jackalopes)
print(len(jackalopes))

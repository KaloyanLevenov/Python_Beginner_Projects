def madlib():
    print("Zombie madlib:")
    time_of_day = input("Time of Day: ")
    body_part_plural = input("Body Part (plural): ")
    color = input("Color: ")
    verb_past_tense = input("Verb (past tense): ")
    food = input("Food: ")
    noun_one = input("Noun: ")
    noun_plural_one = input("Noun (plural): ")
    adjective = input("Adjective: ")
    adjective_two = input("Adjective: ")
    adjective_three = input("Adjective: ")

    madlib = f"It was a {adjective} summer {time_of_day} when we realized that the vaccine to stop \n\
spread of the disease did not work. Instead, it produced ZOMBIES!!! They were thirsty for {body_part_plural} \n\
and the streets were lined with these monsters holding {noun_plural_one} in their hands. \n\
Their eyes were {color} with hunger as they {verb_past_tense} around the city looking for {food}. \n\
They were {adjective_two} and {adjective_three}, unknowing how to act in this human world... except eat {body_part_plural}!!!! \n\
That was their sole mission and they were dedicated towards achieving it for the sake of {noun_one}."

    print(madlib)
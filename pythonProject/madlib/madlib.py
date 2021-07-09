import random


def print3DiffWays(youTuber):
    print("Welcome to madlib " + youTuber)
    print("Welcome to madlibs {}".format(youTuber))
    print(f"Welcome to madlibs {youTuber}")


def print_out_madlibs1(adjectives):
    print(f'''The summer vacation 2021 has been {adjectives[0]}, 
            we have had a {adjectives[1]} time so far, done a few things planned, 
            it was a {adjectives[2]} idea with the vision board we have somehow not been 
            good at implementing the daily non-negotiables, which is {adjectives[3]}''')


def print_out_madlibs2(adjectives):
    print(f"""This thing about Pokémon TCG is really {adjectives[0]},
           we have looked up one site to get ideas on how to build a {adjectives[1]}
           card stack with basic, stage-1, stage-3 cards and a {adjectives[2]} deal of helper cards 
           and a bunch of energy cards, we just realized we have only 2 energy cards, which is quite {adjectives[3]}""")


def print_out_madlibs3(adjectives):
    print(f"""Kaddy has been endlessly obsessing about a new iPhoneXR, which is {adjectives[0]} 
           She has not done all her daily non-negotiables even for a single day, which is {adjectives[1]}
           Yet she wants to dive deeper into the zombie world of chat apps and apple fones, kinda {adjectives[2]} 
           she is an extrmely {adjectives[3]} child and can be really successful in life, if she puts in some smart work and motivation""")


if __name__ == "__main__":
    adjectives = []
    for i in range(0, 4):
        adjectives.append(input("Enter a cool adjective: "))
    random.choice([print_out_madlibs1,
                   print_out_madlibs2, print_out_madlibs3])(adjectives)

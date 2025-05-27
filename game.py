import random
import time
from pet import Pet
from game_stats import GameStats

def feed_pet(pet):
    pet.increase_fullness()
    print(f"{pet.name} is eating", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(f"\n{pet.name} ate it with great relish! Fullness is now {pet.fullness}.")


def play_with_pet(pet):
    pet.decrease_fullness()
    pet.increase_mood()
    print(f"{pet.name} is playing with you", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(f"\nYou played with {pet.name}! Mood: {pet.mood}, Fullness: {pet.fullness}")


def give_toy(pet, game_stats):
    toy_list = ["ball", "rope", "bone", "mouse", "teddy bear", "poop"]
    # Define toy preferences with emojis
    toy_list = [
        ("ball", "🏀"),
        ("rope", "🧶"),
        ("bone", "🦴"),
        ("mouse", "🐁"),
        ("teddy bear", "🧸"),
        ("poop", "💩")
    ]
    print("Choose a toy:")
    for i, toy_name in enumerate(toy_list, 1):
        print(f"{i}. {toy_name[0]}")
    while True:
        t_choice = input("Enter the toy number (1-6): ")
        if t_choice in [str(i) for i in range(1, 7)]:
            toy = toy_list[int(t_choice) - 1]
            break
        print(f"'{t_choice}' is not valid. Please enter a number between 1 and 6.")

    print(f"{pet.name} is playing with {toy[1]}", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print()

    if toy[0] == pet.preference[0]:
        for _ in range(3):
            pet.increase_mood()
        if pet.species == "Haohao" and toy[0] == "poop":
            game_stats.haohao_likes_poop = True
        print(f"{pet.name} loves that toy! Mood +3!")
    else:
        if pet.species != "Haohao" and toy == "poop":
            for _ in range(2):
                pet.decrease_mood()
                pet.decrease_cleanliness()
            print(f"{pet.name} hated the poop! Mood and Cleanliness -2!")
        else:
            mood_boost = random.randint(0, 2)
            for _ in range(mood_boost):
                pet.increase_mood()
            print(f"{pet.name} likes {toy}! Mood +{mood_boost}!")


def bathe_pet(pet):
    pet.increase_cleanliness()
    print(f"{pet.name} is taking a shower", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(f"\nYou bathed {pet.name}. Cleanliness is now {pet.cleanliness}.")


def handle_death(pet, reason, stats):
    print(f"{pet.name} {reason}")
    pet.alive = False
    stats.register_death()


def show_achievements(stats):
    print("--- Achievements ---")
    for sp, count in stats.species_counter.items():
        if count > 3:
            print(f"{sp} Lover")
    if stats.all_species_seen():
        print("Family Reunion")
    if stats.haohao_likes_poop:
        print("Special Taste")
    if stats.loved_pets > 0:
        print("Full of Love")

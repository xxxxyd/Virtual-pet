import random
import time
from pet import Pet
from game_stats import GameStats
from game import feed_pet, play_with_pet, give_toy, bathe_pet, handle_death, show_achievements

species_options = ["Kitten", "Puppy", "Hamster", "Rabbit", "Haohao"]
gender_options = ["Male", "Female"]

def create_pet(stats):
    print("---------------------------------------------------------")
    name = input("What is your pet's name? ")

    print("Choose your pet species:")
    for i, species in enumerate(species_options, 1):
        print(f"{i}. {species}")
    while True:
        choice = input("Enter a number (1-5): ")
        if choice in ['1', '2', '3', '4', '5']:
            species = species_options[int(choice) - 1]
            break
        print(f"'{choice}' is not valid. Please enter a number between 1 and 5.")

    print("Choose gender:")
    print("1. Male\n2. Female")
    while True:
        g_choice = input("Enter 1 or 2: ")
        if g_choice in ['1', '2']:
            gender = gender_options[int(g_choice) - 1]
            break
        print(f"'{g_choice}' is not valid. Please enter 1 or 2.")

    print("---------------------------------------------------------")
    count = stats.update_species(species)
    return Pet(name, species, gender, count)

def print_actions():
    print("\n---------------------------------------------------------\nAvailable actions:")
    print("1. Feed        2. Play         3. Give Toy     4. Bathe")
    print("5. Abandon     6. Sleep        7. End Game")

def handle_action(pet, stats):
    actions_left = 4
    day_over = False
    while not day_over:
        print_actions()
        choice = input(f"Choose an action (1-7), {actions_left} left today: ")

        if choice == '1':
            if actions_left > 0:
                feed_pet(pet)
                print(pet)
                actions_left -= 1
            else:
                print("No actions left. Your pet needs sleep.")
        elif choice == '2':
            if actions_left > 0:
                play_with_pet(pet)
                print(pet)
                actions_left -= 1
            else:
                print("No actions left. Your pet needs sleep.")
        elif choice == '3':
            if actions_left > 0:
                give_toy(pet, stats)
                print(pet)
                actions_left -= 1
            else:
                print("No actions left. Your pet needs sleep.")
        elif choice == '4':
            if actions_left > 0:
                bathe_pet(pet)
                print(pet)
                actions_left -= 1
            else:
                print("No actions left. Your pet needs sleep.")
        elif choice == '5':
            pet.abandon()
            print(f"You abandoned {pet.name}. They wandered the streets alone and sadly did not survive.")
            handle_death(pet, "was abandoned and didn't make it...", stats)
            return False
        elif choice == '6':
            print(f"{pet.name} is going to sleep", end="", flush=True)
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print("\nSweet dreams...")
            day_over = True
        elif choice == '7':
            print("--- GAME SUMMARY ---")
            for sp, count in stats.species_counter.items():
                if count > 0:
                    print(f"{sp}: {count} time(s)")
            print(f"Number of pets that died: {stats.dead_pet_count}")
            if stats.dead_pet_count > 0:
                print("Please be kind to real pets. They love and need you.")
            show_achievements(stats)
            print("Thank you for playing!")
            exit()
        else:
            print(f"'{choice}' is not valid. Please choose a number between 1 and 7.")
    return True

def run_game_loop(pet, stats):
    while pet.age < 5 and pet.alive:
        print(f"\n---------------------------------------------------------\nA new day begins!\n--- Day {pet.age + 1} ---")
        print(pet)

        still_playing = handle_action(pet, stats)
        if not still_playing:
            return

        if pet.mood == 5 and pet.fullness == 5:
            pet.increase_intimacy()

        # Cleanliness impact on mood
        mood_loss = 6 - pet.cleanliness
        for _ in range(mood_loss):
            pet.decrease_mood()

        # Random drop in fullness and cleanliness
        for _ in range(random.randint(1, 2)):
            pet.decrease_fullness()
        for _ in range(random.randint(1, 2)):
            pet.decrease_cleanliness()

        if pet.fullness == 0:
            handle_death(pet, "has starved... They passed away.", stats)
            break
        if pet.mood == 0:
            handle_death(pet, "became too sad and left this world...", stats)
            break

        pet.age += 1

    print("\n--- The Journey Ends! ---")
    if pet.alive:
        if pet.age >= 5:
            print(f"{pet.name} has grown up and left to explore the world!")
        if pet.intimacy == 5:
            print(f"{pet.name} loves you.")
            stats.loved_pets += 1
        print("God bless you.")
    else:
        print("Farewell.")

def main():
    stats = GameStats()
    print("Welcome to the Virtual Pet Game!")
    while True:
        pet = create_pet(stats)
        run_game_loop(pet, stats)

if __name__ == "__main__":
    main()
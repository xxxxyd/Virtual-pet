class GameStats:
    def __init__(self):
        self.species_counter = {
            "Kitten": 0,
            "Puppy": 0,
            "Hamster": 0,
            "Rabbit": 0,
            "Haohao": 0
        }
        self.dead_pet_count = 0
        self.haohao_likes_poop = False
        self.loved_pets = 0

    def update_species(self, species):
        self.species_counter[species] += 1
        return self.species_counter[species]

    def register_death(self):
        self.dead_pet_count += 1

    def all_species_seen(self):
        return all(count > 0 for count in self.species_counter.values())

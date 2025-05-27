import random

class Pet:
    def __init__(self, name, species, gender, count):
        import random
        self.name = name
        self.species = species
        self.gender = gender
        self.age = 0
        self.fullness = random.randint(2, 4)  # Range: 2–4
        self.mood = random.randint(2, 4)      # Range: 2–4
        self.cleanliness = random.randint(2, 4)  # Range: 2–4
        self.intimacy = 0  # Range: 0–5
        self.alive = True
        self.count = count

        # Define toy preferences with emojis
        toys = [
            ("ball", "🏀"),
            ("rope", "🧶"),
            ("bone", "🦴"),
            ("mouse", "🐁"),
            ("teddy bear", "🧸"),
            ("poop", "💩")
        ]

        if self.species == "Haohao":
            self.preference = ("poop", "💩")
        else:
            self.preference = random.choice(toys[:4])

        # Define appearances by species
        species_emoji = {
            "Kitten": "😺",
            "Puppy": "🐶",
            "Hamster": "🐹",
            "Rabbit": "🐰",
            "Haohao": "🧒"
        }
        gender_emoji = {
            "Male": "♂️",
            "Female": "♀️"
        }
        self.appearance = species_emoji.get(self.species, "🦖") + gender_emoji.get(self.gender, "")

    def increase_fullness(self):
        if self.fullness < 5:
            self.fullness += 1

    def decrease_fullness(self):
        if self.fullness > 0:
            self.fullness -= 1

    def increase_mood(self):
        if self.mood < 5:
            self.mood += 1

    def decrease_mood(self):
        if self.mood > 0:
            self.mood -= 1

    def increase_cleanliness(self):
        if self.cleanliness < 5:
            self.cleanliness += 1

    def decrease_cleanliness(self):
        if self.cleanliness > 0:
            self.cleanliness -= 1

    def increase_intimacy(self):
        if self.intimacy < 5:
            self.intimacy += 1

    def abandon(self):
        self.alive = False

    def __str__(self):
        def bar(value, max_val):
            return ''.join(['●' if i < value else '○' for i in range(max_val)])

        name_pad = ' ' * (21 - len(self.name))
        age_str = str(self.age)
        age_pad = ' ' * (21 - len(age_str))
        mood_bar = bar(self.mood, 5)
        mood_pad = ' ' * (21 - len(mood_bar))

        if self.count == 1:
            ordinal = 'st'
        elif self.count == 2:
            ordinal = 'en'
        elif self.count == 3:
            ordinal = 'rd'
        else:
            ordinal = 'th'

        display = (f'----------------------My {self.count}{ordinal} {self.species}----------------------\nName: {self.name}{name_pad}| Appearance:  {self.appearance}\nAge:  {self.age}{age_pad}| Fullness:    {bar(self.fullness, 5)}\nMood: {mood_bar}{mood_pad}| Cleanliness: {bar(self.cleanliness, 5)}\n---------------------------------------------------------\n')
        return display.strip()

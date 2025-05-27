# 🐾 Virtual Pet Game

A text-based virtual pet care game where you feed, play, bathe, and give toys to your pet while unlocking achievements along the way!

---

## 📁 File Structure

- `main.py` - Entry point of the game, handles the main loop and user interaction.
- `pet.py` - Defines the `Pet` class with attributes and behaviors.
- `game.py` - Implements interaction logic such as feeding, playing, bathing, and gifting toys.
- `game_stats.py` - Tracks gameplay progress and achievements.

---

## 🔧 How to Use

Start the game by running:

```bash
python main.py
```

---

## 🧸 File Descriptions

### `main.py`

- Manages the overall game flow:
  - Creates a pet with a name, species, and gender.
  - Allows 4 actions per in-game day: Feed, Play, Give Toy, Bathe, Abandon, Sleep, or End Game.
  - The pet lives for 5 days and may die if its mood or fullness drops to zero.
- Tracks pet condition and ends the game when appropriate.
- Displays game summary and achievements.

### `pet.py`

Defines the `Pet` class with attributes such as:

- `name`, `species`, `gender`, `age`, `fullness`, `mood`, `cleanliness`, `intimacy`, `alive`
- `appearance`: Emoji representation based on species and gender
- `preference`: Toy preference depending on species

Includes methods to adjust pet status and a string representation for display.

### `game.py`

Contains interaction functions:

- `feed_pet(pet)`
- `play_with_pet(pet)`
- `give_toy(pet, game_stats)`
- `bathe_pet(pet)`
- `handle_death(pet, reason, stats)`
- `show_achievements(stats)`

Toy interactions vary by species; some may impact achievement tracking (e.g., "Haohao" likes 💩).

### `game_stats.py`

Defines the `GameStats` class, tracking:

- Number of pets by species
- Death count
- Whether special interactions occurred (e.g., Haohao likes 💩)
- Whether any pet reached max intimacy

---

## 🏆 Achievements

The game includes the following achievements:

- `Kitten/Puppy/etc. Lover`: Own more than 3 pets of a single species
- `Family Reunion`: Own at least one of each of the 5 species
- `Special Taste`: Haohao enjoys 💩
- `Full of Love`: At least one pet loves you (max intimacy)

---

## 📌 Notes

- Pets have emotional and physical needs. Neglect can lead to death.
- The game subtly encourages care and empathy for real pets.
- Great for practicing Python classes, logic, and input handling.

---

Want to extend the game? Consider adding a GUI, saving progress, or introducing new interactions!
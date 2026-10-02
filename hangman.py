import random

print("\n" + "=" * 40)
print("          🎮 H A N G M A N")
print("=" * 40)

print("""
📂 SELECT CATEGORY

  1. 🐾 Animals
  2. 💻 Technology
  3. 🍕 Food
  4. 🌍 Places
  5. 🌿 Nature
  6. ⚽ Sports
  7. 🎨 Colors
  8. 🚗 Vehicles
  9. 👨‍💻 Programming
 10. 🎬 Entertainment
""")

select_cat = input("👉 Enter category number: ")

categories = {
    "1": "animals",
    "2": "technology",
    "3": "food",
    "4": "places",
    "5": "nature",
    "6": "sports",
    "7": "colors",
    "8": "vehicles",
    "9": "programming",
    "10": "entertainment"
}

if select_cat not in categories:
    print("\n❌ Invalid category! Please restart the game.")
    exit()

select_cat = categories[select_cat]


print("""
🎯 SELECT LEVEL

  1. 🟢 Easy
  2. 🟡 Medium
  3. 🔴 Hard
""")

select_level = input("👉 Enter level number: ")

levels = {
    "1": "easy",
    "2": "medium",
    "3": "hard"
}

if select_level not in levels:
    print("\n❌ Invalid level! Please restart the game.")
    exit()

select_level = levels[select_level]


# Read words from file
with open("words.txt", "r") as file:
    content = [line.strip() for line in file.readlines()]


# Find matching words
matching_words = []

for line in content:
    parts = line.split(",")

    if parts[0] == select_cat and parts[1] == select_level:
        matching_words.append(parts[2])


# Select a random word
computer = random.choice(matching_words)

# Create blanks
b = "_" * len(computer)

print("\n" + "=" * 40)
print("          🎮 GAME STARTED!")
print("=" * 40)

print(f"📂 Category : {select_cat.title()}")
print(f"🎯 Level    : {select_level.title()}")
print(f"❤️ Attempts : 14")

print("\n🔤 Word:")
print("   " + " ".join(b))

print("\n" + "-" * 40)


# Store guessed letters
s = set()

i = 1

while i <= 14:

    print(f"\n❤️ Attempts left: {15 - i}")

    player = input("👉 Guess a letter: ").lower()

    if len(player) != 1:
        print("⚠️ Please enter only one letter.")
        continue

    if player in s:
        print("🔁 You already guessed this letter.")
        continue

    s.add(player)

    print("📝 Guessed letters:", " ".join(sorted(s)))

    i += 1

    # Correct guess
    if player in computer:

        for index in range(len(computer)):

            if computer[index] == player:
                b = b[:index] + player + b[index + 1:]

        print("\n✅ Correct guess!")
        print("🔤 Word:")
        print("   " + " ".join(b))

        # Check if word is completely guessed
        if b == computer:

            print("\n" + "=" * 40)
            print("       🎉 YOU WON! 🎉")
            print("=" * 40)

            print(f"🏆 Congratulations!")
            print(f"🔤 The word was: {computer}")
            print(f"❤️ Attempts used: {i - 1}")

            print("\n✨ Great job! Thanks for playing!")
            break

    # Wrong guess
    else:

        print("\n❌ Letter not found!")
        print("🔤 Word:")
        print("   " + " ".join(b))


# Game Over
if b != computer:

    print("\n" + "=" * 40)
    print("        💀 GAME OVER")
    print("=" * 40)

    print(f"🔤 The word was: {computer}")
    print(f"💔 You used all 14 attempts.")

    print("\n😄 Better luck next time!")

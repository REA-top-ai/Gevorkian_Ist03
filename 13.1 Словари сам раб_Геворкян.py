letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {letter: point for letter, point in zip(letters, points)}
letter_to_points[" "] = 0

def score_word(word):
    total = 0
    for letter in word.upper():
        total += letter_to_points.get(letter, 0)
    return total

print(score_word("BLUE"))
print(score_word("EARTH"))
print(score_word("ERASER"))
print(score_word("ZAP"))
print(score_word("TENNIS"))
print(score_word("EYES"))
print(score_word("BELLY"))
print(score_word("COMA"))
print(score_word("EXIT"))
print(score_word("MACHINE"))
print(score_word("HUSKY"))
print(score_word("PERIOD"))

player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

player_to_points = {}
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points
print(player_to_points)

def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word)
    else:
        player_to_words[player] = [word]

def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

play_word("player3", "PYTHON")
play_word("wordNerd", "CODE")
play_word("Lexi Con", "SCRABBLE")
play_word("Prof Reader", "PYTHON")

update_point_totals()
print(player_to_points)
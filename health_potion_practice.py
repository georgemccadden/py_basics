import random

# This is the introductory logic for a title page of a video game. It starts by showing the player what their starting health is and it allows the player to choose the difficulty of the game.

player_health = 50

# The game difficulty affects the player's health whenever it comes in contact with a potion. As the game increases in difficulty the less the player's health becomes increased by when the potion is consumed by the player.

game_difficulty = 1

potion_health = int(random.randint(25, 50) / game_difficulty)
gplayer_health = player_health + potion_health

print(player_health)


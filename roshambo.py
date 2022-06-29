import random


class Player:
	def __init__(self, player_name, roshambo_value, win, lose):
		self.player_name = player_name
		self.roshambo_value = roshambo_value
		self.wins = win
		self.losses = lose

	def __str__(self):
		return f"{self.player_name}: {self.roshambo_value}"


class Bart(Player):
	def __init__(self, player_name, roshambo_value, win, lose):
		Player.__init__(self, player_name, roshambo_value, win, lose)
		self.player_name = "Bart"

	def generateRoshambo(self):
		self.roshambo_value = "rock"
		return self.roshambo_value


class Lisa(Player):
	def __init__(self, player_name, roshambo_value, win, lose):
		Player.__init__(self, player_name, roshambo_value, win, lose)
		self.player_name = "Lisa"

	def generateRoshambo(self):
		options = ["rock", "paper", "scissors"]
		self.roshambo_value = random.choice(options)
		return self.roshambo_value


def play(play_ob, opp_ob, game_session):
	if play_ob.roshambo_value == opp_ob.roshambo_value:
		game_session += 1
		print(f"---> Draw!")

	elif play_ob.roshambo_value == "rock" and opp_ob.roshambo_value == "paper":
		play_ob.losses += 1
		opp_ob.wins += 1
		game_session += 1
		print(f"---> {opp_ob.player_name} wins!")

	elif play_ob.roshambo_value == "rock" and opp_ob.roshambo_value == "scissors":
		play_ob.wins += 1
		opp_ob.losses += 1
		game_session += 1
		print(f"---> {play_ob.player_name} wins!")

	elif play_ob.roshambo_value == "paper" and opp_ob.roshambo_value == "rock":
		play_ob.wins += 1
		opp_ob.losses += 1
		game_session += 1
		print(f"---> {play_ob.player_name} wins!")

	elif play_ob.roshambo_value == "paper" and opp_ob.roshambo_value == "scissors":
		play_ob.losses += 1
		opp_ob.wins += 1
		game_session += 1
		print(f"---> {opp_ob.player_name} wins!")

	elif play_ob.roshambo_value == "scissors" and opp_ob.roshambo_value == "rock":
		play_ob.losses += 1
		opp_ob.wins += 1
		game_session += 1
		print(f"---> {opp_ob.player_name} wins!")

	elif play_ob.roshambo_value == "scissors" and opp_ob.roshambo_value == "paper":
		play_ob.wins += 1
		opp_ob.losses += 1
		game_session += 1
		print(f"---> {play_ob.player_name} wins!")

	print(f"{play_ob.player_name} wins: {play_ob.wins}/{game_session}, total lose: {play_ob.losses}/{game_session}")
	print(f"{opp_ob.player_name} wins: {opp_ob.wins}/{game_session}, total lose: {opp_ob.losses}/{game_session}")

	return game_session


def main():
	print("Roshambo Game\n")
	player_name = input("Enter your name: ")
	play_ob = Player(player_name, "", 0, 0)
	print("\nHint 1: Bart's Roshambo is always rock")
	print("Hint 2: Lisa's Roshambo is selected by random\n")
	while True:
		choose_opponent = input("Would you like to play against Bart or Lisa? (b/B or l/L): ").lower()

		if choose_opponent == "b":
			opp_ob = Bart("", "", 0, 0)
			break
		elif choose_opponent == "l":
			opp_ob = Lisa("", "", 0, 0)
			break
		else:
			print("Invalid choice. Try again.")
			continue

	game_session = 0

	while True:
		play_value = input("\nRock, paper, or scissors? (r/p/s): ").lower()
		if play_value not in ("r", "p", "s"):
			print("Invalid choice. Try again.")
			continue
		if play_value == "r":
			play_ob.roshambo_value = "rock"
		elif play_value == "p":
			play_ob.roshambo_value = "paper"
		elif play_value == "s":
			play_ob.roshambo_value = "scissors"

		opp_ob.roshambo_value = opp_ob.generateRoshambo()

		print()
		print(play_ob)
		print(opp_ob)

		session = play(play_ob, opp_ob, game_session)
		game_session = session

		another_round = input("\nPlay again? (y/n) ").lower()
		if another_round == "y":
			continue
		else:
			break

	print("Thanks for playing!")


if __name__ == "__main__":
	main()

# def centered_average_1(arr):
#     highest = 0
#     lowest = 0
#     total = 0

#     for i in arr:
#         if i < lowest:
#             lowest = i
#         if i > highest:
#             highest = i
#         total += i

#     total -= highest
#     total -= lowest
#     return total // (len(arr) - 2)


# print(centered_average_1([1, 6, 2, 9, 4, 3, 8, 4, 10]))


# def centered_average_2(arr):
#     arr.sort()
#     temp_array = arr[1:-1]
#     # total = 0
#     # for i in arr:
#     #     total += i
#     # return total // len(temp_arr)
#     return sum(temp_array) // len(temp_array)


# centered_average_2([1, 6, 2, 9, 4, 3, 8, 4, 10])
# print(centered_average_2([1, 6, 2, 9, 4, 3, 8, 4, 10]))


# def centered_average(arr):
#     arr.remove(min(arr))
#     arr.remove(max(arr))
#     return sum(arr) // len(arr)


# def double(i):
#     i *= 2
#     return i  # Will not return a dbled value...ints are passed by value, not reference, therefore immutable


# num = 10
# double(num)

# print(num)
import random


class Opponent:

    def __init__(self, name):
        self.name = name
        self._move_choices = ["r", "p", "s"]

    def get_move(self):
        return random.choice(self._move_choices)


class RockOpponent(Opponent):
    def __init__(self, name):
        self.name = name
        self._move_choices = ["r", "r", "r", "r", "r", "r", "r", "p", "s"]


d = {"rp": -1, "rs": 1, "sp": 1, "sr": -1, "pr": 1, "ps": -1}


# Def a function that takes a player and CPU move and returns the win status
# 1 - win, 0 - tie, -1 - loss
def calculate_rps(player_move, cpu_move):
    if player_move == cpu_move:
        return 0
    else:
        return d[player_move + cpu_move]


wins = 0
losses = 0
ties = 0
move_choices = ["r", "p", "s"]

# o = RockOpponent()

# Build a REPL command loop
while True:
    cmd = input("Type r/p/s -> ")
    # Calculate CPU move
    cpu_move = o.get_move()
    # Prompt the player to input r/p/s
    # Evaluate the results based on computer command
    # Check for input validity
    if cmd in move_choices:
        results = calculate_rps(cmd, cpu_move)
        if results == 1:
            # WIN
            wins += 1
            result_name = "win!"
        elif results == 0:
            # TIE
            ties += 1
            result_name = "tie."
        elif results == -1:
            # LOSE
            losses += 1
            result_name = "lose."
        print(f"\nComputer picks {cpu_move}. You {result_name}")
    elif cmd == "q":
        # If the player types 'q', quit the game
        print("Goodbye!")
        break
    else:
        print("I did not understand that command.")
        # If input is not valid, print an error message and loop
    print(f"{wins} - {losses} - {ties}")
    # Display the results and score
    # Loop

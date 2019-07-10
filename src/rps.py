# import random

# wins = 0
# losses = 0
# ties = 0

# # Build a REPL command loop
# while True:
#     cmd = input("Type r/p/s -> ")
#     # Calculate CPU move
#     cpu_move = random.choice(["r", "p", "s"])
#     # Prompt the player to input r/p/s
#     # Evaluate the results based on computer command
#     # Check for input validity
#     if cmd == "r":
#         if cpu_move == "r":
#             # TIE
#             ties += 1
#             print(f"Computer picks {cpu_move}. You tie.")
#         elif cpu_move == "p":
#             # LOSE
#             losses += 1
#             print(f"Computer picks {cpu_move}. You lose.")
#         elif cpu_move == "s":
#             # WIN
#             wins += 1
#             print(f"Computer picks {cpu_move}. You win!")
#     elif cmd == "p":
#         if cpu_move == "p":
#             # TIE
#             ties += 1
#             print(f"Computer picks {cpu_move}. You tie.")
#         elif cpu_move == "s":
#             # LOSE
#             losses += 1
#             print(f"Computer picks {cpu_move}. You lose.")
#         elif cpu_move == "r":
#             # WIN
#             wins += 1
#             print(f"Computer picks {cpu_move}. You win!")
#     elif cmd == "s":
#         if cpu_move == "s":
#             # TIE
#             ties += 1
#             print(f"Computer picks {cpu_move}. You tie.")
#         elif cpu_move == "r":
#             # LOSE
#             losses += 1
#             print(f"Computer picks {cpu_move}. You lose.")
#         elif cpu_move == "p":
#             # WIN
#             wins += 1
#             print(f"Computer picks {cpu_move}. You win!")
#     elif cmd == "q":
#         # If the player types 'q', quit the game
#         print("Goodbye!")
#         break
#     else:
#         print("I did not understand that command.")
#         # If input is not valid, print an error message and loop
#     print(f"{wins} - {losses} - {ties}")
#     # Display the results and score
#     # Loop


##### DRY ######
import random


# Def a function that takes a player and CPU move and returns the win status
# 1 - win, 0 - tie, -1 - loss
def calculate_rps(player_move, cpu_move):
    d = {
        "rp": -1,
        "rs":  1,
        "sp":  1,
        "sr": -1,
        "pr":  1,
        "ps": -1
    }
    if player_move == cpu_move:
        return 0
    else:
        return d[player_move + cpu_move]


wins = 0
losses = 0
ties = 0

move_choices = ["r", "p", "s"]


# Build a REPL command loop
while True:
    cmd = input("Type r/p/s -> ")
    # Calculate CPU move
    cpu_move = random.choice(move_choices)
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

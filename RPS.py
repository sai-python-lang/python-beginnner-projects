import random

# RANDOM provides functions to generate pseudo random number for various distributions

def play_game():
    options = ["rock", "paper", "scissors"]
    user_wins = 0
    computer_wins = 0

    print("Welcome to Rock, Paper, Scissors!😁")
    
    while True:
      
        # 1. Get User Input
      
        user_input = input("\nType Rock/Paper/Scissors or 'Q' to quit: ").lower().strip()
        
        if user_input == "q":
            break
            
        if user_input not in options:
            print("Invalid input! Please choose Rock, Paper, or Scissors.")
            continue

        # 2. Computer makes a choice
      
        computer_pick = random.choice(options)
      
      # [random.choice] is a sequence randome operation that return element from non empty sequence 
      
        print(f"Computer picked: {computer_pick}.")

        # 3. Determine the winner
      
        if user_input == computer_pick:
            print("It's a tie!")
        elif (user_input == "rock" and computer_pick == "scissors") or \
             (user_input == "paper" and computer_pick == "rock") or \
             (user_input == "scissors" and computer_pick == "paper"):
            print("You won!")
            user_wins += 1
        else:
            print("You lost!")
            computer_wins += 1

        print(f"Score - You: {user_wins} | Computer: {computer_wins}")

    print("\nFinal Result:")
    print(f"You won {user_wins} times.")
    print(f"The computer won {computer_wins} times.")
    print("Thanks for playing!")

if __name__ == "__main__":
  
  # this line acts as a safety guard for the code inside so that it runs only when python script is directly executed 
  # and it prevents imports as a module simply
  
    play_game()

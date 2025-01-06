#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


def main():
    print("Welcome to the Go Fish Game!")  # Welcome message

    human_name = None
    while not human_name:
        try:
            # Ask for the human player's name
            human_name_input = input("Please enter your name: ").strip()
            if not human_name_input or not human_name_input.isalpha():
                raise ValueError("Name must contain only alphabetic characters and cannot be empty.")
            human_name = human_name_input  # Assign only if the input is valid
        except ValueError as ve:
            print(f"Input error: {ve}")

    # Create human and CPU players
    human = Player(human_name)  
    cpu = Player("CPU")  

    # Create the game instance
    game = GoFishGame()
    game.add_player(human)
    game.add_player(cpu)

    try:
        # Setup the game
        game.setup_game()

        # Display initial hands
        print(f"\nWelcome, {human.name}! You will be playing against {cpu.name}.")
        print(f"{human.name}'s Initial Hand: {', '.join(str(card) for card in human.hand)}")
        print(f"{cpu.name}'s hand is hidden.")

        # Game loop
        turn = 0
        valid_ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        while not game.is_game_over():
            try:
                if turn % 2 == 0:  # Human's turn
                    print(f"\n{human.name}'s Turn:")
                    print(f"Your Hand: {', '.join(str(card) for card in human.hand)}")

                    # Get a valid rank from the human
                    while True:
                        rank_to_ask = input("Enter the rank you want to ask for (e.g., '5', 'Ace', 'Queen'): ").strip()
                        if rank_to_ask in valid_ranks and any(card.rank == rank_to_ask for card in human.hand):
                            break
                        print("Invalid rank! Please choose a valid rank from your hand.")
                    
                    game.player_ask_for_rank(human, cpu, rank_to_ask)
                else:  # CPU's turn
                    print(f"\n{cpu.name}'s Turn:")
                    if cpu.hand:
                        # Determine the most frequent rank in the CPU's hand
                        rank_counts = {card.rank: sum(1 for c in cpu.hand if c.rank == card.rank) for card in cpu.hand}
                        rank_to_ask = max(rank_counts, key=rank_counts.get)
                        print(f"{cpu.name} asks: Do you have any {rank_to_ask}s?")
                        game.player_ask_for_rank(cpu, human, rank_to_ask, is_cpu=True)
                    else:
                        print(f"{cpu.name} has no cards to play and skips the turn.")
            except Exception as e:
                print(f"An error occurred during the turn: {e}")
                continue  # Skip to the next turn if an error occurs

            turn += 1

        # End the game
        print("\nGame Over!")
        game.show_player_books()
        game.determine_winner()

    except RuntimeError as re:
        print(f"Game error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for playing Go Fish!")

            
    


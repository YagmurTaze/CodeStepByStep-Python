def main():
    print("This program allows you to guess random numbers.")
    print("I will think of a number between 1 and 100")
    print("and you will try to guess it.")
    print("After each guess, I will give you a clue about")
    print("whether the correct number is higher or lower.")

    total_games = 0
    total_guess = 0
    best_game = 100
    start_game(total_games, total_guess, best_game)

def start_game(total_games, total_guess, best_game):
    play = 'y'
    while play.startswith("y") or play.startswith("Y"):
        print()
        print("I'm thinking of a number between 1 and 100...")
        num = random.randint(1, 101)
        count = 0
        guess = 0

        while guess != num:
            guess = int(input("Your guess? "))
            if guess < num:
                print("It's higher.")
            if guess > num:
                print("It's lower.")
            count += 1

        if count < best_game:
            best_game = count
        
        if count == 1:
            print("You got it right in " + str(count) + " guess!")
        else:
            print("You got it right in " + str(count) + " guesses!")
        total_games += 1
        total_guess += count

        play = input("Do you want to play again? ")
   
    print_stats(total_games, total_guess, best_game)

def print_stats(total_games, total_guess, best_game):
    print()
    print("Overall results:")
    print("Total games   =", total_games)
    print("Total guesses =", total_guess)
    print("Guesses/game  =", round(total_guess / total_games,1))
    print("Best game     =", best_game)

main()

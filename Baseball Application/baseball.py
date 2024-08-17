import functions as TOME

def get_at_bat_results(team_name, inning, results, current_score, batting_order):
    num_outs = 0
    at_bat = 1
    batter_index = 0 # Start with the first batter in the lineup

    while num_outs < 3:

        # Get the batter's name from the batting order dictionary
        batter_name = batting_order[batter_index % 9] # Cycle the lineup 

        if at_bat == 1:
            suffix = "st"
        elif at_bat == 2:
            suffix = "nd"
        elif at_bat == 3:
            suffix = "rd"
        else:
            suffix = "th"

        #Get result of AB for the current batter 
        print(f"\nInning {inning} - {team_name} Turn")
        print(f"At-Bat: {at_bat}{suffix} AB")
        result = input(f"Enter the result of {batter_name}'s at-bat (e.g., Single, Strikeout): ").strip()
        results[inning][team_name].append(f"{batter_name}: {result}")

        #Update Outs

        while True:
            try:
                num_outs = int(input("Enter the current number of outs (0-3): "))
                if 0 <= num_outs <= 3:
                    break
                else:
                    print("Number of outs must be between 0 and 3.")
            except:
                print("Invalid input. Please enter a valid number.")


        #Check for runners scored

        while True:
            runners = input("Did any runners score (Y/N)?: ").strip().upper()
            if runners == "Y":
                while True:
                    try:
                        runs = int(input("Enter the number of runs scored: "))
                        current_score += runs
                        print(f"{runs} run(s) scored for {team_name}. Total score: {current_score}")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number for runs scored.")
                break
            elif runners == "N":
                break
            else:
                print("Please enter either Y (yes) or N (no).")

        if num_outs >= 3:
            break

        batter_index += 1
        at_bat += 1

    return num_outs, current_score

# Printing the results
def print_results(results, team1, team2):
    for inning in results:
        print(f"Inning {inning}:")
        print(f"  {team1} AB Results: {results[inning][team1]}")
        print(f"  {team2} AB Results: {results[inning][team2]}")
        print()

def main():

    TOME.print_logo()

    print()
    Team1 = input("Please enter Team 1: ")
    print()
    Team2 = input("Please enter Team 2: ")
    print()

    #initialize the batting order for each team

    team1_batting_order = TOME.get_batting_order(Team1)
    team2_batting_order = TOME.get_batting_order(Team2)


    # Initialize results dictionary
    results = {inning: {Team1: [], Team2: []} for inning in range(1, 10)}

    # Initialize scores
    team1_score = 0
    team2_score = 0


    for inning in range(1, 10):  # Assuming a 9-inning game
        print(f"Inning {inning} - {Team1}'s turn")
        num_outs, team1_score = get_at_bat_results(Team1, inning, results, team1_score, team1_batting_order)

        if num_outs < 3:
            print(f"{Team1} still has outs remaining for inning {inning}")
        else:
            print(f"{Team1} have 3 outs. It's now time for {Team2} to bat!")

        print(f"Inning {inning} - {Team2}'s turn")
        num_outs, team2_score = get_at_bat_results(Team2, inning, results, team2_score, team2_batting_order)

        if num_outs < 3:
            print(f"{Team2} still has outs remaining for inning {inning}")
        else:
            print(f"{Team2} have 3 outs. Moving to next inning")

    # Print the results at the end
    print_results(results, Team1, Team2)
    print(f"Final score: {Team1}: {team1_score}, {Team2}: {team2_score}")

if __name__ == "__main__":
    main()


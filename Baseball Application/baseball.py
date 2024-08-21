import functions as TOME

def get_at_bat_results(team_name, inning, results, current_score, batting_order):
    num_outs = 0
    at_bat = 1
    batter_index = 0 # Start with the first batter in the lineup
    batting_order_list = list(batting_order.values())  # Convert to list for indexing

    while num_outs < 3:

        # Get the batter's name from the batting order dictionary
        
        batter_name = batting_order_list[batter_index % len(batting_order_list)] # Cycle the lineup 


        #Get result of AB for the current batter 

        print(f"\nInning {inning} - {team_name} Turn")
        print(f"{at_bat}{TOME.get_suffix(at_bat)} AB")

        while True:
            result = input(f"Enter the result of {batter_name}'s at-bat (H for help): ").strip().lower()
            if result in TOME.results_list:
                break
            elif result == "h":
                TOME.get_results_list()
                print()
            
            else:
                print("Error: Please enter a valid result (H for help).")


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
    TOME.select_team()

    print()
    while True:

        Team1 = input("Please select Team 1: ")
        if Team1 in TOME.american_league_teams or Team1 in TOME.national_league_teams:
            break
        else:
            print("Please select an MLB team from the provided list.")
        print()

    while True:

        Team2 = input("Please select Team 2: ")
        if Team2 in TOME.american_league_teams or Team2 in TOME.national_league_teams:
            if Team2 != Team1:
                break
            else:
                print("The second team cannot be the same as the first.")
        else:
            print("Please select an MLB team from the provided list.")
        print()

    # Testing Data 
    # Team1 = "Blue Jays"
    # Team2 = "Red Sox"

    while True:

        pitch_logging = input("Would you like to enable individual pitch-logging in your session?(Y/N): ").upper()
        print()
        if pitch_logging == "Y":
            pitch_logging = True
            break
        elif pitch_logging == "N":
            pitch_logging = False
            break
        else:
            print("Data-entry error: Please choose a valid option (Y or N): ")

        

    #initialize the batting order for each team

    team1_batting_order = TOME.get_batting_order(Team1)
    team2_batting_order = TOME.get_batting_order(Team2)

    # Testing Data
    # team1_batting_order = {i: f"Player{i}" for i in range(1, 10)}
    # team2_batting_order = {i: f"Player{i}" for i in range(1, 10)}


    # Initialize results dictionary
    results = {inning: {Team1: [], Team2: []} for inning in range(1, 10)}

    # Initialize scores
    team1_score = 0
    team2_score = 0


    for inning in range(1, 10):  # Assuming a 9-inning game
        print(f"Inning {inning} - {Team1}'s turn")
        if pitch_logging:
            TOME.ab_pitch_count()

        num_outs, team1_score = get_at_bat_results(Team1, inning, results, team1_score, team1_batting_order)

        if num_outs < 3:
            print(f"{Team1} still has outs remaining for inning {inning}")
        else:
            print(f"{Team1} have 3 outs. It's now time for {Team2} to bat!")

        print(f"Inning {inning} - {Team2}'s turn")
        if pitch_logging:
            TOME.ab_pitch_count()

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


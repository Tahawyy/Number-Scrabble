# The list that the players will choose from
scrabble = [1, 2, 3, 4, 5, 6, 7, 8, 9]
run = True
# index(0) is player1 list and index(1) is player2 list , we will use it to check the win condition
player_picked = [[], []]

#The function that checks if there is a winner or not
def is_winner(player_picked):
        #takes the first number and loops inside the list to check it with all the other numbers
        for i in range (0, len(player_picked)-2):
                 #takes the second number and loops inside the list to check it with all the other numbers
                for j in range (i+1 , len(player_picked)-1):
                    #takes the third number and loops inside the list to check it with all the other numbers
                    for k in range (j+1 , len(player_picked)):
                        # check if their sum is 15
                        if player_picked[i] + player_picked[j] + player_picked[k] ==15:

                            return True

# The function that checks if it's draw
def Draw_game():
    # all numbers are taken without a winner
    if len(scrabble) == 0:
            print("  Draw Game :( ")

            return False


# The game loop
while run :

    # for loop to switch between player 1 and player2
    for player in [1, 2]:
        # if  the game is draw
        if Draw_game() == False:
            # break the game loop
            run = False

        # player will choose a number
        inp = int(input("\nPlayer " + str(player) + " enter a number: "))
        # if the input is not in the scrabble list
        while inp not in scrabble:
            # the player will choose another number until the number is in scrabble list
            inp = int(input("\nInvalid input player " + str(player) + " , enter another number : "))
        #the number that the player choose is added to his list
        player_picked[player-1].append(inp)
        #the number that the player choose is removed from the scrabble list because the number cannot be choosen twice
        scrabble.remove(inp)

        # The remaining avaliable numbers for the player to choose
        print("\nRemaining of the list is : " , list(scrabble))

        # if the player's list contains 3 numbers we will check if their sum is 15
        if len(player_picked[player-1])==3:
            # check if their sum is 15
            if sum(player_picked[player-1]) == 15:
                # if their sum is 15 the game stops and a player wins
                print("\n \nPlayer " + str(player) + " Wins !!!")
                # break the game loop
                run = False
                break


        # if both players chose more than 3 numbers
        elif len(player_picked[player-1])>3:
            # call the function which loops inside the loop for any 3 numbers to check their sum if equal to 15
            if  is_winner(player_picked[player-1]) == True:
                print("\n \nPlayer " + str(player) + " Wins !!!")
                run = False
                break
# programming coursework OMI Game[IMANDI]

import random  # this will import random module from library

player = 1     # player 1 is user , player 0 is the robo(computer)
# user = []    # this is the list used to stored user shuffled deck of cards created using carddeck A (will be used to print users deck whenever needed)
# user1 = []   # this is the list  used for calculations which has been created from shuffled cards in carddeckB used by user1
# robo = []   # this is the list used to stored robo shuffled deck of cards created using carddeck A (will be used to print cards whenever needed)
# robo1 = []  # this is the list used for calculations which has been created from shuffled cards in carddeckB used by robo1
tricklead = ""  # this is used to store the player who will be leading the trick
playagain = "y" #this used to see if the user wishes to play for another 8 tricks
trump = ""  # stores the trump suit selected by user or robo depending on the player

carddeckA = ["♦A", "♦K", "♦Q", "♦J", "♦10", "♦9", "♦8", "♦7",
             "♥A", "♥K", "♥Q", "♥J", "♥10", "♥9", "♥8", "♥7",
             "♠A", "♠K", "♠Q", "♠J", "♠10", "♠9", "♠8", "♠7",
             "♣A", "♣K", "♣Q", "♣J", "♣10", "♣9", "♣8",
             "♣7"]  # this the deck of cards which are been used to play the game which is visible to players
carddeckB = ["♦.14", "♦.13", "♦.12", "♦.11", "♦.10", "♦.9", "♦.8", "♦.7",
             "♥.14", "♥.13", "♥.12", "♥.11", "♥.10", "♥.9", "♥.8", "♥.7",
             "♠.14", "♠.13", "♠.12", "♠.11", "♠.10", "♠.9", "♠.8", "♠.7",
             "♣.14", "♣.13", "♣.12", "♣.11", "♣.10", "♣.9", "♣.8",
             "♣.7"]  # this is the deck of cards which will be used for calculations and this deck of cards is not visible to players
#  carddeckA and carddeckB have same elements but the only difference is carddeckB has a dot between the suit and number
#  this dot in carddeckB is only because im using  the split function

# now we have to implement the shuffling algorithm for shuffling of cards before starting the game (TASK1)....

# now im going to implement a function for shuffling which will use the bubble sort method  of swapping the indexes
while playagain == "y": #this is y at beginning because he is starting to play 8 tricks
    user = []  # this is the list used to stored user shuffled deck of cards created using carddeck A (will be used to print users deck whenever needed)
    user1 = []  # this is the list  used for calculations which has been created from shuffled cards in carddeckB used by user1
    robo = []  # this is the list used to stored robo shuffled deck of cards created using carddeck A (will be used to print cards whenever needed)
    robo1 = []  # this is the list used for calculations which has been created from shuffled cards in carddeckB used by robo1
    def shuffledeck(carddeckA,carddeckB):  #creating the shuffling function taking two carddecks as the parameters since both should be shuffled
        for index in range(len(carddeckA) - 1, 0,-1):  # this for loop will access each element of my two  lists, also here i hve said decklength -1 is because there is 32 elements but in python since we have a 0 element it ends at 31
            element = random.randint(0, index + 1)  # this is a randomly chosen element to do the swapping
            carddeckA[index], carddeckA[element] = carddeckA[element], carddeckA[index]
            carddeckB[index], carddeckB[element] = carddeckB[element], carddeckB[index]
        # return carddeckA, carddeckB  # carddeckA and carddeckB  will now  have the shuffled deck of cards


    shuffledeck(carddeckA, carddeckB)  # this calls the function shuffledeck
    # print("the shuffled deck of cards for user to see is :", carddeckA)
    # print("the shuffled deck of cards for me to see is :", carddeckB)

    print("Welcome to OMI")
    # trump selection part
    # now since we need to select the trump we give 4 cards to the player

    if player == 1:  # if user is going to select trump first
        for portion in range(0,4):  # this for loop will generate 4 cards from the shuffled deck of cards and give to the user
            user.append(carddeckA[portion])  # this will add 4 cards from carddeckA  to the user  list
            user1.append(carddeckB[portion])  # this will add 4 cards from carddeckB to user1 list
        print(user) #this displays first 4 cards of user deck
        print("")  # this will display the cards on the user list with spaces
        tricklead = "robo"  # this stores robo in tricklead which means that robo will be leading the trick

        #  implementation of the trump selection part.......
        # this will take the trump suit from player[user]
        trump = input("please enter the trump suit : Enter a ♦ to choose Suit Diamonds,a ♥ to choose suit Hearts ,a ♣ to choose suit Clubs , a ♠ to choose suit Spades ")

        # these lines  will print the trump suit according to symbol chosen by user

        if trump == "♦":
            print("you have chosen  trump suit as  Diamonds ")

        elif trump == "♥":
            print("you have  chosen trump suit as Hearts")

        elif trump == "♣":
            print("you have  chosen  trump suit as  Clubs")

        elif trump == "♠":
            print("as chosen trump suit as Spades")
        else:
            print("please enter a valid trump")    # if anything other than one of the 4 symbols printed, then asks user to again put a valid trump
            trump = str(input("please enter the trump suit : Enter a ♦ to choose Suit Diamonds,a ♥ to choose suit Hearts ,a ♣ to choose suit Clubs , a ♠ to choose suit Spades "))

        # now that trumps were selected by user ,rest of the cards are shared equally
        print("the trump i selected:", trump)

        for portion in range(4, 8):  # this for loop will generate the next 4 cards from the shuffled deck of cards
            robo.append(carddeckA[portion])  # the next 4 cards from list carddeckA is put to the robo list
            robo1.append(carddeckB[portion])  # the next 4 cards from list carddeckB is put to the robo1 list

        for portion in range(8, 12):  # this for loop will generate next  4 cards from the shuffled deck of cards
            user.append(carddeckA[portion])  # give the  next set of 4 cards from list carddeckA to user list
            user1.append(carddeckB[portion])   # gives the next set of 4 cards from list carddeckB to user1 list
        print(user)
        print("")  # this will display as the rest of the 4 cards on the user deck

        for portion in range(12,16):  # this for loop will generate the last set of  4 cards from the shuffled deck of cards
            robo.append(carddeckA[portion])  # this will add those selected cards to the robo  list from carddeckA
            robo1.append(carddeckB[portion])  # this will add the last  4 cards from carddeckB to robo1



    #  if player is not the user but robo then below else runs

    else:
        # so now since robo is stating trumps, first 4 cards should be given to robo(computer)
        for portion in range(0, 4):  # this for loop will generate 4 cards from the shuffled deck of cards
            robo.append(carddeckA[portion])   # this will add 4 cards from carddeckA  to the robo  list
            robo1.append(carddeckB[portion])  # this will add 4 cards from carddeckB to robo1 list

        tricklead = "user"  # user gets stored into tricklead


        # this function is made to display the trump suit selected by the robo(computer)
        def trumpsuit(trump):
            print("trump suit selected is :", trump)

        #  robo[0][0] means first element suit
        #  robo[0][1] means first element number
        if robo[0][0] == robo[1][0] == robo[2][0] == robo[3][0]:  # checks if all 4 card suits are the same by accessing the suits of 4 cards
            trump = robo[1][0]  # since all 4 suits are equal trump suit can be assigned to any card suit
            trumpsuit(trump)  # function will print the trump selected

        # there are different combinations in which 3 card suits can be equal. The 3 elifs below checks for all combinations

        elif robo[1][0] == robo[2][0] == robo[3][0]:  # checks if 3 card suits  are equal (in the first case checks if first ,second and third element suit equal)
            trump = robo[2][0]  # assigns trump suit to any of these three card suit since all three have same suit
            trumpsuit(trump)
        elif robo[0][0] == robo[1][0] == robo[2][0]:  # also checks if 3 card suits are equal but in this case checks if the first,second and third card suit  equal
            trump = robo[0][0]
            trumpsuit(trump)
        elif robo[0][0] == robo[2][0] == robo[3][0]:  # checks if the first , third and fourth cards have same suit
            trump = robo[3][0]  # if they do assigns trumps to the suit of one of these cards
            trumpsuit(trump)

        # there are 3 cases in which two equal suits can occur

        # case 1 for 2 equal suits - [first card suit=second card suit and third card suit=fourth card suit]

        elif robo[0][0] == robo[1][0] and robo[2][0] == robo[3][0]:  # checks for two equal suits now (checks if ist and second card have same suit  and if third and fourth card have same suit )

            # if there is two equal suits we must check if one suit has an ace. If one equal suit has ace , we must put trumps as the second equal suit

            if "A" in robo[0][1] and robo[1][1]:  # if ace is in the first card and second card that means we have to choose the suit of the third and fourth card as trumps
                trump = robo[3][0]  # here trump can be  either third card's suit or fourth card's suit since both equal
                trumpsuit(trump)
            elif "A" in robo[2][1] and robo[3][1]:  # if ace is found in the third and fourth card we must make trumps the first or second card suit
                trump = robo[1][0]
                trumpsuit(trump)
            else:
                trump = robo[0][0]  # assigns trump suit to the first card suit
                trumpsuit(trump)

        # there also  cases where there is two cards of same suit and other two card suits are different

        # case 1 for one  equal suits and two cards different suits [ checks if first and second cards same suit and third and fourth contain a different card suit
        if robo[0][0] == robo[1][0] and robo[2][0] != robo[3][0]:  # in here we take the first and second card suit same but the third and fourth cards have different suit
            trump = robo[1][0]  # assigns trumps to the equal card suit
            trumpsuit(trump)
        elif robo[0][0] != robo[1][0] and robo[2][0] == robo[3][0]:  # here we check if the first two cards have different suits and second and third cards have same suit
            trump = robo[3][0]  # assigns trumps to the equal card suit
            trumpsuit(trump)

        # case 2 for two  equal suits- [first card suit=fourth card suit same and second and third  card suit same]

        elif robo[0][0] == robo[3][0] and robo[1][0] == robo[2][0]:

            # if there is two equal suits, again we check if one equal suit has ace if so we assign trumps to the other equal suit

            if "A" in robo[0][1] and robo[3][1]:
                trump = robo[2][0]
                trumpsuit(trump)
            elif "A" in robo[1][1] and robo[2][1]:
                trump = robo[3][0]
                trumpsuit(trump)
            else:
                trump = robo[0][0]
                trumpsuit(trump)

        # case 2 for one  equal suit and two cards different suits [checks if first and fourth card suit same but second and third card suit different]

        elif robo[0][0] == robo[3][0] and robo[1][0] != robo[2][0]:  # checks if first and fourth card same suit but second and third card different suit
            trump = robo[0][0]  # assigns trumps to the equal card suit
            trumpsuit(trump)
        elif robo[0][0] != robo[3][0] and robo[1][0] == robo[2][0]:  # checks if the first and fourth card suit not equal and second and third card suit equal
            trump = robo[1][0]  # assigns trumps to the equal card suit
            trumpsuit(trump)

        # case 3 for  two equal suits -[first card suit=third card suit and second  card suit= fourth card suit]
        elif robo[0][0] == robo[2][0] and robo[1][0] == robo[3][0]:

            # again if we have two equal suits we must check if one of the equal suits contain an ace if so we must assign trumps to the suit which didnt contain ace

            if "A" in robo[0][1] and robo[2][1]:  # here we check if the first and second suit have an ace if so
                trump = robo[1][0]  # assigns trumps to the other equal suit
                trumpsuit(trump)
            if "A" in robo[1][1] and robo[3][1]:  # here we check if the second and fourth card has an ace if so
                trump = robo[2][0]  # assigns trump suit to the other equal suit
                trumpsuit(trump)

            # case 3 for one equal suits and two cards with different suits [first and third card have same suit but second and fourth card have different suit]

        elif robo[0][0] == robo[2][0] and robo[1][0] != robo[3][0]:  # checks if first card and third card have same suit and second and fourth card have different suit
            trump = robo[2][0]  # assigns trumps to the equal card suit
            trumpsuit(trump)
        elif robo[0][0] != robo[2][0] and robo[1][0] == robo[3][0]:  # checks if first and third card have different suit and second and fourth card have same suit
            trump = robo[3][0]  # assigns trumps to the equal card suit
            trumpsuit(trump)

        # now that the trumps have been selected by robo we need to share equally the rest of the cards.....

        for portion in range(4, 8):  # this for loop will generate next  4 cards for user
            user.append(carddeckA[portion])  # this will add those selected cards from carddeckA to the user  list
            user1.append(carddeckB[portion])  # this will add the next 4 cards from carddeckB to user1 list
        print(user)
        print("")  # this will display the cards on the user list with spaces

        for portion in range(8, 12):  # this for loop will generate the last set of 4 cards for the robo
            robo.append(carddeckA[portion])  # this will add next 4 cards of carddeckA to the robo  list
            robo1.append(carddeckB[portion])  # this will add next 4 cards of carddeckB to robo1 list

        for portion in range(12,16):  # this for loop will generate last  4 cards for user  from the shuffled deck of cards
            user.append(carddeckA[portion])  # this will add last set of 4 cards from carddeckA to the user  list
            user1.append(carddeckB[portion])  # this will add last set of 4 cards from carddeckB to user1 list
        print(user)
        print("")  # this will display the cards on the user list with spaces

    # now that all cards are shared equally the user and robo deck is printed


    print("your card deck is :", user)
    print("this trick is lead by:", tricklead)

    # game phase starts now ..........................

    print("Lets Play")
    tricks=1
    max = 0  # if there is two or more cards with same suit ,calculates which is greater
    robopoints = 0  # points of the robo(computer)
    userpoints = 0  # points of user(you)
    #cardfound=False
    for trick in range(8):  # this for loop will go for the 8 tricks
        print("Trick",tricks)

        suitfound = []  # this list is used to store cards if there is more than one card with a  similar suit
        large = ""
        card = []  # this is used to store the card which is been played currently (from user or robo list)

        card1 = []  # corresponding card found on user1 or robo1 list using index1
        usercard = ""  # this is card which the user enters during play
        print("your card deck is:", user)  # prints users deck for user to see
        print("the trump selected is:", trump)  # prints the trump selected

        if tricklead == "user":  # if the trick is lead by the user
            suit3 = ""

            # this while loop checks  if card entered by user is on the user deck
            cardfound = False  # this is to find whether the user has the entered card on his deck...
            x = True
            suit=""
            number3=""
            number=""
            while cardfound == False:  # initially cardfound is false because we need to find if card entered is in user deck
                while x == True:  #until user puts a valid card(crd on list ) this will loop
                    card = str(input(
                        " pick a card from deck to start playing"))  # user enters the card which he wishes to play with
                    if card in user:  # if card is there on users deck
                        x = False
                        index1 = user.index(card)  # it finds the index of the card you entered from the user list
                        card1 = user1[index1]  # with the index calculated as  index1 we are using that to locate the card which matches that index in user1 list

                        cardfound = True  # cardfound initialised to true because we found card on user deck
                        suit, number = card1.split(".")  # this will seperate the suit from the number by the dot

                        for index in range(len(robo1)):  # this for loop will be used to search through the robo list

                            if suit in robo1[index][0]:  # here im checking if the suit entered by user is available on robo deck of cards
                                suitfound.append(robo1[index])  # if similar suit found it will add to this list -suitfound
                        index3=0
                        if len(suitfound) >= 1:           # here im checking if there was one or more cards with similar suit
                            robocard = random.randrange(0, len(suitfound)) # this will give me a random index from number of elements of suitfound
                            if suitfound[robocard] in robo1:      # checks if the index calculated earlier card on suitfound list is in robo1 list
                                index3 = robo1.index(suitfound[robocard])  # finds the index of the randomly selected card of suitfound in the robo1 list
                                print(robo[index3])         # prints the card in robo list  corresponding to index3 calculated above
                            else:
                                print("please enter a valid card ") # if the card calculated by index was not found user has to enter a valid card again
                            suit3, number3 = suitfound[robocard].split(".")  # if the card from suitfound was found in robo1 list,that card will now get splitted between the suit and number
                            robo1.remove(suitfound[robocard])         # this will remove the card calculated using robocard from robo1 list
                            robo.remove(robo[index3])                 # this will remove the corresponding card of robo list  calculated from index3
                            user1.pop(user.index(card))               # pops the user card from the user list
                            user.remove(card)                          # this will remove the card user picked
                        else:
                            index4=0
                            robocard = random.randrange(0, len(robo))  # if there were no cards of similar suit then an index is randomly calculated from length of robo list
                            if robo[robocard] in robo:                  # if the card calculated from the index(robocard) is in the robo list
                                index4 = robo.index(robo[robocard])     # index of that card on robo list is saved onto index4
                                print("computer says :", robo[robocard])  # prints random card found from robo deck
                            suit3, number3 = robo1[index4].split(".")     # first finds the carresponding card of index4 and splits it between the dot
                            robo.remove(robo[robocard])                   # removes card in robo list calculated by index(robocard)
                            robo1.pop(index4)                              # pops the corresponding card of index4 ffrom robo1 list
                            user1.pop(user.index(card))                    # pops the coresponding card of the index found from card emtered by user
                            user.remove(card)                              # removes card entered by user from user list
                    else:
                        card = str(input("pick a card from deck to start playing"))  # if card user entered is not found on user deck he has to enter another card


            if suit3 == suit:  # if robo has a suit similar to user suit
                if int(number3) > int(number):  # checks if the number on card of robo is greater than users
                    robopoints += 2  # if its greater the robo (computer) wins the trick and gets two points
                    print("computer wins this trick")
                    tricklead = "robo"  # since robo has won the trick the next trick will be lead by robo(computer)
                else:
                    userpoints += 2  # if number on card of robo is smaller than the user ,user wins trick and he gets two points
                    print("you  win this trick")
                    tricklead = "user"  # since user has won this trick the next trick is lead by user(you)
            elif suit3 != suit:  # if robo doesnt have card with similar suit of robo
                if suit3 == trump:  # checks if robo has a trump
                    robopoints += 2  # robo (computer) wins the trick
                    print("computer wins this trick")
                    tricklead = "robo"  # since robo wins this trick the next trick is lead by robo(computer)
                else:
                    userpoints += 2  # if robo has not put a trump nor a card of similar suit
                    print("you win this trick")
                    tricklead = "user"  # since user wins this trick the next trick is lead by you(user)




        else:  # if the trick was lead by robo(computer) the below code runs

            cardindex = random.randint(0, len(robo1) - 1)  # finds a random index calculated using the lemgth of robo1 list
            print("robo puts card:", robo[cardindex])  # displays the card corresponding to the index calculated above

            suit, number = robo1[cardindex].split(".")  # seperates the suit and card level of the card of similar index in robo1 list
            robo1.remove(robo1[cardindex])              # removes the card from robo1 and robo list
            robo.remove(robo[cardindex])
            cardfound=False
            while cardfound == False:

                for index in range(len(user1)):  # this for loop is used to search through the user1 list

                    if suit in user1[index][0]:  # checks if the user has the same suit the robo entered
                        cardfound = True  # since we found a card this will be initialised to true
                suit1 = ""
                if cardfound == True:

                    usercard = str(input("please pick a card"))  # user(you) get to put a card
                    while usercard[0] != suit:  # loop runs if  the card you enterd doesnt have same suit as robo(computer)
                        usercard = str(input("please pick a card"))  # user(you) has to put a card from user deck

                    if usercard in user:  # if card entered by user is in the deck
                        temp = user1[user.index(usercard)]  # store the card in user1 thats the same as user
                        suit1, number1 = temp.split(".")    # split the card that was stored on the temporary variable
                        user1.pop(user.index(usercard))     # pops  card of the corresponding index calculated of the card entered by user from user1 list
                        user.remove(usercard)               # removes the card entered by user from user list
                    else:
                        print("please enter a valid card ")  # if card enetered by user was not in user list he has to put a card again
                        usercard = str(input("please pick a card"))
                # what happens in line 330-line343
                # cardfound is only becoming true if there is a card on user1 list which contains the same suit which robo entered
                # if cardfound becomes true that means theres a suit similar to robo1 so we need to get an inpjut from the user because we only checked if there was a card with similar suit we never inputted a card
                # once the uer has input a card (usercard) we have to check if that card contains same suit.
                # if it doesnt contain the same suit , we need to ask user to input again because we knw that there is a card in user which contains same card suit as robo
                # once we find that we must check if that card user inputted(usercard) is actually in the deck because user can put a card of same suit and that card also may not be in list.
                # if a card user enetered was found then we have to store the card from user1 list on a temporary variable before we pop it from that and remove the same card from user list

                else:  # if the card entered by user is not in user list he has to enter another card(shouldnt this else statement be directly under if usercard in user)

                    usercard = str(input("please pick a card"))

                    cardfound = False
                    while cardfound == False:
                        if usercard in user:
                            cardfound = True

                            index2 = user.index(usercard)    # stores the index calculated from finding position of card entered by user on the user list
                            suit1, number1 = user1[index2].split(".")
                            user1.pop(index2)     # pops card from user1 same index as the card found on user list
                            user.remove(usercard)  # removes the card user has entered

                        else:
                            usercard = str(input("please pick a card")) # if card entered by user was not found on user list user will have to pick another card

            if suit1 == suit:  # if user has a suit similar to robo suit

                if int(number1) > int(number):  # checks if the number on card of user is greater than the number on card of robo
                    userpoints += 2  # if its greater the user wins the trick and gets two points
                    print("you win this trick")
                    tricklead = "user"
                else:
                    robopoints += 2  # if number on card of user is smaller than the robo(computer) ,robo wins trick and he gets two points
                    print("computer win this trick")
                    tricklead = "robo"


            elif suit1 != suit:   # checks if the user card suit is not similar to robo suit
                if suit1 == trump:  # if user has put a card with the trump suit
                    userpoints += 2  # user wins the trick
                    print("you win this trick")
                    tricklead = "user"
                else:
                    robopoints += 2  # if robo has not put a trump nor a card of similar suit
                    print("computer wins this trick")
                    tricklead = "robo"
        tricks+=1
# once all 8 tricks are done we can see who the winner is .........

    if robopoints > userpoints:    # if computer(robo) points were higher than user points
        print("cmputer wins with ", robopoints)    #robo wins
    elif robopoints == userpoints: # checks if both users and robos points are same
        print("This a tie")       # it will be a tie
    else:
        print("you win with", userpoints)

    playagain = input("do you want to play again (y/n):")     # checks if user wants to start playing again
    rounds = True                                             # to start an infinte while loop to check if y or n is put
    while rounds == True:
        if playagain == "y":

            if player == 1:
                player = 0

                tricklead = "robo"
            else:
                player = 1
                tricklead = "user"
            rounds = False
        elif playagain == "n":
            break
        else:
            playagain = input("do you want to play again (y/n):")

from random import*
from time import*
timeStart = time()
playAgain = "y"
while playAgain == "y":
    print("")
    print("Hello and welcome to Jai's Triva!")

    rules = input("Do you want to see the rules? yes/no: ")

    if rules == "yes":
       print("")
       print("This is a multiple choice trivia game!")
       print("There will be five multiple choice questions")
       print("Each question will be worth 5 points")
       print("If you answer all questions correctly, you win the game")
       print("If you answer any question incorrectly, the game will automatically end!")
       print("Good luck and enjoy the game!")

    else:
        print("Ok, lets get you started with the first question!")

    points = 0
    print("")
    print("What is the capital of Australia? ")
    print("Sydney")
    print("Melbourne")
    print("Canberra")
    print("Ottawa")

    question1 = input("Please enter one of the answers stated above: ")

    if question1 not in ["Canberra","canberra"]:
        print("Sorry, but unfortunately you got the wrong answer!")
                      
    else:
        print("Congrats, you have gave the right answer")
        print("")
        print("This question didn't get you, but the other ones will!")
        points = points + 5

        
        print("")
        print("How many provinces are there in Canada? ")
        print("14")
        print("13")
        print("10")
        print("11")

        question2 = input("Please enter one of the answers stated above: ")

        if question2 not in ["10"]:
            print("Sorry, but your streak ends here!")
            print("Better luck next time")
            print("")
            

        else:
            print("")
            print("Wow, you are on a roll!")
            print("Lets hope you win!")
            points = points + 5

        
            print("")
            print("What is the name of the largest sea creature currently living?")
            print("Blue Whale")
            print("Whale Shark")
            print("Giant Octopus")
            print("Orca")

            question3 = input("Please enter one of the answers stated above: ")

            if question3 not in ["Blue Whale","blue whale","Blue whale"]:
               print("Sorry, but this was the wrong answer!")
               print("Please try again")
               
               
               
            else:
               print("")
               print("Good job!")
               print("Two more questions and maybe you can win!")
               points = points + 5
               print("")
               print("Which is the most rarest metal to find?")
               print("Platinum")
               print("Gold")
               print("Ruthenium")
               print("Iridium")

               question4 = input("Please enter one of the answers stated above: ")
               if question4 not in ["Platinum","platinum"]:
                   print("")
                   print("Soo Close!")
                   print("Better luck next time")
                   
               else:
                    print("")
                    print("One more right answer to go and you win the game!")
                    points = points + 5
                    print("")
                    print("Last question!!!")
                    print("If you get this one right, you win the whole game")
                    print("Which is the fastest accelerating car currently in the world?")
                    print("Lamborghini Aventador")
                    print("Buggati Veryon Super Sport")
                    print("Ferrari LaFerrari")
                    print("Tesla Model S P100D")

                    question5 = input("Please enter one of the answers stated above: ")

                    if question5 not in ["tesla model s p100d","Tesla Model S p100d","Tesla Model S P100D","Tesla model s p100d"]:
                            print("")
                            print("Its okay, sometimes you win sometimes you lose")
                            print("You can play again if you want to win!!!")

                           

                    else:
                       print("")
                       print("Congratulations, you have won the game!!")
                       print("You win...... NOTHING!!!")
                       points = points + 5

                       print("")
                       print ("       Game Summary")
                       print ("Here is your score! = ", points)

playAgain = input("Do you want to play again:(y/n)")
print("")
print("Thank youj for playing!!!")
timeFinsh = time()
totalTimeToAnswer = timeFinsh - timeStart
print("You took", totalTimeToAnswer,"seconds to answer all the questions!!!")
print("Try again and get a better score!!!")





tryAgain = True

while tryAgain:
    
    name = input ("Welcome! What is your name?: ")
    #Greeting and asking the user's name
    print("Oh" + name + " That's a beautiful name")
    
    temperature = input ("What is the temperature today?: ")
    #Asking the temperature

    mood = input ("What is your mood today? (good, bad or inbetween): ")
    #Asking the user's mood

    if mood == "good":
        print( "Great, you're feeling good")
    elif mood == "bad":
        print( "I'm sorry you're feeling like this")
    else: 
        print("It looks you're feeling neutral")

    tryAgain = input ("Try again? Enter y for yes, n for no: ")
    


    if tryAgain != "y": # not equal to y
       tryAgain = False

print("Thank you for using my program")




# if answer == 'yes':
# if answer != 'yes'
    
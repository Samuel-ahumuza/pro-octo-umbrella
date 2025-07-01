"""Welcome to the Movie Ticket Booth"""
MovieChoiceInput =str(input("Enter the movie you want to watch:"))
if (MovieChoiceInput) == ("Action"):
    print("UGX 30,000")
elif (MovieChoiceInput) == ("Romantic"):
    print ("UGX 29,000)")
elif (MovieChoiceInput) == ("Horror"):
    print("UGX 28,000)")
elif (MovieChoiceInput) == ("Comedy"):
    print("UGX 25,000)")
elif (MovieChoiceInput) == ("Adventure"):
    print("UGX 26,000)")
elif (MovieChoiceInput) == ("Kids Animation"):
    print("UGX 15,000)")
else:
    print("Invalid,please enter any one movie")
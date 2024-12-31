print ("Welcome to my quiz")

Note = input("Are you ready? ")

if Note != "yes":
    quit()
else:
    print("Welcome boss!!" ) 
    Score = 0 

Question = input("What does AI stand for? ")

if Question.lower() == "artificial intelligence":
    print("Correct")
    Score =+ 1
else:
    print("incorrect")

Question = input("Which term refers to the ability of a machine to learn from data and improve over time? ")

if Question.lower() == "machine learning":
    print('Correct!')
    Score += 1
else:
    print("Incorrect!")   

Question = input("Which is the popular programming language used in AI development? ")  

if Question.lower() == "python":
    print("correct")
    Score += 1

else:
    print("Incorrect!")  


print("Quiz has been completed")
print ("you got " + str(Score) + " correct answers in total") 
print("Congrats!!")      


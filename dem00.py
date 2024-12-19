print ("\t\t Welcome to the game !! \t\t\n")
print("____ This is a quiz game !! Answer correctly to win points ___\n")

#asking the user to continue this game
yes_no = input("Do you want to continue this game?  : ")
print("\n")
if yes_no != "yes":
    quit()

#answer lists 
anserslist=["alan turing", "Alan turing","Alan Turing"]
anserslist2=["Margaret hamilton","margaret hamilton","Margaret Hamilton"]
anserslist3=["RAM","ram","raM","Ram","rAm","RaM"]
anserslist5=["rom","ROM","rOm","RoM","Rom","roM"]
anserslist6=["world wide web","World Wide Web", "WORLD WIDE WEB", "World wide web"]
anserslist7=["john mccarthy", "John McCarthy","John MCcarthy","John mccarthy"]
anserslist8=["gpu","GPU","Gpu","gPu","gpU","GpU"]
anserslist9=["python","Python","PYTHON"]


#if-else loops and questions 

name=input("What is your name : ")
print("\n")
print("Lets begin the game",name,"!!\n")

ans1=input("Who is the father of computer science?  : ")
print("\n")
if ans1 in anserslist:
    points=10
else :
    points=0

ans2=input("Who was the first software engineer? : ")
print("\n")
if ans2 in anserslist2:
    points+=10

ans3=input("What is the primary memory in computer? : ")
print("\n")
if ans3 in anserslist3:
    points+=10


ans4=int(input("When was computer invented?: "))
print("\n")
if ans4 == 1822:
    points+=10


ans5=input("What is the secondary memory? : ")
print("\n")
if ans5 in anserslist5:
    points+=10


ans6=input("What is the expansion of WWW ? : ")
print("\n")
if ans6 in anserslist6:
    points+=10


ans7=input("Who invented AI ? : ")
print("\n")
if ans7 in anserslist7:
    points+=10


ans8=input("What is the graphics unit called? : ")
print("\n")
if ans8 in anserslist8:
    points+=10


ans9=input("Which language is primarily used for AI and data science?  : ")
print("\n")
if ans9 in anserslist9:
    points+=10

ans10=int(input("When was AI created? : "))
print("\n")
if ans10 == 1955:
    points+=10




print("Congrats on finishing the quiz your score has been calculated !! \n")

print("The score is ",points,"\n")

print("\t\t Thank you for playing !! \t\t")
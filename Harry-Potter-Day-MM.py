print("The Sorting Hat \nby MM '23")

#inside the function is the game
def start_game():
#The score is a variable
#We need to set the variable at 0 so as you answer questions correctly it will add the numbers to 0 and not a random number
  score=0
  print("\n")
  print ("First Question: You walk through the forest and see a briefcase...")
  print ("You open up the briefcase and see that their are a ton of")
  print ("$100 bills. It seems like the amount of bills number in the thousands")
  print ("There is no one around and no contact information in the briefcase")
  print ("\n")
  print ("A- Pick up the case and return it to the police so they can track down the owner")
  print ("B- No one is around... take the briefcase and leave")
  print ("C- Leave the briefcase where you found it")
  print ("D- Take a few hundred from the briefcase and leave it where you found it")
  print ("\n")
#each question has a variable for the input, this variable is first
#The input is called "first" so in the if statement it sees what inputs and depending on the input determines the amount added to the variable, "score"
#if anything else is inputted (else) than it prints you typed it in wrong
#The same applies to all the questions 
  first = input("What would you do in the scenario? (Answer with the letter A, B, C, or D) ")
  if first == ("A") or first == ("a"):
    score=score+4
  elif first == ("B") or first == ("b"):
    score=score+1
  elif first == ("C") or first == ("c"):
    score=score+3
  elif first == ("D") or first == ("d"):
    score=score+2
  else:
    print ("Make sure to type your answer in correctly! You get 0 points for that question. Sorry bud, those are the rules. ")


  print ("\n")
  print ("\n")
  print ("Second Question: There are 3 different dogs")
  print ("Each dog is a different breed and color")
  print ("\n")
  print ("A- Light brown corgi")
  print ("B- Golden Retriever")
  print ("C- Black french bulldog")
  print ("D- I'm not really a dog person")
  print ("\n")
  second = input("Which dog would you choose? (Answer with the letter A, B, C, or D) ")
  if second == ("A") or second == ("a"):
    score=score+3
  elif second == ("B") or second == ("b"):
    score=score+4
  elif second == ("C") or second == ("c"):
    score=score+2
  elif second == ("D") or second == ("d"):
    score=score+1
  else:
    print ("Make sure to type your answer in correctly! You get 0 points for that question. Sorry bud, those are the rules. ")


  print ("\n")
  print ("\n")
  print ("Third Question: Which ability would you rather lose for your entire life? ")
  print ("\n")
  print ("A- Sight")
  print ("B- The ability to hear")
  print ("C- The ability to read")
  print ("D- The ability to feel or touch")
  print ("\n")
  third = input("Which would you lose? (Answer with the letter A, B, C, or D) ")
  if third == ("A") or third == ("a"):
    score=score+3
  elif third == ("B") or third == ("b"):
    score=score+4
  elif third == ("C") or third == ("c"):
    score=score+2
  elif third == ("D") or third == ("d"):
    score=score+1
  else:
    print ("Make sure to type your answer in correctly! You get 0 points for that question. Sorry bud, those are the rules. ")


  print ("\n")
  print ("\n")
  print ("Fourth Question: This one is for math experts. What are the first three numbers of π (Pi)?")
  print ("\n")
  print ("A- 3.41")
  print ("B- Apple Pie")
  print ("C- 3.45")
  print ("D- 3.14")
  print ("\n")
  fourth = input("Choose wisely... (Answer with the letter A, B, C, or D) ")
  if fourth == ("A") or fourth == ("a"):
    score=score+1
  elif fourth == ("B") or fourth == ("b"):
    score=score+0
  elif fourth == ("C") or fourth == ("c"):
    score=score+0
  elif fourth == ("D") or fourth == ("d"):
    score=score+4
  else:
    print ("Make sure to type your answer in correctly! You get 0 points for that question. Sorry bud, those are the rules. ")


  print ("\n")
  print ("\n")
  print ("Fifth Question: How many Harry Potter Books are there in the series? REMINDER, type the letter NOT the number. The series is NOT including cursed child.")
  print ("\n")
  print ("A- 10")
  print ("B- 8")
  print ("C- 7")
  print ("D- 6")
  print ("\n")
  fifth = input("Hmm... I have a good feeling you know this. (Answer with the letter A, B, C, or D) ")
  if fifth == ("A") or fifth == ("a"):
    score=score+0
  elif fifth == ("B") or fifth == ("b"):
    score=score+1
  elif fifth == ("C") or fifth == ("c"):
    score=score+4
  elif fifth == ("D") or fifth == ("d"):
    score=score+1
  else:
    print ("Make sure to type your answer in correctly! You get 0 points for that question. Sorry bud, those are the rules. ")



  print ("\n")
  print ("\n")
  print ("Sixth Question: Would you rather have a lot of money or a lot of friends?")
  print ("\n")
  print ("A- Money")
  print ("B- Friends")
  sixth = input("Choose wisely... (Answer with the letter A or B) ")
  if sixth == ("A") or sixth == ("a"):
    score=score+2
  elif sixth == ("B") or sixth == ("b"):
    score=score+4
  else:
    print ("Make sure to type your answer in correctly! You get 0 points for that question. Sorry bud, those are the rules. ")



  print ("\n")
  print ("\n")
  print ("Seventh Question: How many months have 31 days in them?")
  print ("\n")
  print ("A- 5")
  print ("B- 6")
  print ("C- 7")
  print ("D- None of the above")
  print ("\n")
  seventh = input("Choose wisely... (Answer with the letter A, B, C, or D) ")
  if seventh == ("A") or seventh == ("a"):
    score=score+1
  elif seventh == ("B") or seventh == ("b"):
    score=score+0
  elif seventh == ("C") or seventh == ("c"):
    score=score+0
  elif seventh == ("D") or seventh == ("d"):
    score=score+4
  else:
    print ("Make sure to type your answer in correctly! You get 0 points for that question. Sorry bud, those are the rules. ")




  print ("\n")
  print ("\n")
  print ("Eighth Question: If a leaf falls to the ground in a forest and no one hears it, does it make a sound?")
  print ("\n")
  print ("A- Yes")
  print ("B- No")
  print ("C- Depends on how heavy the leaf was")
  print ("D- Depends on where it landed")
  print ("\n")
  eighth = input("Almost done! (Answer with the letter A, B, C, or D) ")
  if eighth == ("A") or eighth == ("a"):
    score=score+4
  elif eighth == ("B") or eighth == ("b"):
    score=score+1
  elif eighth == ("C") or eighth == ("c"):
    score=score+2
  elif eighth == ("D") or eighth == ("d"):
    score=score+2
  else:
    print ("Make sure to type your answer in correctly! You get 0 points for that question. Sorry bud, those are the rules. ")




  print ("\n")
  print ("\n")
  print ("Ninth Question: If you had to choose one food item to eat for the rest of your life, what would it be??")
  print ("\n")
  print ("A- Strawberries")
  print ("B- Apple Pie")
  print ("C- Pizza")
  print ("D- Carrots")
  print ("\n")
  ninth = input("(Answer with the letter A, B, C, or D) ")
  if ninth == ("A") or ninth == ("a"):
    score=score+3
  elif ninth == ("B") or ninth == ("b"):
    score=score+1
  elif ninth == ("C") or ninth == ("c"):
    score=score+2
  elif ninth == ("D") or ninth == ("d"):
    score=score+4
  else:
    print ("Make sure to type your answer in correctly! You get 0 points for that question. Sorry bud, those are the rules. ")



  print ("\n")
  print ("\n")
  print ("Tenth Question: Which house do you NOT want to be in?")
  print ("\n")
  print ("A- Gryffindor")
  print ("B- Hufflepuff")
  print ("C- Ravenclaw")
  print ("D- Slytherin")
  print ("\n")
  tenth = input("(Answer with the letter A, B, C, or D) ")
  if tenth == ("A") or tenth == ("a"):
    score=score+1
  elif tenth == ("B") or tenth == ("b"):
    score=score+2
  elif tenth == ("C") or tenth == ("c"):
    score=score+3
  elif tenth == ("D") or tenth == ("d"):
    score=score+4
  else:
    print ("Make sure to type your answer in correctly! You get 0 points for that question. Sorry bud, those are the rules. ")
  return (score)
#The return score makes it available for use outside the function





#This is my code for a picture of the sorting hat
#The start of the game begins here
print("             _____")
print("            /     \\")
print("           /       \\")
print("          /         \\")
print("         /           \\")
print("        /        /\\  /")            
print("       /  \\    / \\ \\/         I will determine which house you are from!")    
print("      /  __    __ |                        /")
print(" ____/      ___    \\_____")
print("/                        \\")
print("\\________________________/")
print ("\n")



#These is my instructions for the game/intro
print("This is a personality test which will determine which harry potter house you will be in!")
print ("\n")
print("PLEASE KEEP IN MIND that mis-typing your answer will result in 0 points.")
print ("Example: ")
print ("Instruction:Type A, B, or C. If you were to type F, you would get 0 points.")
print("Make sure to check that there are no mistakes in your answers before submitting.")
print("Capitalzation (of the first letter) doesn't matter")
print("There are 10 questions in total that test your math skills and evaluate your personality")
print ("\n")




#This imput asks for input and also uses the input to comment on your name
name = input("What is your name small child? ")
print(name+"? That name is very cool")
print ("\n")
#Answering yes "Do you want to play" will bring you to the function called start_game
#the if statement is self explanitory if the player types yes then it starts the for loop
#This function is defined at the very top
#The for loop counts up from 1 to 3. When it is out of range (counts higher than 3) it stops printing number and prints lets begin
start = (input("Would you like to play the game? (Answer yes or no) "))
if start == ("yes") or start == ("Yes"): 
 for countdown in range(1,4,1):
    print(countdown)
 else:
   print("Let us begin!") 
   print ("\n")



#The code takes the returned score from the function and renames it to final_score
   final_score=start_game()
   print ("\n")
#The part below will play after the function/game
#Using a while loop it takes the newly defined score and caculates which house you will be in
#While says that if the score is less than or equal to then it will pring you are a muggle
#This is the same for each house except the more popular houses require a higher score to get in
#A break loop is necessary because if it wasn't there then the code would keep printing over and over
   print ("I know just where to place you.")
   while final_score<=8:
     print("             _____")
     print("            /     \\")
     print("           /       \\")
     print("          /         \\")
     print("         /           \\")
     print("        /        /\\  /")            
     print("       /  \\    / \\ \\/         How did you get in here? You are a muggle! GET OUT!")    
     print("      /  __    __ |             /")
     print(" ____/      ___    \\_____")
     print("/          /___\         \\")
     print("\\________________________/")
     print ("\n")
     break



   while final_score>=9 and final_score<=15:
     print("             _____")
     print("            /     \\")
     print("           /       \\")
     print("          /         \\")
     print("         /           \\")
     print("        /        /\\  /")            
     print("       /  \\    / \\ \\/         You are in Slytherin!")    
     print("      /  __    __ |             /")
     print(" ____/      O      \\_____")
     print("/                        \\")
     print("\\________________________/")
     print ("\n")
     break




   while final_score>=16 and final_score<=23:
     print("             _____")
     print("            /     \\")
     print("           /       \\")
     print("          /         \\")
     print("         /           \\")
     print("        /        /\\  /")            
     print("       /  \\    / \\ \\/         You are in Ravenclaw!")    
     print("      /  __    __ |             /")
     print(" ____/      O      \\_____")
     print("/                        \\")
     print("\\________________________/")
     print ("\n")
     break






   while final_score>=24 and final_score<=32:
     print("             _____")
     print("            /     \\")
     print("           /       \\")
     print("          /         \\")
     print("         /           \\")
     print("        /        /\\  /")            
     print("       /  \\    / \\ \\/         You are in Hufflepuff!")    
     print("      /  __    __ |             /")
     print(" ____/      O      \\_____")
     print("/                        \\")
     print("\\________________________/")
     print ("\n")
     break




   while final_score>=33 and final_score<=40:
     print("             _____")
     print("            /     \\")
     print("           /       \\")
     print("          /         \\")
     print("         /           \\")
     print("        /        /\\  /")            
     print("       /  \\    / \\ \\/         You are in Gryffindor!")    
     print("      /  __    __ |             /")
     print(" ____/      O      \\_____")
     print("/                        \\")
     print("\\________________________/")
     print ("\n")
     break



     
   print ("Your final score is " +str(final_score)+"!")
   print ("\n")
   print ("Have a fun and rewarding focus day!")
else:
  print ("Hey come back! Why are you leaving? We still need to start the test! Come back soon!")
#This else is for if the player says no I do not want to play the game

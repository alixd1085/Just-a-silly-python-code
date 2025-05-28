import random
import time
import os

ran_num = random.randint (1,99999999999)
attempts = 0
errors = 0

def wait ():                                                                                                #(9,10,11,12) Defines the "wait" function so it could Print the (.) 3 times and waiting 2 seconds after each one
 for i in range(3):
  time.sleep(2)
  print(".")
  


while True:
 try:
  answer = int(input("Please select a number from 1-10:\n>"))                                                #(18) asks the user for an input

  if answer == ran_num:
    print(f"Correct the number was {ran_num}!")                                                              #(21) If the user got the input right (Mostly by cheating) Print the following string
    wait()                                                                                                   #(22) Prints 3 (.)'s after the user gets the input
    print (f">I know that you cheated...")
    time.sleep (2)                                                                                           #(24) Waits for 2 seconds so it doesn't print it at the same time
    print(">Why.")
    time.sleep(2)

    def countdown ():                                                                                        #(28) assigns a "countdown" function that Countsdown from 3 to 0
     seconds = 3
     for i in range(seconds, 0,-1):
      print(f"[{'=' * (seconds - i)}{' ' * i}] {i} seconds left", end='\r')                                  #(31) Line No. 28,30 Got copied from ChatGPT 
      time.sleep(1)




    confirm = input (">Give me a reason why i shouldn't shut this program down...\n>")                       #(37) Asks for a reason to give the user a second chance
    if confirm.lower() in ["I'm sorry","Please"]:                                                            #(38) The list of words (could be better)+(Modified by ChatGPT
     print(">Fine.. at least you feel sorry for it, shutting down in\n")                                     #(39) The user gets a second chance if he entered a word from the list above
     
     countdown()                                                                                             #(41) Calls the countdown function
    
    else:                                                                                                    #(43) If the user didn't write the Correct word this line of code starts
     wait()
     print(">That's not a valid reason. Closing in\n")

    countdown()                                                                  
    break

  if answer != ran_num:
   attempts += 1                                                                                             #(51) After each wrong guess the "attempts" variable increases it's value by 1
  print(f"The number was incorrect try again: attempt {attempts} \n>")
  if attempts == 3:
   print(f"the number is {len(str(ran_num))} numbers long.")                                                 #(54) every time the user gets an input wrong 3 times it displays a hint
  if attempts == 6:
   print(f"The number begins with {str(ran_num)[:3]}")
  if attempts == 9:
   print(f"The number begins with {str(ran_num)[:6]}")
  if attempts == 12:
   print(f"The number begins with {str(ran_num)[:9]}")
  if attempts == 15:
   print(f"fine you idiot the number is {str(ran_num)[:11]}...")


 except ValueError:
   errors += 1

   if errors <5:
    print(f"The input is wrong please try again({errors})\n>")
   if errors == 5:
    print("Stop it...\n>")
   if errors == 6:
    print("You know that this is useless right.\n>")
   if errors == 7:
    print("There's no easter egg in here idiot, Go away\n>")
   if errors == 10:
    print(f"FINE FINE THE NUMBER IS {ran_num} JUST STOP IT\n>")
   if errors == 11:
    print("Ok fuck you you're not playing anymore")
    break                                                                    #Just a silly easter egg :)

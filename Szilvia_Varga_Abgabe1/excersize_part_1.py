import time
#Excersize 1: Famous Quote
import sys


def famous_quote():
    print("Press enter to see my quote: ")
    enter = input()
    print("""The Doggo from Adventure time once said, 
        "Something  weird might just be something familiar
            viewed from a different angle" """)

#famous_quote()


#Excersize 2: Number Eight

def number_eight():
    a = "Mary had a little lamb, John had a giant lamb"

    print(1+2+4+1)
    print(2*4)
    print(int(16/2))
    print(10-2)
    print(a.count('a'))

#number_eight()

#Excersize 3: Formatting

def name_age():

    #ask name
    #lets make it sure, that the user can only input alphabets (Im sorry XÆA-12, you cannot use this program rn!...
 while True:#infinite loop, break out when the condition is met...
     print("What is your name?")
     try:
      name = input()
      if not name.isalpha():
        raise ValueError
      break  # jump out of the loop if input is valid, keep going if it isnt!
     except ValueError:
            print("Your answer must be a word consisting only of Alphabets")

    #ask age
    #lets make it sure that the user can only input numbers, keep going as long as the condition isnt met
 while True:
     print("How old are you?")

        #convert the input to an int straight away, so you can calculate with it...
     try:
        age=int(input())
        break  # jump out of the loop if input is valid, keep going if it isnt!
     except ValueError:
         print("Your answer must be a number")


    # FORMATTING METHODS:

    #Formatting method 1:Concationation
    #here the age must be converted back, so it can be concationated
 messageCon = ("Dear " + name + " you are " + str(age) + " years old.")

    #Formatting method 2:string format() method
 messageFor = ("Dear {} you are {} years old.")

    #Formatting method 3:f-strings
 messageFs = ("Dear %s you are %a years old." % (name, age))

    #lets save a few things to avoid repeating
 a = "\n\t"

  #hard coded massages:
 m1 = "You are still a little baby!"
 m2 = "Hang on...youre getting there...!"
 m3 = "Almost ready to be happy!"
 m4 = "Life is good!"
 m5 = "Keep going buddy!"

    #my very own print method, so I dont have to write the print method so many times
 def printMethod(message):
     print(messageCon + a + message)
     print(messageFor.format(name, age) + a + message)
     print(messageFs + a + message)

 if (age>0 and age < 130 ):
         if (age<=10):
             printMethod(m1)
         elif (age >= 11 and age <= 18):
             printMethod(m2)
         elif (age >= 19 and age <= 32):
             printMethod(m3)
         elif (age >= 33 and age <= 60):
             printMethod(m4)
         elif (age >= 61):
             printMethod(m5)
 else:
     print("Invalid input!")

#name_age()

#Excersize 4: Swap

def swap_integers():
    while True:
         print("Please enter x: ")
         try:
           n1 = int(input())
           break
         except ValueError:
             print("Input 1 Must be a number!")

    while True:
          print("Please enter y: ")
          try:
            n2 = int(input())
            break
          except ValueError:
                 print("Input 2 Must be a number too!")

    print("Before swap "+ "\n" + "x = " + str(n1) + "\n" + "y = " + str(n2))
    n3=n1
    n1=n2
    n2=n3
    print("After swap "+ "\n" + "x = " + str(n1) + "\n" + "y = " + str(n3))


#swap_integers()

#Excersize 5: Modulo check

def check_numbers(number1, number2):
    #number one OR number2 can be divided by 6 without a leftover
    #           AND
    #number1 AND number2 both divisible without a leftover
    if((number1 % 6 == 0 or number2 % 6 == 0) and number1 % 10 == 0 and number2% 10 == 0):
        print("true")
    else:
        print("false")

#check_numbers(12,60)

#Excersize 6: Summarizer
def sum_up(num1, num2):

    #the trick is: introduce variable outside of loop
 sum = 0

 while num1 <= num2:
     print(str(num1), end="")#by default in the end of a print statement there is a \n --> set "end = "" to get ri of it
     if num1 < num2:#check if we are at the last number or not, since we want to stop printing + signs if so
      print(" + ", end="")
     sum = sum + num1
     num1 = num1 + 1


 print(" = " + str(sum))

#sum_up(3,9)

#Excersize 7: Sequencer

def sequence(number):

    if (int(number)>=0 and  int(number)<=9):
        n=0
        while n <= 9:
          if(not n==number):
            print(str(n) + " ",end="")
          n = n + 1
    else:
     print("Not between 0 and 9")

#sequence(3)

#Excersize 8: String check
def string_check(text=""):#I provide a default value : an empty string--> the argument becomes optional
    #like this I an check and react myself, if the user doesnt provide anything
       if len(text) > 0:#is my text empty?if not, check whats inside
            if (str(text).lower().startswith("a") or str(text).lower().endswith("a")):
                print("True")
            else:
                print("False")
       else:#my text is empty --> write my own message
           print("You have to enter something!")

string_check("Alma")

def triangle(rows):
    i=0
    while i<= int(rows):

        print("* " * i)
        i+=1

#triangle(4)




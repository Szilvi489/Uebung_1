import itertools
#Exercise 1: Counting
def count_a_number():
 #Version 1
            # An asterisk (*) in front of a parameter in a function signature captures an unlimited number of arguments into a tuple
            #since the exercise said is must be a list, I transform the tuple into a list
    def count_a_number1(*numbers, number=None):
        numbers = list(numbers)  # convert tuple to list
        counter = 0
        for n in numbers:
             if number is not None and number == n:
               counter += 1
        print("In the list: " + str(numbers) + " ,the number " + str(number) + " occurs " + str(counter) + " times")


    #input list
    my_list = [1,2,3,4,4,4]
    count_a_number1(*my_list, 4)


     #Version 2
    def count_a_number2(numbers,number):

       counter = 0
       for n in numbers:
           if number == n:
               counter += 1


       print("In the list: "+ str(numbers) + " ,the number " + str(number) + " occurs " + str(counter) + " times")



    #pass on several numbers in an argument --> either direc in method call: count_a_number(list((12,44,333,5,6,4443,5,45,5,45)),2), or make a variable out of it to make it more readable
    my_list2=[12,12,2,33,33,5,5,44,5,5,5,5,5]
    count_a_number2(my_list2, 5)

#count_a_number()


#Exercise 2: Playing with lists

def play_with_lists(numbers, number):
 print("*****************REVERSE ORDER**************************************")
#1,Reverse order:
# Print out the list in reverse order but leave the original list in order
 #original_list = [1,2,3,45,555]
 print("List before reverse: ", numbers)

    #Ways to reverse a list:
        #1,Using the .reverse() method -> this will reverse the original list
 numbers.reverse()
 print("List after built in reverse: " ,numbers)

        #2, Using a for loop -> original list untouched
 loop_reversed_list = []
 for v in numbers:
  loop_reversed_list = [v] + loop_reversed_list
 print("List after loop reverse: " , loop_reversed_list)

        #3, Using slicing operation -> original list untouched
        #Slicing-->creating sublists
        #The full slice syntax is [start:stop:step], but parts can also be used.
 print("List after slicing reverse: ", numbers[::-1])

        #4, reversed() method -> original list untouched
 reversed_reversed_list = list(reversed(numbers))
 print("List after reversed() method ", reversed_reversed_list)
    #Reversed isnt limited to lists
 print("\"Reversed()\" used on a range() of non-predefined numbers: " , list(reversed(range(10))))


 print("*****************REPLACE A VALUE**************************************")
# Replace the given integer "number" within the list with the number 1 and print it on the
#console

 for n in range(len(numbers)):
     if numbers[n] == number:
          numbers[n] = 1
          print("Swapping the number " + str(number) + " to 1 : " , numbers)

 print("*****************SORTING**************************************")
#Print out a sorted version of the list in descending order
    #Ways to sort a list:
    # Sorting a list with a built in method:sort() function of the class list --> it will modify the original list
 numbers.sort(reverse = True) #descending order
 print("Descending order with sort() of LIST class: " , numbers)
 numbers.sort()
 print("Ascending order with sort() of LIST class" , numbers)

    #With the python sorted() function
    #sorted(iterable, key=key, reverse=reverse)
 sorted_list = sorted(numbers)
 print("Ascending order with the PYTHON sorted function ", sorted_list)

 sorted_list = sorted(numbers, reverse=True)
 print("Descending order with the PYTHON sorted function ", sorted_list)

    #With while and for (not my invention tho :// )
 new_list = []

 while numbers:                          #as long as there are elements in numbers list
        minimum = numbers[0]             #technically, we say, the smallest number is the one on position 0, and start it from here...It will start comparing of the numbers with the number, that is on position 0, essentially, it doesnt matter from which position you start, coz it will do the sorting, as long as every number is sorted...
        for x in numbers:                #
            if x < minimum:              #
                minimum = x             #if the upcoming element is smaller than the element on position 0, make it position 0
        new_list.append(minimum)        #add it to new_list as the latest element
        numbers.remove(minimum)

 print ("Elements saved in a new list with reversed order: ", new_list)
 print("Elements are gone from the old list: ", numbers)

original_list = [1,2,3,45,555, 2, 33, -33]
#play_with_lists(original_list,2)

#Exercise 3: Comparing list elements
def compare_list(list1,list2):
    #looks for elements that the 2 lists have in common, and returns a list with the common elements

#1,pythons built in set intersection:
 intersections = list(set(list1).intersection(list2)) #this is in a list after this, but the list gets the elements unorderred every time.

 sorted_intersections_list = sorted([str(x) for x in intersections])  #.sort( reverse = True) wont work, since the values are mix of int and string
 print(type(sorted_intersections_list))                                #by convertin ALL the values into strings str() than use the sorted() function which will sort them alphabetically
                                                                        #in the output note the 2 as '2' !!
 print("Compared with set intersections: ", sorted_intersections_list)


#2,for loop and if statement
 common_elements_loop = []                                   #create a new list only for the common elements
 for item in list1:
        if item in list2:
            common_elements_loop.append(item)
 print("Compared with loop and if: ",common_elements_loop)

#3,with list comprehension
    #[expression for item in iterable if condition]
                        #Here, expression is the operation or transformation to be performed on each item in the iterable,
                        # item is the variable representing each item in the iterable,
                        # and condition is an optional filter that can be applied to the items.
 common_elements_comprehension = [item for item in list1 if item in list2]
 print("Compared with list comprehension: ", common_elements_comprehension)


list1=["apple", 2, "monkey",14,444,"U-Nahn"]
list2=["apple", 33, 554, "sea", 6, "yyy", "monkey", 2]

#compare_list(list1,list2)


#Exercise 4: No duplicates!
#remove duplicates with a set:
def remove_duplicates(items):
 items_noDuplicates_set = set(items)                    #in a set duplicates are not alought
 items_noDuplicates_list = list(items_noDuplicates_set) #I save the selected set with no duplicates to a list, so I can sort it agaibn alphabetically
 items_noDuplicates_list.sort(reverse=False)            #sorting it alphabetically
 print(items_noDuplicates_list)

items_list = ["a","a","a","b","b", "c", "d", "e", "f", "g"]
#remove_duplicates(items_list)

#remove duplicates in a different way
def remove_duplicates_my_way(items):
 print("******************for, if ...**************************************************")
 new_items=[]               #a new list, where only the first occurance of a specific item is going to be saved
 for x in items:            # go through all items in the given list
  if x not in new_items:    #if the item that is being checked at the moment, isnt in the new list yet
    new_items.append(x)     #, save it there
 print("Remove duplicates with for loop and if: " , new_items)

 print("******************Using Comprehension**************************************************")
#using comprehension
 #[expression for item in iterable if condition]

 comprehension_list = list(set([x for x in items]))
 comprehension_list.sort(reverse=False)
 print("Remove duplicates with comprehension: ", comprehension_list)

#remove_duplicates_my_way(items_list)



#Exercise 5: Computer description
#Add default values, in case the key isnt there at all
def describe_computer(computer):#accepts a dictionary
    #to print:You have a TYPE from BRAND that costs PRICE€.
 brand=computer.get('Brand','Unknown Brand')
 os=computer.get('OS', 'Linux')
 #output = ("You have a " , computer["Type"] , " from brand: ", computer["Brand"], ", that costs: " , computer["Price"],"$ ", ",OS: ",computer["OS":"Linux"], sep="")
 output = f"You have a {computer['Type']} from brand: {brand}, that costs: {computer['Price']}$, OS: {os}"
 print(output)

my_notebook1 = {'Type': 'Notebook','Brand' : 'MAC' , 'Price': 2000 , 'OS' : 'MacOS Ventura' }
my_notebook2 = {'Type': 'Notebook','Brand' : 'Huawei' , 'Price': 2000 }
my_notebook3 = {'Type': 'Notebook', 'Price': 2000}

#describe_computer(my_notebook1)
#describe_computer(my_notebook2)
#describe_computer(my_notebook3)

#todo COMMIT!!
#Describe Computer 2: An other way to add default values (if the key doesnt exist at all) would be to simply use an if statement and save the new dictionary in the place of the old one...
#Add default values, in case the key isnt there at all
def describe_computer2(computer):
 if "Type" not in computer or "OS" not in computer:
     computer = {'Type':'Unknown type' , 'Brand' : 'DELL' , 'Price': 2000 , 'OS' : 'Linux' }
     print(computer)



my_notebook1 = {'Brand' : 'MAC' , 'Price': 2000 , 'OS' : 'MacOS Ventura' }
my_notebook2 = {'Type': 'Notebook','Brand' : 'Huawei' , 'Price': 2000}
my_notebook3 = {'Price': 2000}

#describe_computer2(my_notebook1)
#describe_computer2(my_notebook2)
#describe_computer2(my_notebook3)

#todo Add default vlaues, if the key there, but there is no value
def describe_computer3(computer):
 if (computer["Type":"T"] or computer["Type":"Y"]):
     print("No type")





my_notebook1 = {'Type': '','Brand' : 'MAC' , 'Price': 2000 , 'OS' : 'MacOS Ventura' }
my_notebook2 = {'Type': 'Notebook','Brand' : 'MAC' , 'Price': 2000 , 'OS' : 'MacOS Ventura' }
my_notebook3 = {'Type': 'Notebook','Brand' : 'MAC' , 'Price': 2000 , 'OS' : 'MacOS Ventura' }

describe_computer3(my_notebook1)

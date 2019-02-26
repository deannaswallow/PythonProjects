#Created by: Deanna Swallow
#Date created: 8/29/2017
#Chapter 8, Exercise 1
#The main program is provided in order to test the functions asked for. One
#function, Chop, will modify a list and return nothing. The second function,
#Middle, will make a new list (a modified version of the list provided), and it
#will return the new list.
#-------------------------------------------------------------------------------
def main():
    #Original dummy list for testing
    numbers = [1,2,3,4,5,6]
    print('The original list is ',numbers)

    #Test the chop function
    chop(numbers)
    print('The new list, modified by the chop function, is: ',numbers)

    #Test the middle function
    middle_test = middle(numbers)
    print('The new list, created by the middle function, is: ',middle_test)

def chop(mod_list):
    #This function will modify the list passed to it, removing the first and
    #last elements. This function returns None.
    del mod_list[0]
    del mod_list[len(mod_list)-1]
    

def middle(old_list):
    #This function takes a list as an argument, and it returns a new list that
    #contains everything in the original list except the first and last
    #elements. This function does not change the list passed to it.
    return old_list[1:len(old_list)-1]

#Call main
main()

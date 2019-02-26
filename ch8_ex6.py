#Created by: Deanna Swallow
#Date created: 8/31/2017
#Chapter 8, Exercise 6
#This program will prompt the user for a list of numbers and then print out the
#maximum and minimum numbers at the end, after the user enters "done" to signify
#that they are finished entering numbers.
#-------------------------------------------------------------------------------
def main():
    #provide user with instructions
    print('You will be prompted to enter a list of numbers. After each number,')
    print('please hit Enter. When you are done, please enter "done", but')
    print('without the quotes. After you do so, the largest and smallest')
    print('numbers you entered will be displayed.')

    #create list to hold input
    user_numbers = []

    #prompt for numbers, store them in list
    while (True):
        ipnumber = input('Enter a number: ')
        if ipnumber == 'done' or ipnumber == 'Done': break
        num = float(ipnumber)
        user_numbers.append(num)

    #print maximum and minimum numbers
    print('The largest number entered is: ',max(user_numbers))
    print('The smallest number entered is: ',min(user_numbers))

#call main
main()

        
        
    

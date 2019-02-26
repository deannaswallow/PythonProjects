#Created by: Deanna Swallow
#Date created: 9/7/2017
#Chapter 9, Exercise 4
#This program will read through a mail log and build a histogram using a
#dictionary to count how many messages come from each unique sender (email
#address). At the end, the program will display who sent the most messages.
#-------------------------------------------------------------------------------
def main():
    #open file
    fname = input('Please enter the file name to open: ')
    try:
        infile = open(fname)
    except:
        print('File could not be opened:',fname)
        exit()
    
    #create empty dictionary to fill
    emails = dict()

    #process file
    for line in infile:
        #split line into list of words
        words = line.split()
        #rule out lines that don't fit criteria
        if len(words)<2 or words[0]!='From': continue
        #assign email address from list
        address = words[1]
        #count each email address
        emails[address] = emails.get(address, 0)+1

    #figure out who sent the most messages
    num = 0
    for key in emails:
        if emails[key] > num:
            num = emails[key]
            sender = key
        else:
            continue
        
    #display results--who sent the most messages
    print('The following shows who sent the most messages and how many they sent:')
    print(sender, num)
    

#call main
main()
        
        

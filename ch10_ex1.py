#Created by: Deanna Swallow
#Date created: 9/14/2017
#Chapter 10, Exercise 1
#This program will read a mail log and build a histogram by using a dictionary
#to count how many messages were sent from each unique email address. It will
#then create a list of tuples and use that list to display which email address
#sent the most messages.
#------------------------------------------------------------------------------
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

    #create list of tuples using the dictionary
    tlist = list()
    for k,v in emails.items():
        tlist.append((v,k))

    #reverse sort list of tuples
    tlist.sort(reverse=True)

    #assign tuple values for sender with most messages
    num, winner = tlist[0]

    #display results
    print('The following shows the email address that sent the most messages')
    print('and how many messages they sent:')
    print(winner, num)

#call main
main()
        

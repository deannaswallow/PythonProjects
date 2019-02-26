#Created by: Deanna Swallow
#Date created: 9/14/2017
#Chapter 10, Exercise 3
#This program will read a file and count the number of times each letter appears.
#All letters will be converted to lowercase, and the results will be displayed
#at the end with the letters listed by decreasing frequency in the file.
#-------------------------------------------------------------------------------
import string
def main():
    #open file
    fname = input('Please enter the file name to open: ')
    try:
        infile = open(fname)
    except:
        print('File could not be opened:',fname)
        exit()

    #create empty dictionary
    charcount = dict()

    #read and process file
    for line in infile:
        #get rid of punctuation
        line = line.translate(line.maketrans(' ',' ',string.punctuation))
        #make everything lowercase
        line = line.lower()
        #split line into words
        words = line.split()
        #filter out numbers and count each letter
        for word in words:
            for index in word:
                if not index.isdigit():
                    letter = index
                    charcount[letter] = charcount.get(letter, 0)+1

    #create list of tuples using dictionary and sort
    tlist = list()
    for k,v in charcount.items():
        tlist.append((v,k))
    tlist.sort(reverse=True)

    #display results
    print('The following shows the letter [first column] and how many times it')
    print('appeared in the file [second column]')
    for k,v in tlist:
        print(v,k)
    
#call main
main()

        
    

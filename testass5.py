#function will check to see if file extension is correct then will count the bases in the file
import os
def basecounter(file):
    filename, ext = os.path.splitext(file) #function splits the pathname into a ext and path
    if ext == '.fasta':
        bases = ['A', 'C', 'G', 'T']
        with open(file, 'r') as input_file: #opens input file
            next(input_file) #skip the header
            texts = input_file.readlines()
            counta = 0  # initializing finalcount variables to 0
            countc = 0
            countg = 0
            countt = 0
            for text in texts: # cycles through the different lines in the file
                for i in text:  # counting each of the characters in the file
                    if i == 'A':
                        counta = counta + 1
                    elif i == 'C':
                        countc = countc + 1
                    elif i == 'G':
                        countg = countg + 1
                    elif i == 'T':
                        countt = countt + 1
            print('A ' + str(counta))
            print('C ' + str(countc))
            print('G ' + str(countg))
            print('T ' + str(countt))
    else:
        print(file, 'is not a valid file extension')





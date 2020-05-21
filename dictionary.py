# Program to find the time taken by SHA-1 algorithm for collisions for different number of bits

# importing required libraries
import random
import hashlib
import time
import xlwt
from xlwt import Workbook
from xlrd import open_workbook
from xlutils.copy import copy

# Open excel sheet for storing data
rb = open_workbook("data-dict.xls")
wb = copy(rb)

sheet1 = wb.get_sheet(0)

for ch in range(1, 14):  # ch denotes the number of characters or hexadecimal digits to be compared
    sheet1.write(4 * (ch) - 3, 0, "Number of characters = " + str(ch))
    sheet1.write(4 * (ch) - 2, 0, "POSITIONS")
    sheet1.write(4 * (ch) - 1, 0, "TIME")  # printing the required row headings

    for i in range(10):

        randlist = random.sample(range(40), ch)  # generating a list of ch random positions 
        print(randlist)
        total_time = 0

        count = 100  # count = number of trials for each set of positions
        for j in range(count):
            collission = {}  # initialising the dictionary
            start_time = time.time()

            while 1:

                input = random.randint(1000, 100000000000000000000000000)  # random number generator
                result = hashlib.sha1(str(input).encode()).hexdigest()  # hashlib generates the hash value and stores the digest in result
                
                # Generating a string by concatenating characters from the randomly chosen positions

                hashstr = ""
                for k in randlist:
                    hashstr = hashstr + str(result)[k]

                if (hashstr in collission) == True:  # checks if the string had been generated earlier
                    print(input)                     # printing collision details to the output console
                    print(collission[hashstr])
                    print("Digit " + str(ch) + " collision " + str(j + 1) + " in " + str(i + 1))
                    print(time.time() - start_time)
                    break
                else:
                    collission.update({hashstr: input})  # appending the new string to the dictionary

            final_time = (time.time() - start_time)  # calculating the time taken for collision
            total_time = total_time + final_time

        total_time = total_time / count
        print(total_time)

        # code for writing the data values into the excel sheet

        sheet1.write(4 * (ch) - 2, i + 1, str(randlist))
        sheet1.write(4 * (ch) - 1, i + 1, total_time)

        wb.save('data-dict.xls')

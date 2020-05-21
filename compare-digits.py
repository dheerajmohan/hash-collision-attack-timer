# Program for comparing digest digits at various positions

import random
import hashlib
import time
import xlwt
from xlwt import Workbook
from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook("comparing_positions.xls")
wb = copy(rb)

sheet1 = wb.get_sheet(0)
sheet1.write(0, 0, "Taking single digits from 3,7,...,39")

list=[]
for p in range(40):
    if (p % 4) == 3:
        list.append(p)
for ch in range(1, 2):
    sheet1.write(4 * (ch+9) - 3, 0, "Number of characters = " + str(ch))
    sheet1.write(4 * (ch+9) - 2, 0, "POSITIONS")
    sheet1.write(4 * (ch+9) - 1, 0, "TIME")

    for i in range(5):
        randlist = random.sample(list, ch)
        total_time=0

        for j in range(100):
            start_time = time.time()
            collission = [0] * (2 ** (4 * ch))
            while 1:

                input = random.randint(1000, 100000000000000000000000000)
                result = hashlib.sha1(str(input).encode()).hexdigest()
                
                hashstr = ""
                for k in randlist:
                    hashstr = hashstr + str(result)[k]

                if collission[int(hashstr, 16)] == 1:
                    print("collision " + str(j + 1) + " in " + str(i + 1))
                    print(time.time() - start_time)
                    break
                else:
                    collission[int(hashstr, 16)] = 1

            final_time = (time.time() - start_time)
            total_time = total_time + final_time

        total_time = total_time/100
        sheet1.write(4 * (ch+9) - 2, i + 1, str(randlist))

        sheet1.write(4 * (ch+9) - 1, i + 1, total_time)

wb.save('comparing_positions.xls')

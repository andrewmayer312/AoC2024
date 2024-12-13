import numpy as np
import os

def determineSaftey(line_array: np.ndarray):

    length = line_array.size

    counterOne,counterTwo = 0,1
    indicator = 0
    

    while counterTwo < length:
        difference = abs(line_array[counterOne] - line_array[counterTwo])

        if difference < 1 or difference > 3:
            return 0
        else:
            if line_array[counterOne] > line_array[counterTwo] and indicator in (0, 1):
                indicator = 1
                counterOne += 1
                counterTwo += 1
                continue
            elif line_array[counterOne] < line_array[counterTwo] and indicator in (0, 2):
                indicator = 2
                counterOne += 1
                counterTwo += 1
            else:
                return 0

    return 1








def main():

    safeReportCount = 0

    with open("input.txt", "r") as file:
        for line in file:
            line_array = np.fromstring(line, dtype=int, sep = ' ')

            safeReportCount += determineSaftey(line_array)

    print(safeReportCount)






main()
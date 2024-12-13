import numpy as np


def isLevelDifSafe(rightLevel, leftLevel):
    if abs(leftLevel - rightLevel) > 3 or abs(leftLevel - rightLevel) < 1:
        return False
    else:
        return True


def isIncDecEven(rightLevel, leftLevel):
    if rightLevel - leftLevel >= 1:
        return -1
    elif rightLevel - leftLevel == 0:
        return 0
    else:
        return 1


def determineSafety(in_array, is_safety_used):


    m = 0

    # initial change of the array
    if in_array[0] - in_array[1] >= 1:
        m = -1
    elif in_array[0] - in_array[1] == 0:
        m = 0
    else:
        m = 1

    for x in range(in_array.size-1):
        current_m = isIncDecEven(in_array[x], in_array[x+1])
        if 0 < abs(in_array[x] - in_array[x+1]) < 4 and  current_m == m:
            if (x+1 == in_array.size):
                break
            else:
                continue
        # safety has been used
        elif is_safety_used == True:
            return 0
        # looking at the first two levels
        elif x == 0:

            if determineSafety(np.delete(in_array, x), True) == 1:
                return 1
            elif determineSafety(np.delete(in_array, x+1), True) == 1:
                return 1
            else:
                return 0
        # looking at last two levels
        elif x == in_array.size - 2:
            return 1
        # looking at two levels in between
        elif x == 1:
            if determineSafety(np.delete(in_array, x-1), True) == 1:
                return 1
            elif determineSafety(np.delete(in_array, x), True) == 1:
                return 1
            elif determineSafety(np.delete(in_array, x+1), True) == 1:
                return 1
            else:
                return 0
        else:

            if determineSafety(np.delete(in_array, x), True) == 1:
                return 1
            elif determineSafety(np.delete(in_array, x + 1), True) == 1:
                return 1
            else:
                return 0
    return 1






def main():
    safeReportCount = 0

    with open("input.txt", "r") as file:
        for line in file:
            line_array = np.fromstring(line, dtype=int, sep=' ')

            x = determineSafety(line_array, False)
            safeReportCount += x

    print(safeReportCount)



main()

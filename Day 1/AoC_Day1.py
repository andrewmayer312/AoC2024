import numpy as np



def main():
    File_Data = np.loadtxt("input.txt", dtype=int)


    x, y = File_Data.T

    x_sort = np.sort(x)
    y_sort = np.sort(y)

    similarity_score = 0

    for x_placeholder in x_sort:
        for y_placeholder in y_sort:
            if x_placeholder == y_placeholder:
                similarity_score += x_placeholder
            else:
                continue
    

    
    print(similarity_score)


main()
def main():

    operation_array = []

    result_sum = 0

    first_operand_added = False
    second_operand_added = False

    with open("Day 3\input.txt", "r") as file:
        #reading file by char
        while True:
            in_char = file.read(1)
            if not in_char:
                print("End of file")
                break
            
            #if char is m, check that next char is u
            if in_char == 'm' and not operation_array:
                operation_array.append(in_char)
                continue
            #if char is u, check that previous char is m and if not empty array
            elif in_char == 'u' and operation_array[-1] == 'm':
                operation_array.append(in_char)
                continue
            #if char is l, check that previous char is u and if not empty array
            elif in_char == 'l' and operation_array[-1] == 'u':
                operation_array.append(in_char)
                continue
            elif in_char == '(' and operation_array[-1] == 'l':
                operation_array.append(in_char)
                continue
            #first digit of first arguement 
            elif in_char.isdigit() and operation_array[-1] == '(':
                operation_array.append(in_char)
                first_operand_added = True
                continue
            elif in_char.isdigit() and operation_array[-1].isdigit() and first_operand_added == True:
                operation_array.append(in_char)
                continue
            elif in_char == ',' and operation_array[-1].isdigit() and first_operand_added == True:
                operation_array.append(in_char)
                first_operand_added == False
                continue
            elif in_char.isdigit() and operation_array[-1] == ',':
                operation_array.append(in_char)
                second_operand_added = True
                continue
            elif in_char.isdigit() and operation_array[-1].isdigit() and second_operand_added == True:
                operation_array.append(in_char)
                continue
            elif in_char == ')' and operation_array[-1].isdigit() and second_operand_added == True:
                operation_array.append(in_char)
                #call a function here to process the operation_array and add the result to 
            
            else:
                operation_array = []
                continue
            


           


main()
# I declare that my work contain no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20220659
# Date: 4/21/2023

# Importing the main code - PART 1/2/3
import Program_1

# Variables
dict = {}
start_value = 1
end_value = 4
count = 0
slicer = 0

# Iterating through the list and obtaining the student id for each data set
for element in Program_1.text_file_data:
    studentid = input(f"Enter the student ID for {Program_1.data_store[count]}: {', '.join(map(str, Program_1.data_store[start_value:end_value]))} :")
    studentid = str(studentid)  # Converting to a string
    if len(studentid) != 8:  # Checking if the ID has 8 digits
        print("Invalid input: Please enter your 8 digit ID")
        exit()
    listlements = Program_1.text_file_data[slicer]
    dict_elements = {f"{studentid}": f"{listlements}"}  # making the format and saving to a variable
    dict.update(dict_elements)  # adding to the dictionary
    start_value = start_value + 4  # Incrementing
    end_value = end_value + 4  # Incrementing
    count = count + 4  # Incrementing
    slicer = slicer + 1  # Incrementing

for key, value in dict.items():  # Printing out the dictionary through a loop
    print(key, "- ", value, end="  ")

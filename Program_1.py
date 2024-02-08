# I declare that my work contain no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20220659
# Date: 4/21/2023

# Variables
progress = 0
progress_module = 0
does_not_progress = 0
exclude = 0
count = 0
count_2 = 0
variable = 0
credit_scores = [0, 20, 40, 60, 80, 100, 120]
data_store = []
text_file_data = []
start_value = 1
end_value = 4


while count == 0:
    # Function collects data from user
    def get_credits():
        while count_2 == 0:
            pass_credit = int(input("Please enter your credit at pass: "))
            if pass_credit not in credit_scores:    # Checking for validation of the proper input for "pass_credit"
                print("\tOut of range")
                continue
            defer_credit = int(input("Please enter your credit at defer: "))
            if defer_credit not in credit_scores:     # Checking for validation of the proper input for "defer_credit"
                print("\tOut of range")
                continue
            fail_credit = int(input("Please enter your credit at fail: "))
            if fail_credit not in credit_scores:  # Checking for validation of the proper input for "fail_credit"
                print("\tOut of range")
                continue
            else:
                break   # Breaking of the loop if all the inputs are  valid
        return pass_credit, defer_credit, fail_credit

    try:
        pass_credit, defer_credit, fail_credit = get_credits()   # Calls the function and store the return values
    except ValueError:
        print("\tInteger required")     # Prints if inputs doesn't contain a integer value
        pass_credit, defer_credit, fail_credit = get_credits()

    if (pass_credit + defer_credit + fail_credit) != 120:  # Checking the total of the inputs
        print("\tTotal incorrect")
        pass_credit, defer_credit, fail_credit = get_credits()

    # Checking if the credits meets the "Progress"
    if pass_credit == 120 and defer_credit == 0 and fail_credit == 0:
        print("\tProgress")
        data_store.append("Progress")
        progress = progress + 1
    # Checking if the credits meets the "Progress Module trailer"
    elif pass_credit == 100 and defer_credit in (0, 20) and fail_credit in (0, 20):
        print("\tProgress Module trailer")
        data_store.append("trailer")
        progress_module = progress_module + 1
    # Checking if the credits meets the "Exclude"
    elif (pass_credit == 40 and defer_credit == 0 and fail_credit == 80) \
            or (pass_credit == 20 and defer_credit in (20, 0) and fail_credit in (80, 100)) \
            or (pass_credit == 0 and defer_credit in (0, 20, 40) and fail_credit in (80, 100, 120)):
        print("\tExclude")
        data_store.append("Exclude")
        exclude = exclude + 1
    else:
        # Checking if the credits meets "Module retriever"
        print("\tDoes not progress - Module retriever")
        data_store.append("retriever")
        does_not_progress = does_not_progress + 1

# Asking for user's verification to proceed
    print('''
    -------------------------------
    \tWould you like to enter another set of data?
    ''')

    loop_break = str(input("\tEnter 'y' for yes or 'q' to quit and view results: "))
    data_store.append(pass_credit)  # Saving  the credit scores accordingly
    data_store.append(defer_credit)
    data_store.append(fail_credit)
    if loop_break == "y":
        pass
    elif loop_break == "q":  # Breaking of the loop according to user's input
        count = 1


print("\t----------------------------")
print("Progress\t", progress, ":", "*"*progress)
print("Trailer  \t", progress_module, ":", "*"*progress_module)
print("Retriever\t", does_not_progress, ":", "*"*does_not_progress)
print("Excluded\t", exclude, ":", "*"*exclude)

# Part 2
# Function to Display stored credits
def get_store_credits():
    global start_value  # Making of local variables global
    global end_value
    for element in data_store:
        if element == "Progress":  # Checking for "Progress" element in the Spec list
            display_value = "Progress: " + ', '.join(map(str, data_store[start_value:end_value]))  # Organizing the proper format and saving into a variable
            print(display_value)
            text_file_data.append(display_value)
            start_value = start_value + 4  # Incrementing
            end_value = end_value + 4  # Incrementing
        elif element == "trailer":
            display_value2 = "trailer: " + ', '.join(map(str, data_store[start_value:end_value])) # Organizing the proper format and saving into a variable
            print(display_value2)
            text_file_data.append(display_value2)
            start_value = start_value + 4  # Incrementing
            end_value = end_value + 4  # Incrementing
        elif element == "Exclude":
            display_value3 = "Exclude: " + ', '.join(map(str, data_store[start_value:end_value])) # Organizing the proper format and saving into a variable
            print(display_value3)
            text_file_data.append(display_value3)
            start_value = start_value + 4  # Incrementing
            end_value = end_value + 4  # Incrementing
        elif element == "retriever":
            display_value4 = "retriever: " + ', '.join(map(str, data_store[start_value:end_value])) # Organizing the proper format and saving into a variable
            print(display_value4)
            text_file_data.append(display_value4)
            start_value = start_value + 4  # Incrementing
            end_value = end_value + 4  # Incrementing


# Asking for User's verification to proceed
answer = input(str('''--------------------------------------
\tWould you like to access the stored data [YES/NO]: '''))
if answer == "YES":
    get_store_credits()  # Calling the function
elif answer == "NO":
    pass
else:
    print("Invalid Answer")
    exit()
# Part 3
# Function to save the stored data into a file
def text_file():
    with open("output.txt", "w") as f:  # writing into a file name "output
        for element in text_file_data:  # Using loop to iterate over text data and write it on the file
            f.write(f"{element}\n")
        print("\tData has been Successfully stored in a textfile")  # displaying the data has been successfully written

# Asking for User's verification to proceed
answer = input(str('''--------------------------------------
\tWould you like to access the stored data in a textfile [YES/NO]: '''))
if answer == "YES":
    text_file()
elif answer == "NO":
    pass
else:
    print("Invalid Answer")
    exit()

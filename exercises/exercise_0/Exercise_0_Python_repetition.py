# # 0. User input for ETL Parameters
# # Ask the user for 2 inputs:

# # source file path
# # destination file path


# # source_path = input("Write your source path: ")
# # destination_file_path = input("Write your destination path: ")

# # print(f"source: {source_path}")
# # print(f"destination {destination_file_path}")


# # ----------------------------------------------------------------------------------

# # In order to maintain data quality, consistency and reliability, a system needs to validate that it conforms to certain predefined structure or format. This is called schema validation and you'll practice this in the following exercises.

# #   a) Create a dictionary that look like this

# # Key	Value
# # id	101
# # name	Erika
# # is_active	True
# # age	45


# my_dict_erika = {"id": 101, "name": "Erika", "is_active": True, "age": 45}


# # if type(my_dict["id"]) == int and type(my_dict["name"]) == str and type(my_dict["is_active"]) == bool and type(my_dict["age"]) == int:
# #     print(True)
# # else:
# #     print(False)

# my_list = list(my_dict_erika.values())
# # print(my_list)

# my_dict_marcus = {"id": 102, "name": "Marcus", "is_active": True, "age": 34}

# my_dict_david = {"id": 103, "name": "David", "is_active": False, "age": 29}

# my_dict_anna = {"id": 104, "name": "anna", "is_active": True, "age": 41.5}

# my_dict_ingrid = {"id": 106, "name": "Ingrid", "is_active": "NOPE", "age": 8}


# people = [
#     {"id": 102, "name": "Marcus", "is_active": True, "age": 34},
#     {"id": 103, "name": "David", "is_active": False, "age": 29},
#     {"id": 104, "name": "Anna", "is_active": True, "age": 41.5},
#     {"id": 106, "name": "Ingrid", "is_active": "NOPE", "age": 8},
# ]


# def test_if_dict_ok(list):
#    for person in list:
#     if (
#         type(person["id"]) == int
#         and type(person["name"]) == str
#         and type(person["is_active"]) == bool
#         and type(person["age"]) == int
#     ):
#         print(True)
#     else:
#         print(False)


# test_if_dict_ok(people)



# # ----------------------------------------------------------------------------------



# # 2. Data quality check
# # Create a function that checks a list that it contains exactly ten elements, and none of them contains None. 
# # If they contain None, print out an error message that says that it is invalid and print out what a valid format should be.

my_list = [1, "2", True, "sdg", 5, "6", False, "apple", 9.5, 10]

def check_list(lst):
    try:
        if None not in lst and len(lst) == 10:
            print(True)
        else:
            raise ValueError("The list must contain exactly 10 elements and must not include None.")
    except ValueError as e:
        print(f"Error: {e}")
    
check_list(my_list)
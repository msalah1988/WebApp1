# Function to Read/Write to a text file:
from streamlit import session_state


def update_todos(txt_file, mode, todos_p):
    """A Read & Write to Text File"""
    if mode == "r":
        with open(txt_file, mode) as todos_file_local:
            todos_p = todos_file_local.readlines()
    elif mode == "w":
        with open(txt_file, mode) as todos_file_local:
            todos_file_local.writelines(todos_p)
    return todos_p


# -------------------------------------------------- #
def avg(user_input):
    original_list = user_input.split(" ")
    new_list = [float(value) for value in original_list]
    average = sum(new_list) / len(new_list)
    return average


def water_state(temprature):
    if temprature <= 0:
        result = "Solid"
    elif 0 < temprature < 100:
        result = "Liquid"
    elif temprature > 100:
        result = "Gas"
    return result



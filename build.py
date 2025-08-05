'''
Description: 
    This script is designed to speed the construction of the 
    periodic-table.json file: the user enters element information, then the 
    program builds the JSON objects and adds them to the file.
Author: RainyCityCoder
Special thanks: rndpkt, Saad, Carcigenicate on Discord.
'''

import json

def read_data(filename):
    '''Reads data from JSON file into program

    Args:
        filename (str): name of JSON file program will work with

    Returns:
        list: list of JSON objects
    '''
    
    all_json_data = []
    
    try:
        with open(filename, 'r') as f:
            all_json_data = json.load(f)
    except Exception as ex:
        print("Error trying to open file: "+str(ex))
        quit()
    return all_json_data
        

def write_data(all_json_data, filename):
    '''Writes JSON data to JSON file

    Args:
        all_json_data (list): list of JSON objects
        filename (str): name of JSON file program will work with
    '''
    
    with open(filename, 'w') as f:
        json.dump(all_json_data, f, indent=2)
        print("Written to file")


def build_object(name, atomic_num, symbol, atomic_weight):
    '''Builds dictionary from user input

    Args:
        name (str): Name of element
        atomic_num (int): atomic number of element
        symbol (str): Symbol of element
        atomic_weight (float): Atomic weight of element

    Returns:
        dict: Object with element's data as key-value pairs
    '''
    return {"Name": name, 
            "Atomic Number": atomic_num, 
            "Symbol": symbol, 
            "Atomic Weight": atomic_weight}
    
    
def atomic_number_check(p = ''):
    '''Checks user-entered atomic number is integer

    Args:
        p (str, optional): user's entry. Defaults to ''.

    Returns:
        int: atomic number of element
    '''
    
    try:
        atomic_num = int(input(p))
    except ValueError:
        print("Error: Input must be a valid integer.")
    else: 
        return atomic_num
    
    
def atomic_weight_check(p = ''):
    '''Checks user-entered atomic weight is float

    Args:
        p (str, optional): user's entry. Defaults to ''.

    Returns:
        float: atomic weight of element
    '''
    
    try:
        atomic_weight = input(p)
        atomic_weight = float(atomic_weight)
    except ValueError:
        print("Error: Input must be a valid number.")
    else:
        return atomic_weight
    
    
def main_loop(json_data):
    '''Main program flow. Checks if user wants to continue, calls atomic number
    and atomic weight check functions. Calls build_object function to add user
    input to existing JSON data.

    Args:
        json_data (list): list of JSON objects
    '''
    
    while True:
        continue_inputs = input("Continue? (y/n): ")
        if continue_inputs == "n": break
        if continue_inputs != "y": continue
            
        atomic_num = atomic_number_check("Atomic Number: ")
        symbol = input("Symbol: ")
        name = input("Name: ")
        atomic_weight = atomic_weight_check("Atomic weight: ")
        
        new_object = build_object(name, atomic_num, symbol, atomic_weight)
        json_data.append(new_object)
    
    
def main():
    '''Calls main program functions
    '''
    all_json_data = read_data('periodic-table.json')
    main_loop(all_json_data)
    write_data(all_json_data, 'periodic-table.json')
    
    
if __name__ == '__main__':
    main()    
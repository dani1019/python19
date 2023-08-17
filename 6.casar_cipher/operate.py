changed_ascii_code = []

def move_ascii_code(type, ascii_code, move_number):
    #operate type is encode or decode
    #if type is encode plus ascii_code to move_number
    if type.lower() == "encode":
        for element in ascii_code:
            changed_ascii_code.append(chr(element + move_number))

    #if type is decode minus ascii_code to move_number
    elif type.lower() == "decode":
        for element in ascii_code:
            changed_ascii_code.append(chr(element - move_number))
    #if type is not encode or decode, display message "you must enter encode or decode."      
    else:
        print("you must enter encode or decode.")
    
    #changed ascii_code convert list to string
    changed_ascii_code_string = "".join(changed_ascii_code)
    print(f"{changed_ascii_code_string}")

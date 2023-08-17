import operate as op

type= input("Type 'encode to encrypt, type 'decode' to decrypt: ")
words = input("Type your message: ")
move_number = int(input("Type the shift number.: "))

#the ascii_code of letters
ascii_code = [ord(i) for i in words]

#save the ascii_code after move_number
op.move_ascii_code(type, ascii_code, move_number)


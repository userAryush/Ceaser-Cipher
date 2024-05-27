#Aryush_khatri_2408485



##This block imports the os module and defines a function welcome that prints a welcome message.
import os

def welcome():
    #printing welcome message
    print("Welcome to the Caesar Cipher\nThis program encrypts and decrypts text using Caesar Cipher.")
   
def enter_message():
    """The function "enter_message" does not take any parameters and does not return anything.
    Its main purpose is to gather user input to determine whether to encrypt or decrypt a message,
    also to receive the message and shift number."""
    filename = None  # Initialize filename here
    #Continuously executing a while loop until the user provides a valid mode.
    while True:
       
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")
## determine whether to encrypt or decrypt, and if the input should be read from a file or the console.
    source = input("Would you like to read from a file (f) or the console (c)? ").lower()

    if source == 'c':
        #Asking the user to input the message they wish to encrypt or decrypt.
        message = input("What message would you like to {} : ".format('encrypt' if mode == 'e' else 'decrypt')).upper()
#Continuously executing a while loop until the user provides a valid shift number
        while True:
            #handling error with try and except
            try:
                shift = int(input("What is the shift number: "))
                break
            except ValueError:
                print("Invalid Shift")
    elif source == 'f':
        #Continuously executing a while loop until the user provides a valid file name
        while True:
            #enter the file name from your directory
            filename = input("Enter a filename: ")
            #checking if the file exists
            if is_file(filename):
                break
            else:
                print("Invalid Filename")

        while True:
            try:
                shift = int(input("What is the shift number: "))
                break
            except ValueError:
                print("Invalid Shift")

        message = None
        #if source is neither c or f it will show invalid source
    else:
        print("Invalid Source")



    return mode, message, shift, filename
##The encrypt function takes a message and a shift as parameters and returns the encrypted message using the Caesar Cipher algorithm.
def encrypt(message, shift):
    """The function "encrypt" takes in two parameters,the purpose of this function is to encrypt messages by applying a shift number."""
    
    result = ""  #creating variable to store result
    for char in message:
        if char.isalpha():
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            result += encrypted_char
        else:
            result += char
    return result

def decrypt(message, shift):
    """The function "decrypt" takes in two parameters, the purpose of this function is to decrypt messages by applying a shift number."""
    #calling function encrypt as the logic remains same but instead of +shift it will be - shift so -shift has been passed in argument
    #The decrypt function utilizes the encrypt function by passing the original message and the negation of the shift. This effectively decrypts the message.
    return encrypt(message, -shift)
#The is_file function checks if a given filename exists in the current directory.
def is_file(filename):
    return os.path.isfile(filename)
##The process_file function reads messages from a file, encrypts or decrypts them based on the mode, and returns a list of processed messages.
def process_file(filename, mode, shift):
    if not is_file(filename):#checks if there is a file in the directory if not returns empty list[].
        print("File not found.")
        return []

    messages = []          # If the file exists, the function initializes an empty list called messages. It then opens the file in read mode ('r') using a with statement
    with open(filename, 'r') as file:
        for line in file:           #It iterates through each line in the file, strips leading and trailing whitespaces using strip(), and appends the cleaned line to the messages list.
            messages.append(line.strip())

    processed_messages = []  #After reading all the messages from the file, the function initializes an empty list called processed_messages.
    for message in messages:  #It then iterates through each message in the messages list.
        if mode == 'e': #If the mode is encryption ('e'), it calls the encrypt function on the message with the specified shift and appends the result to processed_messages.
            processed_messages.append(encrypt(message, shift))
        elif mode == 'd': #If the mode is decryption ('d'), it calls the decrypt function on the message with the specified shift and appends the result to processed_messages.
            processed_messages.append(decrypt(message, shift))
#returns the list of processed messages (processed_messages) back to the calling code.
    return processed_messages
#The write_messages function writes a list of messages to an output file named 'output.txt.'
def write_messages(messages):
    with open('output_2408485.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')
#The message_or_file function gathers user input to determine whether to encrypt or decrypt and if the input should be read from a file or the console.
            #It returns a tuple containing the mode, message, and filename.
def message_or_file():
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    source = input("Would you like to read from a file (f) or the console (c)? ").lower()

    if source == 'c':
        message = input("What message would you like to {} : ".format('encrypt' if mode == 'e' else 'decrypt')).upper()
        return mode, message, None
    elif source == 'f':
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("Invalid Filename")
        return mode, None, filename
    else:
        print("Invalid Source")
#The main block of code executes the program. It calls the welcome function, enters a loop to
#continuously process user input and perform encryption/decryption operations, and allows the user to encrypt or decrypt another message. The loop continues until the user chooses to exit.
if __name__ == "__main__":
    welcome()

    while True:
        mode, message, shift, filename = enter_message()

        if message:
            result = encrypt(message, shift) if mode == 'e' else decrypt(message, shift)
            print(result)
        elif filename:
            processed_messages = process_file(filename, mode, shift)
            write_messages(processed_messages)
            print("Output written to output.txt")

        another_message = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        while another_message not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")


        if another_message == 'n':
            print("Thanks for using the program, goodbye!")
            break

#The block ensures that the code within it will only run when the script is executed directly (not imported as a module).
#It includes the main logic of the program, prompting the user for input, performing encryption/decryption, and providing an option to continue or exit.
   

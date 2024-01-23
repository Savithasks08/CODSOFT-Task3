#A program to generate password
#Importing the 'random' and 'string' modules
import random
import string

#Function to get the length of the password
def get_length_of_password():

    #A variable that stores the given length of the password
    length_password = int(input("\nEnter the length of the password: "))
    return length_password

#End of get_length_of_password() function


#Function to generate a character 
def generate_character(length_password):
    #A if condition for checking the length of given password id not equal to zero
    if length_password!=0:
         # Access the characters to use in the password
        characters_password = string.ascii_letters+string.digits+string.punctuation+string.ascii_lowercase+string.ascii_uppercase
        # Use the random package for generating the password
        password = ''.join(random.choice(characters_password) for i in range(length_password))
        return password   
    
    else:
        return ""
     
#End of generate_character() function
     

#Function to display the password
def display_password(password):
    
    #A variable that stores the generated password
    display_password=password
    #The print statement to display the password[]
    print("\nYour Password : ",display_password)

#End of display_character() function
    

#Main program which generates and prints the password

length=get_length_of_password()
random_password=generate_character(length)
display_password(random_password)

#End of main program
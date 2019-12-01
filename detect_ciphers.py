### This is a python program to decode and detect the type of Ceasar Cipher ###

import sys
import detectlanguage
import config

detectlanguage.configuration.api_key = config.API_key

def produce_ciphers(x,shift_amount):

    ### Produces a cipher with the given shift amount ###

    # Create the dictionary mapping letters to the corresponding shifted letters

    alphabet = {}
    for i in range (65,91):
        if i + shift_amount > 90:
            change_index = 65 + ((i + shift_amount) % 90) - 1
        else:
            change_index = i + shift_amount
        alphabet[chr(i)] = chr(change_index)
    for i in range (97,123):
        if i + shift_amount > 122:
            change_index = 97 + ((i + shift_amount) % 122) - 1
        else:
            change_index = i + shift_amount
        alphabet[chr(i)] = chr(change_index)  

    # Traversing through the cipher string and shifting

    return_string = ""
    for i in x:
        if (i.isalpha()) == False:
            return_string += i
        else:
            return_string += alphabet[i]
    
    return return_string
            

def get_ciphers(cipher_string):

    # Dictionary is now created we can use this to produce ROTs of different numbers 

    ROT_list = []
   
    #Create 25 ROTs 

    for count in range(0,26):
        shift_length = count
        ROT_list.append(produce_ciphers(cipher_string, shift_length))

    # Add ROT_list to a dictionary with ROT indices

    ROT_dict = {}
    for i in range(0,len(ROT_list)):
        if i == 0:
            ROT_dict['ROT'+ str(0)] = ROT_list[i]
        else:
            ROT_dict['ROT'+ str(26 - i)] = ROT_list[i]
   
   # Tabulating confidence scores for languages detected as english

    english_ciphers = {}
    for key,value in ROT_dict.items():
        temp_dict = detectlanguage.detect(value)
        if temp_dict[0]['language'] == 'en':
            english_ciphers[key] = temp_dict[0]['confidence']

    # Obtaining the cipher with most confidence

    max_confidence = 0
    for i in english_ciphers.values():
        if i > max_confidence:
            max_confidence = i
    return_ROT = ""
    for key, value in english_ciphers.items():
        if value == max_confidence:
            return_ROT = key
            
 
    return return_ROT, ROT_dict[return_ROT]
    

if __name__ == "__main__":
    check_args = sys.argv
    if len(check_args) < 2:
        print("Insufficient arguments! Usage: python filename.py <Encrypted cipher>")
    else:

        # Obtaining the command line argument string

        temp = sys.argv
        cipher_string = ""
        for i in range(1,len(temp)):
            cipher_string += temp[i]
            cipher_string += " "
        cipher_type, decoded_text = get_ciphers(cipher_string)
        print("The Ceasar Cipher type is " + cipher_type + "!")
        print("The decoded text is '" + decoded_text + "'")

    



            

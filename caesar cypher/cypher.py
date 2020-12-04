# -*- coding: utf-8 -*-
"""
Created on Dec 1st 2020

A simple script to encode or decode a caesar cypher

@author: Ethan Bosworth
"""
#%% main code
def letter_check(letter):
    """Takes an imput and returns True if is a single charecter and not a number"""
    #check if length is greater than 1
    if len(letter) != 1:
        print('Please enter a single letter')
        test = False
    else: # try if it can be made into an integer
        try:
            letter =int(letter)
        except ValueError:
            test = True
        else:
            test = False

    return test

#create a while loop that will continue until a language is confirmed
lang_confirm = 0                    	
while lang_confirm == 0:
	print('Preset languages: English, Russian(Русский) ') #show preset languages
	alphabet = input('Enter your language from presets or type Other to add a new language: ')
	alphabet = alphabet.lower() #take input and convert the input to lowercase
	
    #if input is in presets return the alphabet and end the loop
	if alphabet in ('english' , 'en'):
		alphabet =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		lang_confirm = 1
	elif alphabet in ('russian' , 'ru' , 'русский' , 'рус'):
		alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
		lang_confirm = 1
	
    #if other is entered will create an alphabet
	elif alphabet == 'other': 
		missing_lang = 0 
		alphabet = [] #creates an empty alphabet to add to
		while missing_lang == 0: #create a while loop until the language is finalised
			print('Your current alphabet is ' + str(alphabet)) #print the current alphabet created
            #create an input of 4 possible actions to do
			action = input('\n Enter a new letter: 0 \n Change a letter: 1 \n Alphabet is complete: 3 \n Return: 4 \n ')
			
			if action == '4': #if need to return to preset alphabets
				missing_lang = 1
				continue
				
			if action == '0': #if a new letter is to be added
				letter = input('Please enter a new letter: ')
				#check it is a letter
				if letter_check(letter) == True:
					alphabet.append(letter) #if a letter then add to the alphabet
				else:
					print('Please enter a letter') #if not then do not add and ask for a letter
									
			if action == '1': #if a letter needs to be changed
				change = input('Select number of the letter to change') #ask for which number needs to be changed
				try: #make sure it is a number
					 num =int(change)
				except ValueError:
					print('Please enter a valid integer')
					continue
                #check the number is not already used in the alphabet with index 1
				if (int(change) > len(alphabet)) or (int(change) <= 0):
					print('number outside or range')
					continue
				else: #if number is used already then ask for the new letter and replace
					new_letter = input('Please enter the new letter')
					if letter_check(new_letter) == True:
						alphabet[int(change) -1] = new_letter
					
			if action == '3': #if alphabet is complete end both loops
				missing_lang = 1
				lang_confirm =1
			else: #if no option was chosen
				print('Please choose a valid option')
				
	else:
		print('Please choose a valid option')
		
#create a dictionary for alphabet to number and number to alphabet
dict_for = {}
dict_rev = {}

#loop over the alphabet to create both dictionaries
for i in range(len(alphabet)):
	dict_for[alphabet[i]] = i
	dict_rev[i] = alphabet[i]
	
def shift_cypher(cypher,k,shift):
    '''Input cypher, the size of the output and the shift to use and will shift the message '''
    output = [] #create an output variable
    for i in range(k): #for the length asked for
        letter = cypher[i] #take each letter of the message
        if letter == ' ': #if the letter is a space then add a space to the output
            output.append(' ')
        elif letter.isnumeric(): #if the letter is a number then shift the number by the shift given
            output.append(str(int(letter) + shift))
        else:
            #else convert the letter to a number, shift by the shift
            new_letter_num = (dict_for[letter] + shift) % len(alphabet) #% is needed incase the shift takes it past the last letter
            new_letter = dict_rev[new_letter_num] #convert back to a letter
            output.append(new_letter) #add letter to the output
				
        print('')
        print('With a shift of : ' + str(shift)) #write the shift used
        message = ''.join(output) #show the output as a string rather than an array
        print(message)
	
#ask if need encoding or decoding
encode_or_decode = int(input('Please enter 0 if you wish to encode and 1 if you wish to decode: '))
if (encode_or_decode != 1 & encode_or_decode != 0): #make sure a valid option is chosen
	encode_or_decode = input('Missing input. Please enter 0 if you wish to encode and 1 if you wish to decode: ')
	
#if to encode a cypher
if encode_or_decode == 0:
	cypher = input('Enter cypher text: ') #enter the text to encrypt and convert to lowercase
	cypher = cypher.lower()
	shift = int(input('Enter amount to shift by: ')) #enter shift amount
	shift_cypher(cypher,len(cypher),shift) #run the function to output the cypher
	

#if to decode
if encode_or_decode == 1:
	
    #enter the coded message
    cypher = input('Enter your Encrypted message: ')
	
    if cypher == 'test': #add a testing cypher to make testing easier
        cypher =  'Vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdlfkedqnbrxghflghrqldpvhmwlqjxsvdihkrxvhfr '
    cypher = cypher.lower() #convert input to lower
    #check if person knows encryption key
    code_decode = 0
    while code_decode == 0:
        key_check = input('Do you have the decryption key?  [yes/no] : ')
    	
        if key_check == 'yes':
    		#if encyption key is known then shift by negative of the key in the function to return the message
            shift = input('Input the correct shift: ')
            shift = int(shift)
            shift_cypher(cypher,len(cypher),-shift)
            code_decode = 1
    		
    		
        elif key_check == 'no': #if key is not known
            temp = 0
            while temp == 0: #create a loop for requency analysis
                check = input('Do you know the most common letter of your alphabet? [yes/no]:  ')
    	        #check if frequency analysis can be used
                if check == 'yes': #if yes then ask for the most common letter
                    top_letter = input('Input the most common letter: ')
                    if letter_check(top_letter) == True:
                        counts = [] #create an array to count each letter
                        for i in range(len(alphabet)):
                            count = 0 #for counting a letter
                            for j in range(len(cypher)): #add a count of each letter
                                if cypher[j] == alphabet[i]:
                                    count += 1
                                counts.append(count) #add letter count to the couns array
    
                        counts.index(max(counts)) #find the most common letter
                        letter - dict[top_letter] #find the shift of the most common letter in cypher to that of the language
                        (cypher,len(cypher),-shift) #run the function with the shift used
    
                        temp2 = 0 #create a loop for checking the key
                        while temp2 == 0:
                            check2 = input('Is this decryption correct? [yes/no]: ')
    						#ask if decryption was correct
                            if check2 == 'yes':
                                temp = 2 #if yes end the loop and stop running the script
                                code_decode = 0
                                break
                            elif check2 == 'no': #if no then end both loops
                                temp = 1
                                temp2 = 1
                            else:
                                print('Please enter a valid choice')
                    else: 
                        print('Please enter a letter')		
                elif check == 'no': #if most common letter is not known end loop
                    temp = 1
                else:
                    print('Please input a valid choice')
    			
    				
                if temp == 1: #temp 1 is given when fequency analysis did not work
                    if len(cypher) >= 10: #if the message is long then just work on the first k values
                        k = 10
                    else: 
                        k = len(cypher)
    				#run the shift cypher function for each possible shift in the alphavet
                    for i in range(len(alphabet)):
                        shift_cypher(cypher,k,i) #eg in english will return 26 possible shifts
                    test3  = 0
                    while test3 == 0:
                        shift = input('Input the correct shift from the list: ')
    					#ask for the correct shift based on what was shown
                        try: #check it is a number
                            shift = int(shift) 
                        except ValueError:
                            print('Please enter a number')
                        else: #if is a number then decrypt the while message using this shift
                            shift_cypher(cypher,len(cypher),shift)
                            test3 = 1
                            code_decode = 0
                                                            
        else: 
            print("Please enter a valid option")
                                                                       				
    	
    	
    	
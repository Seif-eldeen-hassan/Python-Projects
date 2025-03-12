

# Function to check if a binary number is valid
def Check_Binary_num(number):
 count = 0 
 i = 0 
 while count < len(number):
    if number[i] != "0" and number[i] != "1":
        print("\nInvalid number. \n")
        number = input("\nPlease Enter a Binary number\n ")
        
        
    else:
        i += 1
        count += 1
 return(number)
      

def First_complement(number):
 length = len(number)
 i = 0
 First_complement = ""
 while i < length:
    if number[i] =="0":
        First_complement = First_complement + "1"           # >>>>>>>>> Function to calculate the 1's complement of a binary number
        i+= 1
    elif number[i] == "1":
        First_complement = First_complement + "0" 
        i += 1
 return(First_complement)
#Remove the comment to test the function >>> output = 01010
#print("The 1st complement is:" , First_complement ("10101"))

def Second_complement(number):
 i = -1 
 count = 0 
 second_complement =""
 length = len (number)
 while count < length :
    if number[i] == "0":
        second_complement = "0" + second_complement
        i = i - 1 
        count = count + 1                                    # >>>>>>>>> Function to calculate the 2nd complement of a binary number
    elif number[i] == "1":
        second_complement = "1" + second_complement
        break
 numbers_after_one = number[0:i]    
 second_complement = First_complement((numbers_after_one)) + second_complement
 return(second_complement)              
#Remove the comment to test the function >>> output = 01011
#print("The 2nd complement is:" , Second_complement ("10101"))

def Addition(First_number , Second_number):
 len_num1 = len (First_number)
 len_num2 = len (Second_number)
 if len_num1 < len_num2 :
    First_number = ("0"*(len_num2 - len_num1)) + First_number
 else:
    Second_number = ("0"*(len_num1 - len_num2)) + Second_number  
 length = len(First_number)    
 Result = ""
 Carry = 0 
 bit_sum = "" 
 i = -1                                                                         # >>>>>>>>> Function to perform Binary Addition
 count = 0  
 while count < length:
    bit_sum = int(First_number[i]) + int(Second_number[i]) + Carry
    Result = str(bit_sum % 2) + Result    # Build the result bit by bit
    Carry = bit_sum // 2
    i = i - 1
    count = count + 1
 if Carry:
        Result = "1" + Result    # If there is a carry after processing all bits, add it to the leftmost position
 return(Result)  
#Remove the comment to test the function >>> output = 1001
#print("The Sum is:" , Addition ("101" , "100"))

def Subtraction(First_number , Second_number):
 len_num1 = len (First_number)
 len_num2 = len (Second_number)
 if len_num1 < len_num2 :
    First_number = ("0"*(len_num2 - len_num1)) + First_number
 else:
    Second_number = ("0"*(len_num1 - len_num2)) + Second_number
 length = len(First_number)   
 Result = ""
 Carry = 0 
 bit_sub = "" 
 i = -1
 count = 0  
 while count < length:                                                  # >>>>>>>>> Function to perform Binary Subtraction
    bit_sub = int(First_number[i]) - int(Second_number[i]) - Carry
    if bit_sub < 0 :
        bit_sub += 2
        Carry = 1
    else: 
        Carry = 0   
    Result = str(bit_sub) + Result
    count += 1
    i -= 1 
 return(Result)      
#Remove the comment to test the function >>> output = 0111
print("The Result of Binary subtraction is:" , Subtraction ("1010" , "11"))


# Main loop for the binary calculator
while True:
    print("\n** binary calculator **\n")
    print("A) Insert new numbers")
    print("B) Exit")
    Choise = input("\nPlease Type 'A' or 'B'\n").upper()
    if Choise == "A":
        First_number = (input("Please insert a binary number\n"))
        number = First_number 
        First_number = Check_Binary_num(number)
        while True:    
         print("\n** please select the operation **\n")
         print("A) Compute one's complement")
         print("B) Compute two's complement")
         print("C) Addition")
         print("D) Subtraction\n")
         Operation = input("\nPlease choose the operation\n").upper()
         if Operation == "A" or Operation == "B" :
            break
         elif Operation == "C" or Operation == "D":
          Second_number = (input("Please enter the Second number\n"))
          number = Second_number
          Second_number = Check_Binary_num(number) 
          break
         
         else:  print("\nPlease enter a valid choice\n")

        if Operation == "A":
           print("The 1st Complement is: ", First_complement(number))
        elif Operation == "B":
           print("The 2nd Complement is: ", Second_complement(number))
        elif Operation == "C":
           print("The sum is:" , Addition(First_number , Second_number))
        elif Operation == "D":
           print("The Result of Binary subtraction is:" , Subtraction(First_number , Second_number))   
           
    elif Choise == "B": 
       print("\n Exiting the program \n")   
       break
    else:
       print("Please enter a valid choise")

         
         
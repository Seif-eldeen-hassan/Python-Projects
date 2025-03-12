

def Binary_to_Decimal(number):
 power = 0 
 sum = 0 
 length = len (str(number))                      #>>>>>>>>>>>>>> A function take a binary number and convert it in to decimal number
 while power < length:
  sum = sum + ((2**power)*(int(number)%10))
  power = power +1 
  number = int(number) // 10
 return(sum)
#Remove the comment to test the function >>> output = 10 
#print("The Decimal is:" , Binary_to_Decimal(1010))

def octal_to_Decimal(number):
 power = 0 
 sum = 0 
 length = len (str(number))                      #>>>>>>>>>>>>>> A function take a octal number and convert it in to decimal number
 while power < length:
  sum = sum + ((8**power)*(int(number)%10))
  power = power +1 
  number = int(number) // 10
 return(sum)
#Remove the comment to test the function >>> output = 83
#print("The Decimal is:" , octal_to_Decimal(123))

def Decimal_to_Binary(number):
 Binary_number = ""
 number = int(number)
 while number > 0:
      reminder = number % 2
      Binary_number = str(reminder) + Binary_number  #>>>>>>>>>>>>>> A function take a Decimal number and convert it in to Binary number
      number //= 2
 return(Binary_number)
#Remove the comment to test the function >>> output = 1010
#print("The Binary  is:" , Decimal_to_Binary(10))

def Decimal_to_Octal(number):
 octal_number = ""
 number = int(number)
 while number > 0:
      result = number // 8
      reminder = number % 8
      octal_number = str(reminder) + octal_number   #>>>>>>>>>>>>>> A function take a Decimal number and convert it in to Octal number
      number //= 8
      if result == 0:
        break
 return(octal_number)
#Remove the comment to test the function >>> output = 12
#print("The Octal number is:" , Decimal_to_Octal(10))

remainder = []
def Decimal_to_Hexadecimal(number):
 number = int(number)
 while number > 0:
    remainder_number = number % 16
    if remainder_number == 10:
        remainder.append("A")
    elif remainder_number == 11:
        remainder.append("B")
    elif remainder_number == 12:
        remainder.append("C")
    elif remainder_number == 13:            #>>>>>>>>>>>>>>> A function take a decimal number and convert it to a Hexadecimal number
        remainder.append("D")
    elif remainder_number == 14:
        remainder.append("E")
    elif remainder_number == 15:
        remainder.append("F")
    elif remainder_number < 10:
        remainder.append(str(remainder_number))
    number = number // 16
 remainder.reverse()
 hexadecimal_number = ''.join(remainder)
 return(hexadecimal_number)
#Remove the comment to test the function >>> output = A
#print("The Hexadecimal number is:" , Decimal_to_Hexadecimal(10)) 

def Octal_to_Binary(number):
    num = ""
    number_after_conversion = ""
    while int(number) > 0:
        if int(number) % 10 not in [1, 2, 3 , 0 ]:
            num = str(Decimal_to_Binary(number % 10))
        else:
            if int(number) % 10 == 1:
                num = "001"
            elif int(number) % 10 == 2:                                 #>>>>>>>>>>>>>> A function take a Octal number and convert it in to Binary number
                num = "010"
            elif int(number) % 10 == 3:
                num = "011"
            elif int(number) % 10 == 0:
                num = "000"   
        number_after_conversion = num + number_after_conversion
        number = int(number) // 10
    return(number_after_conversion)
#Remove the comment to test the function >>> output = 1000
#print("The Binary number is:" , Octal_to_Binary(10)) 

def Binary_to_Hexadecimal(number):
 hexa_number = ''
 number = int(number)
 while number > 0:
    Decimal_number =Binary_to_Decimal(number % 10000)
    hexa_number = (str(Decimal_to_Hexadecimal(Decimal_number))) + hexa_number    #>>>>>>>>>>>>>> A function take a Binary number and convert it in to Hexadecimal number
    number //= 10000
 return(hexa_number)
#Remove the comment to test the function >>> output = 2
#print("The Hexadecimal number is:" , Binary_to_Hexadecimal(10)) 

def Binary_to_octal(number):
 octal_number = ''
 number = int(number)
 while number > 0:
    Decimal_number = Binary_to_Decimal(number % 1000)                             #>>>>>>>>>>>>>> A function take a Binary number and convert it in to Octal number
    octal_number = str(Decimal_number) + octal_number
    number //= 1000
 return(octal_number)
#Remove the comment to test the function >>> output = 4
#print("The Octal number is:" , Binary_to_octal(100)) 

def Hexadecimal_to_Decimal(number):
 Hexa_number = []
 i = 0
 length = len(number)
 while i < length:
    if number[i] == "A":
        Hexa_number.append(10)
    elif number[i] == "B":
        Hexa_number.append(11)
    elif number[i] == "C":
        Hexa_number.append(12)
    elif number[i] == "D":
        Hexa_number.append(13)
    elif number[i] == "E":
        Hexa_number.append(14)                                                   #>>>>>>>>>>>>>> A function take a Hexadecimal number and convert it in to Decimal number
    elif number[i] == "F":
        Hexa_number.append(15)
    else:
        Hexa_number.append(int(number[i]))
    i += 1
 index = -1   
 power = 0
 total_sum = 0
 while power < len(Hexa_number):
    total_sum += Hexa_number[index] * (16 ** power)
    power += 1
    index -= 1
 return(total_sum)
#Remove the comment to test the function >>> output = 171
#print("The Decimal number is:" , Hexadecimal_to_Decimal("AB")) 

def Hexadecimal_to_Binary(number):
  length_number = len(number)
  new_number = ""
  index = 0
  count = 0
  binary_num = ""
  nums = []
  while index < length_number:
    nums.append(number[index])
    index += 1
  while count < length_number:
          # The compiler cleared the zero from the left, so I had to save its value
          if (nums[length_number-1])== '0':binary_num = "0000"
          elif (nums[length_number-1])== '1':binary_num = "0001"
          elif (nums[length_number-1]) == '2':binary_num = "0010"
          elif (nums[length_number-1]) == '3':binary_num = "0011"
          elif (nums[length_number-1]) == '4':binary_num = "0100"
          elif (nums[length_number-1]) == '5':binary_num = "0101"
          elif (nums[length_number-1]) == '6':binary_num = "0110"             
          elif (nums[length_number-1]) == '7':binary_num = "0111"                   #>>>>>>>>>>>>>> A function take a Hexadecimal number and convert it in to Binary number
          elif (nums[length_number-1]) == '8':binary_num = "1000"
          elif (nums[length_number-1]) == '9':binary_num = "1001"
          elif (nums[length_number-1]) == 'A':binary_num = "1010"
          elif (nums[length_number-1]) == 'B':binary_num = "1011"
          elif (nums[length_number-1]) == 'C':binary_num = "1100"
          elif (nums[length_number-1]) == 'D':binary_num = "1101"
          elif (nums[length_number-1]) == 'E':binary_num = "1110"
          elif (nums[length_number-1]) == 'F':binary_num = "1111"
          new_number = binary_num + new_number
          length_number -= 1
  return(new_number)
#Remove the comment to test the function >>> output = 1010
#print("The Binary number is:" , Hexadecimal_to_Binary("A")) 

# ********* Combined Functions *********  
#  1) Octal >> Hexadecimal function : used in line 252
#Remove the comment to test the function >>> output = 8
#print("The Hexadecimal number is:" , Decimal_to_Hexadecimal(octal_to_Decimal(10))) 

#  2) Hexadcimal >> Octal function : used in line 264
#Remove the comment to test the function >>> output = 12
print("The Octal number is:" , Decimal_to_Octal(Hexadecimal_to_Decimal("A")))


while True:
  print("\n ***numbering system converter*** \n")
  print("A) insert a new number")
  print("B) Exit program\n")
  Choise = input("Please choose 'A' or 'B'\n").upper()
  if Choise == "A":
      number = (input("\nPlease insert a number\n"))
      while True:
         print(" \n**Please select the base you want to convert a number from**\n")
         print("A) Decimal")
         print("B) Binary")
         print("C) octal")
         print("D) hexadecimal")
         Base_Convert_from = input("\nPlease choose a numbering system\n").upper()
         if Base_Convert_from == 'A' or Base_Convert_from == 'B' or Base_Convert_from == 'C' or Base_Convert_from == 'D':
           break
         else: print("\nPlease enter a valid choise\n")
         
      while True:
         print(" \n**Please select the base you want to convert a number to** \n")
         print("A) Decimal")
         print("B) Binary")
         print("C) octal")
         print("D) hexadecimal")
         Base_Convert_to =input("\nPlease choose a numbering system \n").upper()
         if Base_Convert_to == 'A' or Base_Convert_to == 'B' or Base_Convert_to == 'C' or Base_Convert_to == 'D':
           break
         else: print("\nPlease enter a valid choice\n")

      if Base_Convert_from == "B" and Base_Convert_to =="A":
            bin_to_dec = Binary_to_Decimal(number)
            print("The Decimal number is:" , bin_to_dec)
      elif Base_Convert_from == "C" and Base_Convert_to == "A":
            oct_to_dec = octal_to_Decimal(number)
            print("The Decimal number is:", oct_to_dec)
      elif Base_Convert_from == "A" and Base_Convert_to == "B":
            dec_to_bin = Decimal_to_Binary(number)
            print("The Binary number is:" , dec_to_bin )
      elif Base_Convert_from == "A" and Base_Convert_to == "C":
            dec_to_oct = Decimal_to_Octal(number)
            print("The Octal number is:" , dec_to_oct)
      elif Base_Convert_from == "A" and Base_Convert_to == "D":
            dec_to_hex = Decimal_to_Hexadecimal(number)
            print("The Hexadecimal number is:", dec_to_hex)
      elif Base_Convert_from == "C" and Base_Convert_to == "B":
            octa_binary = Octal_to_Binary(number)
            print("The Binary number is:", octa_binary)
      elif Base_Convert_from == "C"  and Base_Convert_to =="D":
            print("The Hexadecimal number is:" , Decimal_to_Hexadecimal(octal_to_Decimal(number))) # Using the function "octal_to_Decimal" to convert the octal to decimal 
            #then Decimal_to_Hexadecimal Function to convert the decimal to hexadecimal      
      elif Base_Convert_from == "B"  and Base_Convert_to == "D":
            Bin_to_Hex = Binary_to_Hexadecimal(number)
            print("The Hexadecimal number is:" , Bin_to_Hex)     
      elif Base_Convert_from == "B"  and  Base_Convert_to == "C" :
            bin_to_octal = Binary_to_octal(number)
            print("The Octal number is:" , bin_to_octal)
      elif Base_Convert_from == "D" and Base_Convert_to == "A":
          hex_to_decimal = Hexadecimal_to_Decimal(number)
          print("The Decimal number is:", hex_to_decimal )   
      elif Base_Convert_from == "D" and Base_Convert_to == "C":
            print("The Octal number is:" , Decimal_to_Octal(Hexadecimal_to_Decimal(number)) )  # Using the function "Hexadecimal_to_Decimal" to convert the hexadecimal to decimal 
            #then Decimal_to_Octal Function to convert the decimal to octal
      elif Base_Convert_from == "D" and Base_Convert_to == "B":
           hex_to_bin = Hexadecimal_to_Binary(number)  
           print("The Binary number is:" , hex_to_bin)    

  elif    Choise == "B":
     print("Exiting the program") 
     break
  else:
      print("please select a valid choice")
      


  
#import the necessary modules!
import random
import string

print('Welcome to Password generator!')

#input the length of password
length = int(input('Enter Password length: '))                      

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#string.ascii_letters

#combine the data
all = lower + upper + num + symbols

#use random 
temp = random.sample(all,length)

#create the password 
password = "".join(temp)

#print the password
print(f"Password: {password}")
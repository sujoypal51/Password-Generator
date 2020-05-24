#generate weak, medium, strong password 
import random

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                     'v', 'w', 'x', 'y', 'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U',
                     'V', 'W', 'X', 'Y', 'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')']

def password_generator(p,l,s) :
	random.shuffle(s)    
	while len(p) < l :
		p += random.choice(s)
	a = []
	for i in p :
		a.append(i)
	random.shuffle(a) 
	p = ""
	for i in a :
		p += i
	return p	
	
print("Select Password Strength :\n1. Weak\n2. Medium\n3. Strong")
ch = int(input("Enter Choice : "))
if ch == 1 :
	pass_length = 8
	password = random.choice(LOCASE_CHARACTERS)*2 + random.choice(UPCASE_CHARACTERS)*2 #contain atleast one character from each set
	combined = list((LOCASE_CHARACTERS+UPCASE_CHARACTERS))
	key = password_generator(password,pass_length,combined)
elif ch == 2 :
	pass_length = random.randint(9,12)
	password = random.choice(DIGITS) + random.choice(LOCASE_CHARACTERS) + random.choice(UPCASE_CHARACTERS) #contain atleast one character from each set
	combined = list((DIGITS+LOCASE_CHARACTERS+UPCASE_CHARACTERS))
	key = password_generator(password,pass_length,combined)
else :
	pass_length = 13
	password = random.choice(DIGITS) + random.choice(LOCASE_CHARACTERS) + random.choice(UPCASE_CHARACTERS) + random.choice(SYMBOLS) #contain atleast one character from each set
	combined = list((DIGITS+LOCASE_CHARACTERS+UPCASE_CHARACTERS+SYMBOLS))
	key = password_generator(password,pass_length,combined)

print(key)
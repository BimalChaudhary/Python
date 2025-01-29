'''
2. Write a program to fill in a letter template given below with name and date.
letter = 
Dear <|Name|>,
You are selected!
<|Date|>
'''

name = input("Enter you name :")
date = input("Enter your Date :")
letter = f'''
Dear {name}
You are selected in
{date}
'''
print(letter)
# SINGLE LINE COMMENT
letter = 'P'                
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  
print(greeting)             
print(len(greeting))        
sentence = ("I hope you were expecting another", greeting)
print(sentence)

# MULTILINE STRINGS
multiline_string = '''I am still learning python.
My name is Chase'''
print(multiline_string) # can de done with ''' ''' or """ """

# STRING CONCAT
first_name = 'Chase'
last_name = 'Simmons'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) 

# len() returns length
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # False
print(len(full_name)) # 15

# CHARACTER UNPACKING
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# STRING INDEXING
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# REVERSE INDEXING
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon

last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# SKIP WHILE SPLICING
language = 'Python'
pto = language[0:6:2] # [0 - start: 6 - end: 2 - every [num] grab]
print(pto) # pto

# ESC SEQUENCE
print('I hope this is another hello world!.\nIs it?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')
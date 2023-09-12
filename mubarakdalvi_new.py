# code for finding words in re
import re
s = 'I live in Dapoli'
print(re.findall('[A-Z][a-z]*', s))

# code for checking for checking fisrt three alphabet is Capital or not
import re
s = ['TECHNOGEEKS', 'Institute', 'IE', 'A', 'GOOD', 'Institute']
filter_string = [string for string in s if re.match('^[A-Z]{3}',string)]
print(filter_string)

# code for checking  len and first capital letter of the list
import re
input1 = 'I live in Pune and Pune is in Maharashtra'
x = re.findall('[A-Z][a-z]*',input1)
print(x,len(x))

# Display all the numbers in output and Display output in the form of dict
# where first number will come with key primary_number and second number will come as emergency_number
import re
input1 = 'my contact number is 1111 and my emergency contact number is 2222'
x = re.findall('[0-9]+', input1)
print('my first number is key primary_number which is', {x[0]}, 'my second number is emergency_number which is ', {x[1]})

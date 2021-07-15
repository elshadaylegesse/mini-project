countries =['India', 'Denmark', 'Ghana', 'India', 'Maldives', 'US', 'India', 'Angola']
print(len(countries))
country_set = set(countries)
print(len(country_set))

country_set.add('Italy')
print(country_set)

print('Ethiopia' in country_set)

print('\n')


numbers = [1, 2, 3, 4, 3, 2, 1, 1]
unique_nums = set(numbers)
print(unique_nums)

unique_nums.add(11)
print(unique_nums)

unique_nums.pop()
print(unique_nums)

print('\n')

a = [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4 ,5]
b = set(a)
print(b)
print(len(a) - len(b))
b.add(9)
print(b)


print('\n')

####Dictionaries


elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}

print(elements['helium'])

print('\n')

##updating by adding one at a time

elements['Oxygen']=8

##updating by passign dictionary
elements.update({'nitrogen': 7, 'lithium': 3, 'sodium': 11})

print(elements)

##updating by passing iterables

new_elements_itr = (('boron', 5), ('potassium', 10), ('calcium', 20))

elements.update(new_elements_itr)

print('update by passing iterables')
print(elements)

#update using keyword arguments

elements.update(beryllium = 4, phosphorus = 15, aluminium = 13)
print(elements)


print('argon' in elements)

print('hydrogen' in elements)

print('helium' in elements)

print(elements.get('iron'))

print(elements.get('cobalt'))

print(elements.get('kryptonite', 'thats a fake element!!!!'))



cities = {'Brazil': {'capital': 'Brasilia', 
'sea': 'yes', 
'good food': 'yes',
'climate': 'very hot'},

 'Ethiopia': {'capital': 'Addis ababa',
 'sea': 'no',
 'good food': 'fuck yes',
 'climate': 'tropical and mild'}}
 
print(cities)

print('\n')
 
 
 
 
phone_balance = 3
bank_balance = 100
 
print(phone_balance, bank_balance)
 
 
if phone_balance < 5:
 phone_balance += 10
 bank_balance -= 10
 	
print(phone_balance, bank_balance)

print('\n')


n = 4

if n % 2 == 0:
	print('Number ' + str(n) + ' is even.')
else:
	print('Number ' + str(n) + ' is odd.')
	

n = 15

if n % 2 == 0:
	print('Number ' + str(n) + ' is even.')
else: 
	print('Number ' + str(n) + ' is odd')


print('\n')

season = 'winter'

if season == 'spring':
	print('plant the garden')
elif season == 'summer' :
	print('water the garden')
elif season == 'fall':
	print('harvest the garden')
elif season == 'winter':
	print('go indoors and read')
else:
	print('unrecognised')
	



weight = 84
height = 163

if 18.5 <= (weight/height **2) <25:
	print('Your ass is fine.')
else:
	print('eat or do not eat please')
	

is_raining = True

if is_raining or is_sunny:
	print('where is the rainbow?')


unsubscribed = False 
location = 'USA'

if (not unsubscribed) and (location =='USA' or location == 'CAN'):
	print('send email')
	

	
if True:
	print('This indented code will always run but not useful as a condition')
	
weather = 'rain'	
	
if weather == 'snow' or 'rain':
	print('wear boots!')
	

is_cold = False
if is_cold == True: 
	print('the weather is cold!')
	
#good example

if is_cold: 
	print('the weather is cold brr!')

is_cold = True	
	
if not is_cold:
	print('fuck its hot')	
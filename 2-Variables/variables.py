first_name = 'Chase'
last_name = 'Simmons'
country = 'United States'
city = "Kansas City"
age = 23
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
  'firstName':first_name,
  'lastName':last_name,
  'country':country,
  'city':city
}

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

first_name, last_name, country, age, is_married = 'Chase', 'Simmons', 'United States', 23, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
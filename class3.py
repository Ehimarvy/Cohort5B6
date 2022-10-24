#string cocatenation
firstname ="marvelous"
lastname ="ehimwenma"
print(firstname +" " +lastname)

name=input("Tell us your name :")
year_of_birth=int(input("date of birth :"))
current_year=2022
age=current_year - year_of_birth
print(f"welcome,{name}. we can see that you are {age}years old.")


index
b="I am just good you know"
print(b[2])
print(b[5:9])
print(b[0:5] + " " +b[10:15])


first_name=input("tell us your first name :")
last_name=input("tell us your last name :")
user_name=(last_name[0:3] +""+first_name[1:4])
print(user_name)
#CORRECTION
username=last_name[:3] + first_name[-3:]
print(username)

# METHOD
name= 'marv'
f= name.upper()
print(f)
name="marvelous"
print(name.upper())
f="i am a good boy"
print(f.index('o'))
print(f.find('o'))
print(f.rfind('o'))
print(f.rindex('o'))
ball='i love messi'
print(ball.capitalize())
ball='i love rashford'
print(ball.split())
ball='i love messi'
print(ball.title())

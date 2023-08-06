file_text = open("blank.txt", "r")
text = file_text.read()
# open("blank.txt", "a")
# open("blank.txt", "r+")
#can create file with open w

print(file_text.readable())
print(file_text.read())
print(text)
file_text.close()
file_write = open("blank.txt", "w")
file_write.write(text + "456")
file_write.close()
file_text = open("blank.txt", "r")
print(file_text.read())
file_text.close()
file_write = open("blank.txt", "w")
file_write.write(text)
file_write.close()

any_var = "this be a variable yes"
print(any_var)
secret = "secret"
guess = ""
lenght = len(any_var)
any_var = input("the truth you seek? ")
lenght2 = len(any_var)
if lenght > lenght2 - 7:
    any_var = "this be a variable yes"
else:
    lenght = lenght2
print("hello bitch")
print("....")
print("wait")
print("who are \"you\"!")
print(any_var.upper().isupper())
print(any_var.upper())
print(lenght)
print(any_var[lenght - 5])
print(any_var.index("e"))
print(any_var[::-1])
last = lenght - 1 - any_var[::-1].index("e")
print(last)
print(any_var[last])

color = input("color: ")
plural_noun = input("plural noun: ")
people = input("people: ")

random_list = ["color:" + color, "people:" + people, "plural_noun:" + plural_noun, "any_var:" + any_var]

print(random_list)
print(random_list[1])
random_list.extend(random_list)
print(random_list)
print(random_list.index("color:" + color))

print("roses are " + color)
print(plural_noun + " are blue")
print("i love " + people)

count = 0
text = "make a guess: "
while secret != guess and count < 3:
    guess = input(text)
    if secret == guess:
        print("correct")
    else:
        print("wrong")
        text = "try again: "
        count = count + 1
if count == 3:
    print("YOU FAILURE!")
for letter in "failure!":
    print(letter)
for num in range(7, 1000000):
    print(num * (num - (num / 5)))
# try:
# code
# except:
# code
# try:
# code
# except type_of_error:
# code
# try:
# code
# except type_of_error as err:
# code err

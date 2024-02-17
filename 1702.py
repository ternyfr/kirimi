from random import randint
     
def GeneratePassword(max, sep):
     password = ""
     for i in range(0, max):
          password += chr(randint(65,122))
          if i % 5 == 0 and i > 0:
               password += "sep"
     return password 

print(GeneratePassword(5, "---"))
print(GeneratePassword(10, "+++"))
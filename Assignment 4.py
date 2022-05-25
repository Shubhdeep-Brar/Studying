password = input("Enter a password: ")
containsOnlyAlpgabet = False
atleast6Characters = False
combinationOfUpperAndLower = False
containsOnlyAlpgabet = password.isalpha()
if len(password)>=6:
    atleast6Characters=True
    
if not password.isupper() and not password.islower():
    combinationOfUpperAndLower = True
    
if containsOnlyAlpgabet and atleast6Characters and combinationOfUpperAndLower:
    print("Password is valid")
else:
    print("Password is Not valid")

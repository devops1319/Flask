import re
password = input("Enter string to test: ")
# Add any special characters as your wish I used only #@$
if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", password):
    print ("match")
else:
    print ("Not Match")
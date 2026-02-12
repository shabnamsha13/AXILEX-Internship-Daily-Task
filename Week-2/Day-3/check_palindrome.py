#Check whether a string is palindrome
text = input("Enter a string: ")

reverse = ""
i = len(text) - 1

while i >= 0:
    reverse = reverse + text[i]
    i = i - 1

if text == reverse:
    print("It is a Palindrome")
else:
    print("It is Not a Palindrome")

# Get the string
string = input()

if string[0].isupper():
    print(string)
else:
    string = list(string)
    string[0] = chr(ord(string[0])-32)
    print("".join(string))
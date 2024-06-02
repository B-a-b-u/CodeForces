# Getting string1
str1 = input()

# Getting string 2
str2 = input()

# Converting string 1 and string 2 to lowercase letters
str1 = str1.lower()
str2 = str2.lower()

# Comparing two strings Lexicographically
if str1 < str2:
    print("-1")
elif str2 < str1:
    print("1")
else:
    print("0")
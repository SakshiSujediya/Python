str1 = input("Enter the string:-")
vowels = "a","e","i","o","u"
count =0 

for i in str1:
  if i in vowels:
     count = count + 1
     print(i)

print("count of vowels is",count)
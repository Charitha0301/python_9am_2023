#ps-- WAP to take dictionary from keyboard and print sum of values?

# d=eval(input('Enter Dictionary:'))
# sum = 0
# for item in d.items():
#     sum=sum+item[1]
# print('The sum:',sum)
# ------------------------------
 
# d=eval(input('Enter Dictionay:'))
# print('The sum:',sum(d.values()))

#WAP to find the no of occurences of each letter present in the given string?

# word=input("Enter any String:")
# d={}
# for ch in word:
#     d[ch]=d.get(ch,0)+1
# # print(d)

# for k,v in d.items():
#     print(k,'occurs',v,'times')

#WAP to find the no of occurences in each vowel present in the given string?

# word=input("Enter any String:")
# vowels={'a','e','i','o','u'}
# d={}
# for ch in word:
#     if ch in vowels:
#         d[ch]=d.get(ch,0)+1
#         # print(d)

# for k,v in sorted(d.items()):
#     print(k,'occurs',v,'times')






with open('dialogues.text','r') as file_data:
    pass

print(file_data.closed)

l=[1,2,3,4,5]
print(dic(l))
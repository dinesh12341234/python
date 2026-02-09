str1='abcdefgh'
c=0
v=0
for i in str1:
    if i=='a' or i=='e' or i=='o' or i=='u' or i=='i':
        v = v+1

    else:
       c=c+1
print(c)
print(v)
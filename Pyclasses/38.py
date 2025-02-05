val = input("Give the input: ")

i = 0
val2=''
while i<len(val):
    if  'A'<=val[i]<='Z':
        # print(val[i],end='')
        val2+=val[i]
    elif 'a'<=val[i]<='z':
        b=ord(val[i])-32
        b=chr(b)
        val2+=b
        # print(b,end='')
        #print(chr(ord(val[i])+32))

    i+=1

print(val2)

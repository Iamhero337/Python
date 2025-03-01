def countupper(s,count=0,i=0):
    if i >=len(s):
        return count
    if 'A'<=s[i]<='Z':
        count+=1
    return countupper(s,count,i+1)
print(countupper(input()))

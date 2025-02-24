def toupp(s, si=0, ei=0):
    if si==0:
        ei = len(s)-1

    out = ''

    for i in range(len(s)):
        if 'a'<=s[i]<='z' and si<=i<=ei:
            out+=s[i].upper
        else:
            out+=s[i]

        print(out)

toupp('hello* hI byE bye',1,13)

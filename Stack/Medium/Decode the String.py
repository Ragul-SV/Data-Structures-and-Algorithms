t = int(input())
for cases in range(t):
    s = input()
    st = []
    ch = []
    i = 0
    while i<len(s):
        if s[i].isdigit():
            temp = s[i]
            while i<len(s) and s[i+1].isdigit():
                temp+=s[i+1]
                i+=1
            st.append(temp)
        else:
            if s[i].isalpha() or s[i]=='[':
                ch.append(s[i])
            elif s[i]==']':
                temp = ""
                while ch[-1]!='[':
                    temp+=ch.pop()
                ch.pop()
                num = st.pop()
                temp = temp*int(num)
                for j in range(len(temp)-1,-1,-1):
                    ch.append(temp[j])
        i+=1
    temp = ""
    while ch:
        temp += ch[-1]
        ch.pop()
    print(temp[::-1])
                

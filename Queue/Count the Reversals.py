import math
t = int(input())
for cases in range(t):
    s = input()
    if len(s)%2!=0:
        print(-1)
    else:
        st = []
        for i in range(len(s)):
            if not st:
                st.append(s[i])
            elif st[-1]=='{' and s[i]=='}':
                st.pop()
            else:
                st.append(s[i])
        m = st.count('{')
        n = st.count('}')
        print(math.ceil(m/2)+math.ceil(n/2))

t = int(input())
for cases in range(t):
    n = int(input())
    n = (n<<4 & 0xFF) | n>>4
    print(n)

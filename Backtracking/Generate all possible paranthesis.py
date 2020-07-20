#-----------------------------------------O(2^N)-------------------------------------------------#
def Parenthesis(st,pos,n,openP,closeP,res):
    if closeP==n:
        res.append("".join(st))
        return
    if openP>closeP:
        st[pos]=')'
        Parenthesis(st,pos+1,n,openP,closeP+1,res)
    if openP<n:
        st[pos]='('
        Parenthesis(st,pos+1,n,openP+1,closeP,res)
        
    
def AllParenthesis(n):
    res = []
    st = [""]*2*n
    Parenthesis(st,0,n,0,0,res)
    return res

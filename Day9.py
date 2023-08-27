#16/8/2023
def countSubstring(S):
    ans, lower, upper = 0, 0, 0
 
    for i in range(len(S)):
        upper = 0
        lower = 0
 
        for j in range(i, len(S)):
            if S[j].isupper():
                upper += 1
            else:
                lower += 1
            if upper == lower:
                ans += 1
 
    return ans
 
S = "WomensDAY"
print("There are ",countSubstring(S)," of given string which satisfy the condition.")
def Palindrome(s):
    f=True
    size=len(s)//2
    string1=s[:size]
    string2=s[len(s):size-1:-1]
    for i in range(size):
        if string1[i]!=string2[i]:
            f=False
            break
    return f
    
if __name__=="__main__":
    ss=str(input())
    if Palindrome(ss):
        print("Palindrome")
    else:
        print("Not Palindrome")
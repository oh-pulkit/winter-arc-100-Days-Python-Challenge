#finding factorial

'''n = int(input())
product=1
for i in range(1,n+1):
    product = product*i

print(f"{n}! = {product}")'''

#pyramid star pattern

'''

  *
 ***
*****

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i), end = "")
    print("*"* (2*i-1))'''

#star pattern

'''n = int(input())
for i  in range(1,n+1):
    print("*"*i)
    i += 1'''

#square star pattern

n = int(input())
for i in range(1,n+1):
    if i == 1 or i == n:
        print("*"*n, end = "")
    else:
        print("*",end="")
        print(" "*(n-2), end = "")
        print("*",end="")  
    print("")      
   
    

    
    

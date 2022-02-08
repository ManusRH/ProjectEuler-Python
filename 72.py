from math import floor
from math import gcd
"""
def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount
"""
def computeTotient(n): 
  
    phi=[] 
    for i in range(n + 2): 
        phi.append(0) 
  
    for i in range(1, n+1): 
  
        phi[i] = i
   
    # Compute other Phi values 
    for p in range(2,n+1): 
      
        # If phi[p] is not computed already, 
        # then number p is prime 
        if (phi[p] == p): 
          
            # Phi of a prime number p is 
            # always equal to p-1. 
            phi[p] = p-1
   
            # Update phi values of all 
            # multiples of p 
            for i in range(2*p,n+1,p): 
              
                # Add contribution of p to its 
                # multiple i by multiplying with 
                # (1 - 1/p) 
                phi[i] = (phi[i]//p) * (p-1) 

    return phi 



d = 1000000
u = (d**2 - d)//2
p = computeTotient(d)

print(sum(p)-1)

# It's just the sum phi(2) + phi(3) + ... + phi(1000000)


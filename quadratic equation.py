def __main__(a,b,c):
    delta=(b**2)-4*a*c
    
    if delta<0:
        print("Not Have Reel")
    elif delta==0:
        print("x1=x2")
    else:
        x1=(-b+(delta**1/2))/(2*a)
        x2=(-b-(delta**1/2))/(2*a)
        
        print("""
                 X1= {}
                 X2= {}   
              """.format(x1,x2))              
                        
print("""
          ax^2+bx+c=0
          X1,x2 solve program
      """)              
a1=float(input("A: "))
b1=float(input("B: "))
c1=float(input("C: "))

__main__(a1, b1, c1)
    
    
          
    
          
          
          
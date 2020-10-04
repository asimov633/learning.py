numbers=[]
squares=[]
while True:
    number=input("Number: ")
    
    if number=="":
        break
    numbers.append(int(number))
    
for index in numbers:
    squares.append(index**2)
    
print("""
      Numbers List: {}
      Squares List: {}
      """.format(numbers,squares))
    
    

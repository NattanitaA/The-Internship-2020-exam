def prime(check):
    inputs=[int(check*10),int(check*100),int(check*1000)]
    for number in inputs:  
        if number > 1:
            for i in range(2,int(number/2)):
                if (number % i == 0):
                    print(number, "is not a Prime Number")
                    break
            else:
                print(number, "is a Prime Number")
                return True
        
    else:
        return False

check= float(input("Enter The Number: "))
while check != 0.0:
    floats = str(check)
    print(prime(check))
    break
    




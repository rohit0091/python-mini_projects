# calculate the factoiral of a given number 
# find the number of trailing zeros in that factorial of a given number

def cal_factorial(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n * cal_factorial(n-1)
    
def FactorialTrailingZeros(n):
    #fact = cal_factorial(n)
    count = 0
    i = 5
    # while fact % 10 == 0:
    #     count += 1
    #     fact = fact //  10   
    while( n//i != 0 ):
        count += int(n/i)
        i = i * 5
    return count

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    # fac = cal_factorial(n)
    # print(f"the factorial of {n} is {fac}")     # bigger number can't bgive the factorial .eg 10000 
    print(f"the number of trailing zeros in the factorial of {n} is {FactorialTrailingZeros(n)}")
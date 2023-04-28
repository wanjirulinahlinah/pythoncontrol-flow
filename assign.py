# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 



def even_numbers():
    n = 0
    while n < 50:
        n += 1
        if n % 2 == 0:
                continue
        print(n)

# Write a function that takes an integer argument and prints "Prime" if the number is prime, 
# and "Not prime" if the number is not prime.  
def intergers():
     x=range(30)
      for i in x:
        if i%2!=0:
            print(f"{i}is a prime number")
            else:
                print(f"{i}is not a prime number")


# Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.

def list of intergers():
    x=range(40)
    sums = 0
    for i in List:
        if i % 2 == 0 : 
            sums += i
            print(sums)

#  Write a function that takes any two integers as input, and prints the sum of all the numbers
#  between the two integers (inclusive) that are divisible by 3
def integers():
    for i in range(1, m+1):
        sum1 =0
        sum2 =0
        if i % n ==0:
            sum1 += i
            else:
                sum2 +=i
                print(f"{sum1} and {sum2}")
#Problem7.py
#Project Euler problem 7

from NumberTests import isEven


def main():
  primecount=0
  num=1
  while primecount<10001:
    num=num+1
    if isPrime(num):
      primeCount
  nums = fibonacciSequence(4000001)
  print (nums)
  total = 0
  for fib in nums:
    if isEven(fib):
      total = total + fib
  
  print(total) # final answer

if __name__ == '__main__':
  main()

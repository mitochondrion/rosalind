import sys

def fib(input):
  '''
  #1 Fibonacci Numbers
  '''
  result = 0
  prev = 1

  for i in range(input):
    prev, result = result, prev + result
    #print "{}: result: {}, previous: {}".format(i, result, previous_result)

  return result
  

def fib_r(input, prev=1, result=0):
  '''
  #1 Fibonacci Numbers (recursive)
  '''
  #print "{}: result: {}, previous: {}".format(input, prev, result)

  if input <= 0:
    return result

  return fib_r(input - 1, result, prev + result)


def fib_l(n, pad=""):
  '''
  #1 Fibonacci Number (abuse of recursion)
  '''
  print "{}l {}".format(pad, n)
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fib_l(n-1, pad + " ") + fib_r(n-2, pad + " ")


def fib_r(n, pad=""):
  print "{}r {}".format(pad, n)
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fib_l(n-1, pad + " ") + fib_r(n-2, pad + " ")




#!/usr/local/bin/python

import sys
import rosalind

def main(argv):
  args = argv[1:]
  n = int(args[0])
  print rosalind.fib(n)

if __name__ == "__main__":
  main(sys.argv)

"""
s = input()
t = input()
print s
print t
"""
import sys
input = sys.stdin.read()
data = list(input)
print data
del(data[-1])
print data
#for x in data:
#    print x,

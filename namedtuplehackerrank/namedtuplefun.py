# Enter your code here. Read input from STDIN. Print output to STDOUT 
from collections import namedtuple
N = int(input())
student = namedtuple('student',input().strip().split())
print(sum(float(student(*input().strip().split()).MARKS) for _ in range(N))/N)

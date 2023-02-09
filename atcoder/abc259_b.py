import math

a, b, d = map(int, input().split())

rad = math.pi*d/180
print(a*math.cos(rad) - b*math.sin(rad), a*math.sin(rad) + b*math.cos(rad))

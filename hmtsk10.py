
a = [input() for i in range(int(input()))]
a_ = a
n = 3
test_ = [f'{x}{y}' for y in range(1, n+1) for x in a_]
print(test_)
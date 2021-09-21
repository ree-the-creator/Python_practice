r = 5
print(range(r))

for i in range(5):
    print(i)
range(5, 10)

print(range(5, 10))
print(list(range(5, 10)))
print(list(range(10, 15)))
print(list(range(0, 10, 2)))

s = [0, 1, 4, 6, 13]
for i in range(len(s)):
    print(s[i])
    
t = [6, 372, 8862, 148800, 2096886]
for p in enumerate(t):
    print(p)
    
for i, v in enumerate(t):
    print(f"i = {1}, v = {v}")
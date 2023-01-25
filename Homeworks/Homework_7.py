lst = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
prime = []
composite = []
count = 0

for i in lst:
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0:
        prime.append(i)
        if 1 in prime:
            prime.remove(1)
    else:
        count = 0
        composite.append(i)

# print(prime)
# print(composite)

print('Min:', min(prime))
print('Max:', max(composite))
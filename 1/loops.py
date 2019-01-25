animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)

for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))

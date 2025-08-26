# Odd or Even Ascending order

print('------Odd or Even Ascending Order------')

numbers = [[],[]]

for c in range(0,7):
	value = int(input('Enter a number:\n'))
	numbers[0].append(value) if value % 2 == 0 else numbers[1].append(value)

numbers[0].sort()
numbers[1].sort()
print(f'The even values ​​entered were {numbers[0]}')
print(f'The odd values ​​entered were {numbers[1]}')
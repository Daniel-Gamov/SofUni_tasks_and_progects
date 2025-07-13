n = int(input())
numbers = [int(input()) for _ in range(n)]
max_number = max(numbers)
min_number = min(numbers)

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
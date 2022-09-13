import sys
arr = sys.argv[1].split(',')
my_numbers = [None]*len(arr)
for idx, arr_val in enumerate(arr):
    my_numbers[idx] = int(arr_val)

print(f'Before sorting {my_numbers}')

for k in range (0, len(my_numbers)):
    for m in range (k+1,len(my_numbers)):
        if my_numbers[k]>my_numbers[m]:
            temp= my_numbers[k]
            my_numbers[k]=my_numbers[m]
            my_numbers[m]=temp

print(f'After sorting {my_numbers}')
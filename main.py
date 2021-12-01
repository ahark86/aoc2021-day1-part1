running_total = 0

with open('input.txt') as input_file:
    input = [int(reading.strip()) for reading in input_file.readlines()]
    print(input)

compare_value = input[0]

for reading in input[1:]:
    if reading > compare_value:
        print(f'{reading} > {compare_value}: INCREASED')
        running_total += 1
    else:
        print(f'{reading} <= {compare_value}: DID NOT INCREASE')
    compare_value = reading

print(f'Times increased: {running_total}')
print(f'Total readings: {len(input)}')
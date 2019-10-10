#finding max and min elements from the list
def min_max(numbers):
    smallest=largest=numbers[0]
    for item in numbers:
        if item>largest:
            largest=item
        elif item<smallest:
            smallest=item
    return smallest,largest

print(min_max([2,3,4,1,55,23,45]))


def average(numbers):
    length = len(numbers)
    total = 0.0
    #print("before for loop", total)
    for number in numbers:
        total += number
        print("This is the total on every loop", total)
        return total/length
    
print(average([1, 5, 9]))
#print(average(range(11)))
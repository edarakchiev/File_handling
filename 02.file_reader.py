with open("numbers.txt", "r") as file:
    nums = [int((n[:-1])) for n in file]
    print(sum(nums))
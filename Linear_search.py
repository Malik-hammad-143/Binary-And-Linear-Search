def linearSearch(numbers, targetNum):
    for i in range(len(numbers)):
        # Print the current index and value being checked
        print(f"Checking index {i}, value: {numbers[i]}")

        if numbers[i] == targetNum:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

numbers = [12, 45, 23, 67, 34]
targetNum = 67

result = linearSearch(numbers, targetNum)

if result != -1:
    print("Value", targetNum, "found at index", result)
else:
    print("Value", targetNum, "not found")

def binarySearch(numbers, targetNum):
    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2
        print(f"Checking middle index {mid}, value: {numbers[mid]}")

        if numbers[mid] == targetNum:
            return mid  # Return the index if the target is found
        elif numbers[mid] < targetNum:
            print(f"Value {numbers[mid]} is less than {targetNum}, searching right half...")
            start = mid + 1
        else:
            print(f"Value {numbers[mid]} is greater than {targetNum}, searching left half...")
            end = mid - 1

    return -1  # Return -1 if the target is not found

numbers = [12, 23, 34, 45, 67]
targetNum = 67

result = binarySearch(numbers, targetNum)

if result != -1:
    print("Value", targetNum, "found at index", result)
else:
    print("Value", targetNum, "not found")

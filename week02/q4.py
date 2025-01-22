def processNumDecorator(func):

    def wrapper(numbers):
        print(f"Numbers: {numbers}")
        print(f"Count of Numbers: {len(numbers)}")
        print(f"Sum of Numbers: {sum(numbers)}")

        return func(numbers)
    return wrapper

@processNumDecorator
def processNum(numbers):
    print("Processing the numbers....")

numList = {10, 20, 30, 40}
processNum(numList)
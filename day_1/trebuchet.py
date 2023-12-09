
def process_line(line):

    # get the digits
    firstDigit = int(next(char for char in line if char.isdigit()))
    lastDigit = int(next(char for char in reversed(line) if char.isdigit()))

    # concatenate
    concatenated = int(str(firstDigit) + str(lastDigit))

    return concatenated

def main():
#    inputFilePath = "test.txt"
    inputFilePath = "input.txt"
    totalSum = 0

    try: 
        with open(inputFilePath, 'r') as file:
            for line in file:
                totalSum += process_line(line)

        print("Trebuchet coordinates: ", totalSum)

    except FileNotFoundError:
        print(f"Error: {inputFilePath} not found.")
    except Exception:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

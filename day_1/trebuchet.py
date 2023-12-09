def word_to_digit(word):

    wordToDigitMap = {
            'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
            'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    return wordToDigitMap.get(word.lower(), 0)

def process_line(line):

    wordToDigitMap = {
            'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
            'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    # get the digits
    firstDigit = word_to_digit(next((word for word in line.split() if word.isdigit() or word.lower() in wordToDigitMap), '0'))
    lastDigit = word_to_digit(next((word for word in reversed(line.split()) if word.isdigit() or word.lower() in wordToDigitMap), '0'))

    # concatenate
    concatenated = int(str(firstDigit) + str(lastDigit))

    return concatenated

def main():
    inputFilePath = "2test.txt"
#    inputFilePath = "input.txt"
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

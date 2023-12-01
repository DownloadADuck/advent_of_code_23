#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::string firstDigitFinder(std::string l);
std::string lastDigitFinder(std::string l);

int main() {
    std::string filePath = "input.txt";

    std::ifstream inputFile(filePath);

    int sum(0);
    std::string firstDigit, lastDigit;

    // check if file is opened properly
    if (!inputFile.is_open()) {
        std::cerr << "Error opening file: " << filePath << std::endl;
        return 1;
    }

    std::vector<std::string> lines;
    std::string line;

    while (std::getline(inputFile, line)) {
        lines.push_back(line);
    }

    inputFile.close();

    for (const auto& l : lines) {
        firstDigit = firstDigitFinder(l);
        lastDigit = lastDigitFinder(l);

        sum += std::stoi(firstDigit + lastDigit);
    }

    std::cout << "Trebuchet coordinates --> " << sum << std::endl;

    return 0;
}

std::string firstDigitFinder(std::string l) {
    std::string firstDigit;
    for (int i = 0; i <= static_cast<int>(l.length()); i++) {
        if ( l[i] >= 0  && l[i] <= 9) {
            firstDigit = std::to_string(l[i]);
            std::cout << "firstDigit --> " << firstDigit << std::endl;
            return firstDigit;
        }
    }
    return 0;
}

std::string lastDigitFinder(std::string l) {
    std::string lastDigit;
    for (int i = static_cast<int>(l.length()) -1; i != 0; i--) {
        if ( l[i] >= 0 && l[i] <= 9) {
            lastDigit = std::to_string(l[i]);
            std::cout << "firstDigit --> " << lastDigit << std::endl;
            return lastDigit;
        }
    }
    return 0;
}






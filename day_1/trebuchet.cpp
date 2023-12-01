#include <iostream>
#include <fstream>
#include <vector>
#include <string>

int main() {
    std::string filePath = "input.txt";

    std::ifstream inputFile(filePath);

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

    std::cout << "Lines from the file\n";
    for (const auto& l : lines) {
        std::cout << l << std::endl;
    }

    return 0;
}

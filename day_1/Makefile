CXX := g++
CXXFLAGS := -std=c++11 -Wall

.PHONY: all clean

all: myprogram

myprogram: $(wildcard *.cpp)
	$(CXX) $(CXXFLAGS) $^ -o $@

clean:
	rm -f myprogram

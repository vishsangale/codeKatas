#include <iostream>
#include <map>

int main() {
    std::map<int, std::string> students;

    students[1] = "Adam";
    students[2] = "April";
    students[3] = "Rachel";
    students[4] = "Sonia";
    students[5] = "Zack";
    std::cout << students << std::endl;
    std::cout << "Hello world!" << std::endl;
    return 0;
}

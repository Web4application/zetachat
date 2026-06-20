#pragma once

#include <vector>
#include <string>

class Memory {
public:
    void add(
        const std::string& item
    );

    std::string recall();

private:
    std::vector<std::string> memories;
};

#pragma once

#include <vector>
#include <string>

class voice {
public:
    void add(
        const std::string& item
    );

    std::string recall();

private:
    std::vector<std::string> voice;
};

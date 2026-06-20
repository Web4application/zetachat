#pragma once

#include <string>

class Agent {
public:
    std::string think(
        const std::string& task
    );

    std::string plan(
        const std::string& goal
    );
};

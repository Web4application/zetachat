#pragma once

#include <string>

class AI {
public:
    AI();

    std::string chat(
        const std::string& prompt
    );

    void remember(
        const std::string& memory
    );

private:
    std::string context;
};

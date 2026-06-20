#import "AIBridge.h"
#include "AIEngine.hpp"

@implementation AIBridge

- (NSString *)ask:(NSString *)prompt {

    AIEngine engine;

    std::string response =
        engine.ask([prompt UTF8String]);

    return [NSString stringWithUTF8String:
            response.c_str()];
}

@end

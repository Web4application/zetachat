import Foundation

final class AIService {

    static let shared = AIService()

    private let bridge = AIBridge()

    func ask(_ prompt: String) -> String {
        bridge.ask(prompt)
    }
}

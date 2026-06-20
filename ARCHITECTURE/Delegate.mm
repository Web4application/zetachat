import SwiftUI
import FirebaseCore
import FirebaseAuth
import FirebaseFirestore
import FirebaseStorage

// MARK: - App Delegate

final class AppDelegate: NSObject, UIApplicationDelegate {

    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
    ) -> Bool {

        FirebaseApp.configure()

        print("Firebase Initialized")

        return true
    }
}

// MARK: - Models

struct ChatMessage: Identifiable, Codable {

    let id: String
    let senderId: String
    let text: String
    let timestamp: Date
}

struct UserProfile: Identifiable, Codable {

    let id: String
    let username: String
    let email: String
}

// MARK: - Authentication Service

final class AuthService {

    static let shared = AuthService()

    func signIn(
        email: String,
        password: String
    ) async throws {

        try await Auth.auth()
            .signIn(
                withEmail: email,
                password: password
            )
    }

    func register(
        email: String,
        password: String
    ) async throws {

        try await Auth.auth()
            .createUser(
                withEmail: email,
                password: password
            )
    }

    func signOut() throws {
        try Auth.auth().signOut()
    }
}

// MARK: - AI Service

final class AIService {

    static let shared = AIService()

    func ask(
        prompt: String
    ) async -> String {

        // Replace with OpenAI/Gemini/Ollama

        return "AI Response: \(prompt)"
    }
}

// MARK: - Chat View Model

@MainActor
final class ChatViewModel: ObservableObject {

    @Published var messages: [ChatMessage] = []

    func sendMessage(_ text: String) {

        let message = ChatMessage(
            id: UUID().uuidString,
            senderId: "user",
            text: text,
            timestamp: Date()
        )

        messages.append(message)
    }

    func askAI(_ text: String) async {

        let response =
            await AIService.shared.ask(
                prompt: text
            )

        let aiMessage = ChatMessage(
            id: UUID().uuidString,
            senderId: "ai",
            text: response,
            timestamp: Date()
        )

        messages.append(aiMessage)
    }
}

// MARK: - Chat Screen

struct ChatView: View {

    @StateObject private var vm =
        ChatViewModel()

    @State private var input = ""

    var body: some View {

        VStack {

            ScrollView {

                LazyVStack {

                    ForEach(vm.messages) { msg in

                        HStack {

                            if msg.senderId == "user" {
                                Spacer()
                            }

                            Text(msg.text)
                                .padding()
                                .background(
                                    msg.senderId == "user"
                                    ? Color.blue
                                    : Color.gray.opacity(0.3)
                                )
                                .foregroundColor(.white)
                                .cornerRadius(12)

                            if msg.senderId == "ai" {
                                Spacer()
                            }
                        }
                        .padding(.horizontal)
                    }
                }
            }

            Divider()

            HStack {

                TextField(
                    "Type message...",
                    text: $input
                )
                .textFieldStyle(.roundedBorder)

                Button("Send") {

                    let text = input

                    vm.sendMessage(text)

                    input = ""

                    Task {
                        await vm.askAI(text)
                    }
                }
            }
            .padding()
        }
        .navigationTitle("ZetaChat")
    }
}

// MARK: - Main App

@main
struct ZetaChatApp: App {

    @UIApplicationDelegateAdaptor(
        AppDelegate.self
    )
    var appDelegate

    var body: some Scene {

        WindowGroup {

            NavigationStack {

                ChatView()
            }
        }
    }
}

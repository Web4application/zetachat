import SwiftUI
import FirebaseCore

// MARK: - App Delegate

final class AppDelegate: NSObject, UIApplicationDelegate {

    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
    ) -> Bool {

        FirebaseApp.configure()

        print("Firebase initialized successfully")

        return true
    }
}

// MARK: - Main App

@main
struct ZetaChatApp: App {

    @UIApplicationDelegateAdaptor(AppDelegate.self)
    var appDelegate

    var body: some Scene {
        WindowGroup {
            RootView()
        }
    }
}

// MARK: - Root View

struct RootView: View {

    var body: some View {
        NavigationStack {
            ContentView()
        }
    }
}

// MARK: - Content View

struct ContentView: View {

    var body: some View {
        VStack(spacing: 20) {

            Image(systemName: "message.fill")
                .font(.system(size: 60))

            Text("Welcome to ZetaChat")
                .font(.largeTitle)
                .fontWeight(.bold)

            Text("Firebase Connected")
                .foregroundStyle(.secondary)

        }
        .padding()
    }
}

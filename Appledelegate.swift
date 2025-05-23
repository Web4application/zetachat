import SwiftUI
import FirebaseCore

// Custom AppDelegate to handle Firebase initialization
class AppDelegate: NSObject, UIApplicationDelegate {
    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
    ) -> Bool {
        FirebaseApp.configure()
        return true
    }
}

@main
struct YourApp: App {
    // Attach AppDelegate for Firebase configuration
    @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate

    var body: some Scene {
        WindowGroup {
            NavigationView {
                ContentView()
            }
        }
    }
}

// Ensure the ContentView is defined
struct ContentView: View {
    var body: some View {
        Text("Hello, Firebase!")
            .padding()
    }
}

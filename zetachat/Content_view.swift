import SwiftUI

struct ContentView: View {

    @State private var prompt = ""
    @State private var response = ""

    var body: some View {

        VStack {

            TextField(
                "Ask AI...",
                text: $prompt
            )
            .textFieldStyle(.roundedBorder)

            Button("Send") {

                response =
                    AIService.shared
                    .ask(prompt)
            }

            ScrollView {
                Text(response)
            }
        }
        .padding()
    }
}

//
//  ContentView.swift
//  CoinFlip Watch App
//
//  Created by Ben Sieberer on 10.05.24.
//

import SwiftUI

struct ContentView: View {
    @State private var coinImageName = "heads"  // Initial image to display
    @State private var buttonText = "Toss Coin"
    @State private var spinDegrees = 0.0  // State to manage spin degrees

    var body: some View {
        VStack {
            Image(coinImageName)
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 160, height: 160)
                .padding(.top, 10)  // Reduced top padding
                .rotation3DEffect(.degrees(spinDegrees), axis: (x: 0, y: 1, z: 0))  // 3D rotation on Y-axis

            Spacer()  // Helps in distributing space

            Button(action: tossCoin) {
                Text(buttonText)
                    .fontWeight(.bold)
                    .foregroundColor(.white)
                    .padding(EdgeInsets(top: 5, leading: 10, bottom: 5, trailing: 10))  // Custom padding for text
                    .background(Color.blue)
                    .cornerRadius(30)  // Slightly smaller corner radius
            }
            .padding(.bottom, 50)  // Reduced bottom padding
        }
        .padding(.horizontal, 5)  // Reduced horizontal padding to gain a bit more space
    }
    
    func tossCoin() {
        let result = Bool.random()
        coinImageName = result ? "heads" : "tails"
        buttonText = "Toss Again"

        // Animation Logic
        withAnimation(.linear(duration: 0.5)) {
            spinDegrees += 360
        }
    }
}

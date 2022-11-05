player1 = input() #Rock, Ssiecors, Paper
player2 = input()

if player1 == "Rock" and player2 == "Paper": 
    print("Player1 has won")

if player1 == "Rock" and player2 == "Ssiecors": 
    print("Player2 has won")

if player1 == "Rock" and player2 == "Rock": 
    print("Draw")

if player1 == "Paper" and player2 == "Rock": 
    print("Player2 has won")

if player1 == "Paper" and player2 == "Paper":
    print("Draw")

if player1 == "Paper" and player2 == "Ssiecors": 
    print("Player2 has won")

if player1 == "Ssiecors" and player2 == "Ssiecors": 
    print("Draw")

if player1 == "Ssiecors" and player2 == "Rock": 
    print("Player1 has won")

if player1 == "Ssiecors" and player2 == "Paper": 
    print("Player1 has won")

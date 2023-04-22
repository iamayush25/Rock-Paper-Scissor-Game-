print(" 1. Rock\n 2. Paper\n 3.Scissors\n \n ")

print(" Rock and Rock = Match is tie\n Rock and paper = Paper is win\n Rock and Scissor = Rock is win\n Paper and Paper = Match is tie\n Paper and Rock = Paper ia win\n Paper and scissor =Scissor is win\n scissor and Rock = Rock is win \n scissor and paper = scissor is win \n scissor and scissor = Match is tie \n \n  " )

print(" Please choose your option : \n 1.Rock\n 2.paper\n 3.Scissore ")
player1=input("First Player  : ")
player2=input("Second Player  : ")

if player1.lower()== "rock" and player2.lower()== "rock":
	print("Match is tie")
elif player1.lower()=="rock" and player2.lower()=="paper":
	print("Second Player is win")
elif player1.lower()=="rock" and player2.lower()=="scissor":
	print("First Player is win ")
elif player1.lower()=="paper" and player2.lower()=="rock":
	print("First player is win")
elif player1.lower()=="paper" and player2.lower()=="paper":
	print("Match is tie")
elif player1.lower()=="paper" and player2.lower()=="scissor":
	print("Second player is win")
elif player1.lower()=="scissor" and player2.lower()=="rock":
	print("Second player is win")
elif player1.lower()=="scissor" and player2.lower()=="paper":
	print("First player is win")
elif player1.lower()=="scissor" and player2.lower()=="scissor":
	print("Match is tie")
else:
	print("Please Choose Valid option")
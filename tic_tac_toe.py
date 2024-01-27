board = ["   ","   ","   ","   ","   ","   ","   ","   ","   "]


def displayboard(board):
   print(board[0]+"|"+board[1]+"|"+board[2]) 
   print("---|---|---")
   print(board[3]+"|"+board[4]+"|"+board[5])
   print("---|---|---")
   print(board[6]+"|"+board[7]+"|"+board[8])



#displaying board  
displayboard(board)
print("player 1 has X")
print("player 2 has O")

for j in range(9):
    #player 1 chance 
    i=1
    while i :
        pos_X=int(input("Enter the position for 1 player: "))
        if board[pos_X-1]=="   ":
         board[pos_X-1]=" X "
         i=0
        else:
         print(" enter the position which is not used") 
    # check 

    if board[0]==board[1]==board[2]==" X ":
     print("player 1 has won")
     break
    elif board[3]==board[4]==board[5]==" X ":
     print("player 1 has won")
     break
    elif board[6]==board[7]==board[8]==" X ":
     print("player 1 has won")
     break
    elif board[0]==board[3]==board[6]==" X ":
     print("player 1 has won")
     break
    elif board[1]==board[4]==board[7]==" X ":
     print("player 1 has won")
     break
    elif board[2]==board[5]==board[8]==" X ":
     print("player 1 has won")
     break
    elif board[0]==board[4]==board[8]==" X ":
     print("player 1 has won")
     break
    elif board[2]==board[4]==board[6]==" X ":
     print("player 1 has won")
     break

    displayboard(board)

    if "   " not in board:
     print("it is a tie")
     break
    
    # player 2 chance 

    i=1
    while i :
        pos_O=int(input("Enter the position for 2 player: "))
        if board[pos_O-1]=="   ":
         board[pos_O-1]=" O "
         i=0
        else:
         print(" enter the position which is not used ")

    displayboard(board)

    #check

    if board[0]==board[1]==board[2]==" O ":
     print("player 2 has won")
     break
    elif board[3]==board[4]==board[5]==" O ":
     print("player 2 has won")
     break
    elif board[6]==board[7]==board[8]==" O ":
     print("player 2 has won")
     break
    elif board[0]==board[3]==board[6]==" O ":
     print("player 2 has won")
     break
    elif board[1]==board[4]==board[7]==" O ":
     print("player 2 has won")
     break
    elif board[2]==board[5]==board[8]==" O ":
     print("player 2 has won")
     break
    elif board[0]==board[4]==board[8]==" O ":
     print("player 2 has won")
     break
    elif board[2]==board[4]==board[6]==" O ":
     print("player 2 has won")
     break


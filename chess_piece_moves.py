lst = [ ]
string='abcdefgh'       # To store the indexes of the blocks of chess board
a=[ ]
for char in string:
    for j in range(8):
        ele = [char,j+1]
        lst.append(ele)     # chessboard index names stored
def ask():
    ch=int(input("Enter the required number to know the posssible moves of the corresponding chess pieces \n 1- The Pawn\n 2- The Knight\n 3- The Bishop \n 4- The Rook\n 5-The Queen\n 6- The King\n") )
    print("The initial postion(s) is/are")
    if ch==1:
        c=0
        for i in range (8):         #to display 8 initial positions of pawn
            print(lst[1+c])
            c+=8
        print("The possible moves are")
        c=2
        for i in range (8):             #calculating the next block(s) for each position
            print(lst[c],lst[c+1])
            c+=8
    if ch==2:                       #Knight
        print(lst[8],lst[8+8*5])
        print("The possible moves are")
        print("for knight at b1 ",lst[2],lst[2+8*2])
        print("for knight at g1 ",lst[42],lst[42+8*2])
    if ch==3:                       #Bishop
        print(lst[16],lst[16+3*8])
        firdex=16       #for first index 
        secdex=16+3*8   #for second index
        c=9
        print("The available blocks when initial position is ",lst[firdex])
        for i in range (5):
            print(lst[firdex+c])            #to calculate the diagonal elements
            c+=9
        print(lst[10])
        print(lst[1])
        print("The available blocks when initial position is ",lst[secdex])
        c=7
        for i in range(5):
            print(lst[secdex-c])            #same logic for second position
            c+=7
        print(lst[49])
        print(lst[58])
    if ch==4:                               #Rook
        print(lst[0],lst[56])
        print("The available positions when the initial position is ",lst[0])
        for i in range (7):                 # To calculate all the blocks vertically
            print([lst[1+i]])               
        for i in range (7):                 ## To calculate all the blocks horizontally
            print(lst[8+i*8])
        print("The available positions when the initial position is ",lst[56])
        for i in range (7):
            print(lst[56+i])
        for i in range (1,8,1):
            print(lst[56-8*i])
    if ch==5:                               #The queen
        print(lst[24])
        print("The available positions are ")   
        for i in range (7):                 #For vertical positions
            print([lst[25+i]])
        c=9
        for i in range(4):                  #For diagonal position
            print(lst[24+c])
            c+=9
        c=7
        for i in range(3):
            print(lst[24-c])
            c+=7
        for i in range (1,3,1):
            print(lst[24-i*8])
        for i in range (1,5,1):             #for horizontal position
            print(lst[24+i*8])
    if ch==6:                               #The king
        print(lst[32])
        print("The available positions are ")
        print(lst[33])
        print(lst[32-8])
        print(lst[32+8])
        print(lst[32-8+1])
        print(lst[32+8+1])
ask()
 

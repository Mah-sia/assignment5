from random import randint
def show_game_board():
    for i in range(3):
        for j in range(3):
          print(game[i][j],end='')
        print()
def Winingcheck():
    if game[0][0]==' X ' and game[1][1]==' X ' and game[2][2]==' X ':
        print('You win..!')
    if game[0][0]==' O ' and game[1][1]==' O ' and game[2][2]==' O ':
        print('You win..!')
    for i in range (3):
        if game[i][0]==' X ' and game[i][1]==' X ' and game[i][2]==' X ':
            print('You win..!')
        if game[0][i]==" X " and game[1][i]==' X ' and game[2][i]==' X ':
            print('You win..!')
        if game[i][0]==' O ' and game[i][1]==' O ' and game[i][2]==' O ':
            print('You win..!')
        if game[0][i]==" O " and game[1][i]==' O ' and game[2][i]==' O ':
            print('You win..!')
   # else:
      #  c=0
       # for i in range(3):
        #    for j in range(3):
         #       if game[i][j]!=' - ':
          #          c+=c
        #if c==9:
          #print('Equal...!')
            
            



game=[[' - ',' - ',' - '],[' - ',' - ',' - '],[' - ',' - ',' - ']]
p=int(input('computer play insert 0 anf play with player insert 1'))
show_game_board()
while True:
    print('player1')
    while True:
        row = int(input('satr ra verad kon:'))
        col = int(input('sotoon ra verad kon:'))
        if 0<=row<=2 and 0<=col<=2:
            if game[row][col]==' - ':
                game[row][col]=' X '
                break
            else:
                print('Cell is Full...!')
                
        else: 
            print('index out of range ,Try again!')

    show_game_board()
    Winingcheck()
    if p==1:

        print('player2')
        while True:
            row = int(input('satr ra verad kon:'))
            col = int(input('sotoon ra verad kon:'))
            if 0<=row<=2 and 0<=col<=2:
                if game[row][col]==' - ':
                    game[row][col]=' O '
                    break
                else:
                    print('Cell is Full...!')
                    

        show_game_board()
        Winingcheck()
    elif p==0:
        print('computer')
        while True:
            row = randint(0,2)
            col = randint(0,2)

            if 0<=row<=2 and 0<=col<=2:
                if game[row][col]==' - ':
                    game[row][col]=' O '
                    break
                else:
                    print('Cell is Full...!')
                    

        show_game_board()
        Winingcheck()
import random
import time

class TicTacToe:

    #variables
    def __init__(self):
        self.board=[" "]*9
        self.setPos=[i for i in range(9)]
        self.winner=""
        self.turn=""
        self.game=True
        
        
        
    def display(self):
        print(self.board[0]+" | "+self.board[1]+" | "+self.board[2]+"           1 | 2 | 3 ")
        print("----------         -----------")
        print(self.board[3]+" | "+self.board[4]+" | "+self.board[5]+"           4 | 5 | 6 ")
        print("----------         -----------")
        print(self.board[6]+" | "+self.board[7]+" | "+self.board[8]+"           7 | 8 | 9 ")
        print("----------         -----------")

    def chooseTurn(self):
        if self.turn=="":
            response=input("\nLet's flip a coin! Head(H) or Tail(T)?").upper()
            if response not in ["H","T"]:
                self.chooseTurn()
            else:

                flip=random.choices(["H","T"])[0]
                if (flip==response):
                    print("You won! So have your start move with X....")
                    self.turn="X"
                else:
                    print("Yayy! My Turn first with O...")
                    self.turn="O"


        else:
            self.turn="O" if (self.turn=="X" ) else "X"
            

    def play(self):
        
        if self.turn=="X":
            print("\n")
            print(self.turn+" turn's")
            response=input("Choose Your Next Move (1-9) :  ")
            if (response.isnumeric() and (int(response)-1 in self.setPos)):
                index=int(response)
                self.board[index-1]="X"
                self.setPos.remove(index-1)
                print()
                self.display()
                self.chooseTurn()

            else:
                self.play()

        else:
            print("\n"+"-"*40+"\n")
            print(self.turn+" turn's")
            index=random.choice(self.setPos)
            time.sleep(1)
            self.setPos.remove(index)
            self.board[index]="O"
            self.display()
            self.chooseTurn()

    def checkRows(self):
        for index in range(0,7,3):
            if(self.board[index]==self.board[index+1]==self.board[index+2]!=" "):
                self.game=False
                self.winner=self.board[index]


    def checkColumns(self):
        for index in range(0,3):
            if(self.board[index]==self.board[index+3]==self.board[index+6]!=" "):
                self.game=False
                self.winner=self.board[index]
                

    def checkDiagonal(self):
        d1=self.board[0]==self.board[4]==self.board[8]!=" "
        d2=self.board[2]==self.board[4]==self.board[6]!=" "
        if d1 or d2:
            self.game=False
            self.winner=self.board[4]
            

    def checkEnd(self):
        
        self.checkRows()
        
        self.checkColumns()
        
        self.checkDiagonal()
                
        self.checkGame()
        

        if (self.game==False) and (self.winner==""):
            print("\n\nYayy! It's a Tie...")
            return False

        elif (self.game==False) and (self.winner!=""):
            if self.winner=="X":
                print("\n\nYou Win!!!!!!! \nSee ya next Time...")
            else:
                print("\n\nHurray! I won!....\nBetter luck next time...")
            return False

        else:
            return True

    def checkGame(self):
        if len(self.setPos)==0:
            self.game=False
        
    def main(self):
        
        print("\n-------TIC TAC TOE-------\n\n")
        start=True
        while start:
            print("The Board and the Corresponding positions: \n")
            self.display()
            self.chooseTurn()
            while self.checkEnd():
                self.play()
            
            temp=input("\n\n"+"-"*50+"\nDo you want to play again? (Y for yes): ")
            start=True if (temp=="Y" or temp=="y") else False


            
game=TicTacToe()
game.main()

    

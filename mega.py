import sys
import random


#The class is the board, which is created based on the game type - tic, connect or mega. 
#A game is an instantiation of the board, with attributes - arrangement (of the pieces), 
#conn_l (no. of connected pieces), size, open (set of possible next positions that can be played. )
#

class Board():
    def __init__(self, s): 
        if s=='tic':
            self.size = [3,3]
            i,j = self.size
            self.conn_l = 3
            self.game = s

        if s=='connect':
            self.size = [6,6]
            i,j = self.size
            self.conn_l = 4
            self.game = s
            self.open = [a for a in range(j)] 

        if s=='mega':
            self.size = [8,8]
            i,j = self.size
            self.conn_l = 3
            self.game = s


        self.arrangement = [["-" for x in range(j)] for y in range(i)]  #Create a list of j lists, with each list containing i elements. 
        if s != 'connect':
            self.open = [a for a in range(i*j)]


#required only in the while loop
#Another game with another definition of 'full' should override this
    def isfull(self):
        i = 0
        for row in self.arrangement:
            for spot in row: 
                if spot == '-':
                    i += 1
        if i == 0:
            print "GAMEOVER? True" 
            return True

        print "GAMEOVER? False"
        return False


    def play_turn(self, player):
        play = random.randrange(len(self.open))
        if self.game == 'connect':
            column = self.open[play]
            for row in range(self.size[0]-1, -1, -1):
                if self.arrangement[row][column] == '-':
                    self.arrangement[row][column] = player
                    break
                if row == 0:
                        self.open.remove(column)    



        if self.game != 'connect':
            index = self.open.pop(play)
            i,j = index/self.size[0], index%self.size[0]
            print i,j, self.arrangement[i][j]
            self.arrangement[i][j] = player
        
        game.display_arrangement()

    def display_arrangement(self):
        for row in self.arrangement:
            for spot in row: 
                print spot,
            print    


    def isconnected(self):
        #I have tried to generalise the code so that changing conn_l should still work That's why I have 3 loops instead of 2. 
        if self.game == 'connect':
            for x in range(0, self.size[0] + 1 -self.conn_l ):
                for y in xrange(0, self.size[1]):
                    result1, result2 = True, True
                    for z in range(0, self.conn_l):
                        result1 = result1 and (self.arrangement[x+z][y] == 'A')
                        result2 = result2 and (self.arrangement[x+z][y] == 'B')

                    if result1 or result2:
                        return True
            
            #Check for items rightwards
            for x in range(0, self.size[0]):
                for y in xrange(0, self.size[1] + 1 -self.conn_l ):
                    result1, result2 = True, True
                    for z in range(0, self.conn_l):
                        result1 = result1 and (self.arrangement[x][y+z] == 'A')
                        result2 = result2 and (self.arrangement[x][y+z] == 'B')

                    if result1 or result2:
                        return True


            return False

        else :
            #Check for items downwards
            for x in range(0, self.size[0] + 1 -self.conn_l ):
                for y in xrange(0, self.size[1]):
                    result1, result2 = True, True
                    for z in range(0, self.conn_l):
                        result1 = result1 and (self.arrangement[x+z][y] == 'A')
                        result2 = result2 and (self.arrangement[x+z][y] == 'B')

                    if result1 or result2:
                        return True
                            
            #Check for items rightwards
            for x in range(0, self.size[0]):
                for y in xrange(0, self.size[1] + 1 -self.conn_l ):
                    result1, result2 = True, True
                    for z in range(0, self.conn_l):
                        result1 = result1 and (self.arrangement[x][y+z] == 'A')
                        result2 = result2 and (self.arrangement[x][y+z] == 'B')

                    if result1 or result2:
                        return True

            #Check for items right-down
            for x in range(0, self.size[0] + 1 -self.conn_l ):
                for y in xrange(0, self.size[1]+ 1 -self.conn_l):
                    result1, result2 = True, True
                    for z in range(0, self.conn_l):
                        result1 = result1 and (self.arrangement[x+z][y+z] == 'A')
                        result2 = result2 and (self.arrangement[x+z][y+z] == 'B')

                    if result1 or result2:
                        return True



            #Check for items left-down
            for x in range(self.conn_l-1, self.size[0] ):
                for y in xrange(0, self.size[1]+ 1 -self.conn_l):
                    result1, result2 = True, True
                    for z in range(0, self.conn_l):
                        result1 = result1 and (self.arrangement[x-z][y+z] == 'A')
                        result2 = result2 and (self.arrangement[x-z][y+z] == 'B')

                    if result1 or result2:
                        return True

            return False


if __name__ == "__main__":
    g = sys.argv[1]
    game = Board(g)
    #print game
    players = ['A', 'B']
    i = 0
    game.display_arrangement()
    while (not game.isfull()):
        pl = players[i]
        game.play_turn(pl)
        i += 1
        i = i%2
        if game.isconnected():
            print "GAMEOVER? True"
            break
            


# a = random.randrange(i*j)
# i , j = a/i, a%i           
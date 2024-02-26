from tkinter import *
import random as rand

class game():
    grid = [[0 for r in range(4)] for c in range(4)]
    gui = Tk()
    instruct = Tk()
    gui.title("2048")
    instruct.title("Instructions")
    colors = {0: "black", 2: "red", 4: "yellow", 8: "lightgreen", 16: "turquoise", 32: "skyblue", 64: "mediumpurple", 128: "mediumorchid", 256: "violet", 512: "magenta", 1024: "hotpink", 2048: "lightpink"}


    def __init__(self): ##game setup
        self.gui.bind("<Left>", self.left)
        self.gui.bind("<Right>", self.right)
        self.gui.bind("<Up>", self.up)
        self.gui.bind("<Down>", self.down)


    def draw(self): ##draw gui
        tiles = []
        for row in range(4):
            for col in range(4): ##for each number in the grid
                color = self.colors[self.grid[row][col]] ##retrieve corresponding color to value from dictionary
                tile = Label(self.gui, bg=color, text=str(self.grid[row][col]), width=10, height=5, font=("Arial", 15)) #draw tile
                tile.grid(row=row, column=col, padx=5, pady=5) ##add to grid
                tiles.append(tile)


    def start(self): ##begins game by displaying instructions and adding two tiles
        inst = Label(self.instruct, text="Use arrow keys to move tiles. If two tiles have the same value, they merge! Reach 2048 to win :)", font=("Arial", 15))
        inst.pack()
        self.spawn()
        self.spawn()


    def spawn(self): ##spawns a 2 at a random empty tile
        temp_val = 1
        while temp_val != 0:
            r = rand.randint(0,3)
            c = rand.randint(0,3) ##choose random coordinate
            temp_val = self.grid[r][c]
            if temp_val == 0: ##if tile is empty
                self.grid[r][c] = 2
        self.draw() ##update grid
        self.win() ##check if game is won
   
    def left(self, event): #move left
        #check every block not col 0
        for c in range(1,4):
            for r in range(4):
                left_block = 0 #val of first block to the left
                left_c = 0 #column of left_block
                temp_val = self.grid[r][c]
                if temp_val != 0:#if block has value, find first block to left with value
                    for col in range(0,c): #find block to left
                        if self.grid[r][col] != 0:
                            left_block = self.grid[r][col]
                            left_c = col
                    if left_block == 0:#if there is no block to left with value, block moves to col 0
                        self.grid[r][c] = 0
                        self.grid[r][0] = temp_val
                    elif temp_val != left_block:# if two blocks have diff value, block goes to right of left block
                        self.grid[r][c] = 0
                        self.grid[r][left_c+1] = temp_val
                    else:#if blocks have same val, combine
                        self.grid[r][left_c] = left_block*2
                        self.grid[r][c] = 0                
        self.spawn()
   
    def right(self, event): ##move right
        #check every block not col 3  
        for c in range(2,-1,-1):
            for r in range(4):
                right_block = 0
                right_c = 0
                temp_val = self.grid[r][c]
                if temp_val != 0:#if block has value, find first block to right with value
                    for col in range(3,c,-1): #find block to right
                        if self.grid[r][col] != 0:
                            right_block = self.grid[r][col]
                            right_c = col
                    if right_block == 0:#if there is no block to right with value, block moves to col 3
                        self.grid[r][c] = 0
                        self.grid[r][3] = temp_val
                    elif temp_val != right_block:# if two blocks have diff value, block goes to left of right block
                        self.grid[r][c] = 0
                        self.grid[r][right_c-1] = temp_val
                    else:#if blocks have same val, combine
                        self.grid[r][right_c] = right_block*2
                        self.grid[r][c] = 0                
        self.spawn()


    def up(self, event): ##move up
        #check every block not row 0
        for c in range(4):
            for r in range(1,4):
                up_block = 0
                up_r = 0
                temp_val = self.grid[r][c]
                if temp_val != 0:#if block has value, find first block above with value
                    for row in range(0,r): #find block above
                        if self.grid[row][c] != 0:
                            up_block = self.grid[row][c]
                            up_r = row
                    if up_block == 0:#if there is no block above with value, block moves to row 0
                        self.grid[r][c] = 0
                        self.grid[0][c] = temp_val
                    elif temp_val != up_block:# if two blocks have diff value, block goes below up block
                        self.grid[r][c] = 0
                        self.grid[up_r+1][c] = temp_val
                    else:#if blocks have same val, combine
                        self.grid[up_r][c] = up_block*2
                        self.grid[r][c] = 0                
        self.spawn()


    def down(self, event): ##move down
        #check every block not row 3    
        for c in range(4):
            for r in range(2,-1,-1):
                down_block = 0
                down_r = 0
                temp_val = self.grid[r][c]
                if temp_val != 0:#if block has value, find first block below with value
                    for row in range(3,r,-1): #find block below
                        if self.grid[row][c] != 0:
                            down_block = self.grid[row][c]
                            down_r = row
                    if down_block == 0:#if there is no block below with value, block moves to row 3
                        self.grid[r][c] = 0
                        self.grid[3][c] = temp_val
                    elif temp_val != down_block:# if two blocks have diff value, block goes above down block
                        self.grid[r][c] = 0
                        self.grid[down_r-1][c] = temp_val
                    else:#if blocks have same val, combine
                        self.grid[r][c] = 0
                        self.grid[down_r][c] = down_block*2
                                       
        self.spawn()


    def win(self): ##check if game is won
        for row in range(4):
            for col in range(4):
                if self.grid[row][col] == 2048: ##check if there is a 2048
                    message = Label(self.gui, text="You win!") ##display victory message
                    message.grid()
                    self.gui.unbind("<Left>") ##no more moving
                    self.gui.unbind("<Right>")
                    self.gui.unbind("<Up>")
                    self.gui.unbind("<Down>")        


play = game()    
play.start() ##start the game
play.gui.mainloop()

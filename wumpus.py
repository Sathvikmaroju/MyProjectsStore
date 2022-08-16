import numpy as np

grid = [
    ['S',  '' ,'B', ''],
    ['W','SGB','P','B'],
    ['S', ''  ,'B', ''],
    [ '', 'B' ,'P','B']
]
print(np.matrix(grid))

def possibile_positions(x,y):
    res = []
    if x+1<4:
        res.append((x+1,y))
    
    if y+1<4:
        res.append((x,y+1))
    
    if x-1>=0:
        res.append((x-1,y))
    
    if y-1>=0:
        res.append((x,y-1))
    return res   

def cave_atmos(str):
    if str=='':
        pass
    elif str=='B':
        return "You can feel Breeze"
    elif str=='S':
        return "You can smell Stench"
    elif str=='G':
        return "You found Gold"
    elif str=='P':
        return "You fell in a Pit"
    elif str=='W':
        return "You encountered wumpus"

def update_player_grid(x,y,env,grid):
    if env =='':
        grid[x][y]='ok'
    elif str=='B':
        grid[x][y]="Breeze"
    elif str=='S':
        grid[x][y]="Stench"
    elif str=='G':
        grid[x][y]="Gold"
    elif str=='P':
        grid[x][y]="Pit"
    elif str=='W':
        grid[x][y]="Wumpus"
    return grid

player_grid = [
    ['?','?','?','?'],
    ['?','?','?','?'],
    ['?','?','?','?'],
    ['?','?','?','?']
]

print(np.matrix(player_grid))
"""x,y = input("Enter agent initial position (x,y): ").split(',')
x,y = int(x),int(y)
curent_position=[x,y]
print(f"\nInitially agent is at {x},{y}\n{cave_atmos(grid[x][y])}\n")
for i in possibile_positions(x,y):
        print(f"You can got to {i[0]},{i[1]}")
player_grid = update_player_grid(x,y,grid[x][y],player_grid)
print(np.matrix(player_grid))"""

gold = False
i=0
while not gold:
    if i==0:
        x,y = input("\nEnter agent initial position (x,y): ").split(',')
        i+=1
    else:
        x,y = input("\nEnter agent position (x,y): ").split(',')
        while (x,y) not in possibile_positions:
            x,y = input("\nEnter agent position (x,y): ").split(',')
    x,y = int(x),int(y)
    curent_position=[x,y]
    if len(grid[x][y])>1:
        s=''
        for i in grid[x][y]:
            s+= cave_atmos(i)
        
    
    for i in possibile_positions(x,y):
        print(f"You can got to {i[0]},{i[1]}")
    
    player_grid = update_player_grid(curent_position[0],curent_position[1],grid,player_grid)
    print(np.matrix(player_grid))
    
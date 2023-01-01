# Brian's Cell Sim
import random

n_bugs = 10
cell_dim = 3
grid_dim = 500


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

class cell:
    def __init__(self):
        self.x = random.randint(0, grid_dim-1)
        self.y = random.randint(0, grid_dim-1)
        self.bg_color = [random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)]
        self.age = 0
        self.p_mitosis = 0.1
        self.lifespan = 20
        self.speed = random.randint(1, 3)
      
    def random_walk(self):
        dir_x = random.randint(-1, 1)
        dir_y = random.randint(-1, 1)
        
        self.x = self.x + dir_x*self.speed
        self.y = self.y + dir_y*self.speed
        
        self.x = clamp(self.x, 0, grid_dim-1)
        self.y = clamp(self.y, 0, grid_dim-1)

bugs = []
for i in range(n_bugs):
    bugs.append(cell())

def setup():
    size(grid_dim*cell_dim,grid_dim*cell_dim)
    colorMode(RGB, 255)
    background(0)
    frameRate(10)

def draw():

    background(0)
    # draw the grid on the background
    for i in range(100):
        noFill()
        stroke(50, 50, 50)
        #line(x1, y1, x2, y2)
        #line(i*cell_dim, 0, i*cell_dim, height) 
        #line(0, i*cell_dim, width, i*cell_dim)
            
    for bug in bugs:
        fill(bug.bg_color[0], bug.bg_color[1], bug.bg_color[2])
        noStroke()
        rect(bug.x*cell_dim, bug.y*cell_dim, cell_dim, cell_dim)
        bug.random_walk()
        
        if random.random() < bug.p_mitosis and len(bugs) < 5000:
            baby = cell()
            baby.x = bug.x + random.randint(-1, +1)
            baby.y = bug.y + random.randint(-1, +1)
            #baby.bg_color = [random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)]
            baby.bg_color = [bug.bg_color[0] + random.randint(-10, +10) , bug.bg_color[1] + random.randint(-10, +10) , bug.bg_color[2] + random.randint(-10, +10)]
            baby.age = 0
            baby.p_mitosis = bug.p_mitosis + (random.random()-0.5)/15
            baby.lifespan = bug.lifespan + random.randint(-1, +1)
            bugs.append(baby)
                    
        bug.age += 1
        if bug.age > bug.lifespan:
            bugs.remove(bug)

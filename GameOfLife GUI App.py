import random
import math
import tkinter


class Person:
    def __init__(self):
        self.is_alive = False

    def dead(self):
        self.is_alive = False

    def alive(self):
        self.is_alive = True


class Population:
    def __init__(self):
        self.p_size = 2500
        self.sqrt = int(math.sqrt(self.p_size))
        self.population = []

        for p in range(self.sqrt):
            row = []
            for q in range(self.sqrt):
                person = Person()
                row.append(person)
            self.population.append(row)

        # ###################
        for i in range(200):
            x = random.randint(0, self.sqrt-1)
            y = random.randint(0, self.sqrt-1)
            self.population[x][y].alive()
        # ###################

    def update(self):
        for i in range(self.sqrt):
            for j in range(self.sqrt):
                count = 0
                #if self.population[i][j].is_alive:
                if i == 0:
                    if j == 0:
                            if self.population[i+1][j].is_alive:
                                count += 1
                            if self.population[i][j+1].is_alive:
                                count += 1
                            if self.population[i+1][j+1].is_alive:
                                count += 1
                    elif j == self.sqrt-1:
                            if self.population[i+1][j].is_alive:
                                count += 1
                            if self.population[i][j-1].is_alive:
                                count += 1
                            if self.population[i+1][j-1].is_alive:
                                count += 1
                    else:
                            if self.population[i][j-1].is_alive:
                                count += 1
                            if self.population[i][j+1].is_alive:
                                count += 1
                            if self.population[i+1][j-1].is_alive:
                                count += 1
                            if self.population[i+1][j].is_alive:
                                count += 1
                            if self.population[i+1][j+1].is_alive:
                                count += 1
                elif i == self.sqrt-1:
                    if j == 0:
                            if self.population[i-1][j].is_alive:
                                count += 1
                            if self.population[i-1][j+1].is_alive:
                                count += 1
                            if self.population[i][j+1].is_alive:
                                count += 1
                    elif j == self.sqrt-1:
                            if self.population[i-1][j].is_alive:
                                count += 1
                            if self.population[i-1][j-1].is_alive:
                                count += 1
                            if self.population[i][j-1].is_alive:
                                count += 1
                    else:
                            if self.population[i][j-1].is_alive:
                                count += 1
                            if self.population[i-1][j-1].is_alive:
                                count += 1
                            if self.population[i-1][j].is_alive:
                                count += 1
                            if self.population[i-1][j+1].is_alive:
                                count += 1
                            if self.population[i][j+1].is_alive:
                                count += 1
                else:
                    if j == 0:
                        if self.population[i - 1][j].is_alive:
                            count += 1
                        if self.population[i - 1][j + 1].is_alive:
                            count += 1
                        if self.population[i][j + 1].is_alive:
                            count += 1
                        if self.population[i + 1][j].is_alive:
                            count += 1
                        if self.population[i + 1][j + 1].is_alive:
                            count += 1
                    elif j == self.sqrt-1:
                        if self.population[i - 1][j].is_alive:
                            count += 1
                        if self.population[i - 1][j - 1].is_alive:
                            count += 1
                        if self.population[i][j - 1].is_alive:
                            count += 1
                        if self.population[i + 1][j].is_alive:
                            count += 1
                        if self.population[i + 1][j - 1].is_alive:
                            count += 1
                    else:
                        if self.population[i][j - 1].is_alive:
                            count += 1
                        if self.population[i - 1][j - 1].is_alive:
                            count += 1
                        if self.population[i - 1][j].is_alive:
                            count += 1
                        if self.population[i - 1][j + 1].is_alive:
                            count += 1
                        if self.population[i][j + 1].is_alive:
                            count += 1
                        if self.population[i + 1][j + 1].is_alive:
                            count += 1
                        if self.population[i + 1][j].is_alive:
                            count += 1
                        if self.population[i + 1][j - 1].is_alive:
                            count += 1

                # change state
                if self.population[i][j].is_alive:
                    if count < 2 or count > 3:
                        self.population[i][j].dead()
                else:
                    if count == 3:
                        self.population[i][j].alive()

    def show_matrix(self):
        alive = 0
        dead = 0
        for i in range(self.sqrt):
            for j in range(self.sqrt):
                if self.population[i][j].is_alive:
                    alive += 1
                else:
                    dead += 1

        print("\n.....Alive # ", str(alive))
        print(".....Dead # ", str(dead))


def show_graphics(population, canvas):
    square_dim = 600// population.sqrt

    for i in range(population.sqrt):
        y = i*square_dim
        for j in range(population.sqrt):
            x = j*square_dim

            if population.population[i][j].is_alive == False:
                canvas.create_rectangle(x, y, x + square_dim, y + square_dim, fill='black')
            else:
                canvas.create_rectangle(x, y, x + square_dim, y + square_dim, fill='white')

###########################tkinter properties ###################
width = 600
height = 600

window = tkinter.Tk()
window.title("Game of Life")
canvas = tkinter.Canvas(window, width=width, height=height, bg='light blue')
canvas.pack()#side=tkinter.LEFT)

def main():
    population = Population()
    print("<- Welcome, to Game of Life Command line app ->")
    generation = 1
    print("\n<---------- Generation # ", str(generation), " ----------->")
    population.show_matrix()
    input("\n...Please, press enter to stimulate the app...")
    running = True
    while running:
        print("\n<---------- Generation # ", str(generation+1), " ----------->")
        population.update()
        population.show_matrix()
        show_graphics(population, canvas)
        generation += 1
        window.update()


main()

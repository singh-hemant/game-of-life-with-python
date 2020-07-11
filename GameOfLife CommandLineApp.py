import random
import math


class Person:
    def __init__(self):
        self.is_alive = False

    def dead(self):
        self.is_alive = False

    def alive(self):
        self.is_alive = True


class Population:
    def __init__(self):
        self.p_size = 1296
        self.sqrt = int(math.sqrt(self.p_size))
        self.population = []

        for p in range(self.sqrt):
            row = []
            for q in range(self.sqrt):
                person = Person()
                row.append(person)
            self.population.append(row)

        ####################
        for i in range(400):
                x = random.randint(0, self.sqrt-1)
                y = random.randint(0, self.sqrt-1)
                self.population[x][y].alive()
        ####################

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
        self.alive = 0
        self.dead = 0
        for i in range(self.sqrt):
            for j in range(self.sqrt):
                if self.population[i][j].is_alive == True:
                    self.alive += 1
                    print("0", end=" ")
                else:
                    self.dead += 1
                    print("X", end=" ")
            print()

        print("\n.....Alive # ", str(self.alive))
        print(".....Dead # ", str(self.dead))


def main():
    population = Population()
    print("<- Welcome, to Game of Life Command line app ->")
    generation = 1
    print("\n<---------- Generation # ", str(generation), " ----------->")
    population.show_matrix()
    running = True
    while running:
        input("\n...Please, press enter to stimulate the app...")
        print("\n<---------- Generation # ", str(generation+1), " ----------->")
        population.update()
        population.show_matrix()
        generation += 1


main()

import random 
import math

class Bees:

    def __init__(self, size_x, size_y, best_site, elite_site, nre, nrb, ns, max_value):
        self.size_x = size_x
        self.size_y = size_y
        self.best_site = best_site
        self.elit_site = elite_site
        self.nre = nre
        self.nrb = nrb
        self.max_value = max_value

        self.flower_patch_radius = 3
        self.solutions = []
        self.scout_bees = []
        self.new_scout_bees = ns
        self.foragers = []
        self.flower_patches = []
        self.local_maximums = []

        self.__create_field__()

    def __create_field__(self):
        for _ in range(0, self.size_x * self.size_y):
            random_int = random.randint(0, self.max_value)
            self.solutions.append(random_int)

    def do_first_step(self):
        self.foragers = []
        self.assign_scouts()
        self.create_flower_patches()

    def do_second_step(self):
        self.assign_foragers()

    def do_third_step(self):
        self.evaluate_forager_results()
        
    def assign_scouts(self):
        available_positions = [i for i in range(0, len(self.solutions))]
        while self.new_scout_bees > 0:
            random_int = random.randint(0, len(available_positions)-1)
            self.scout_bees.append(available_positions[random_int])
            del available_positions[random_int]
            self.new_scout_bees -= 1
        
    def create_flower_patches(self):
        for scout_bee in self.scout_bees:
            found = False
            if scout_bee in [x[0] for x in self.flower_patches]:
                found = True
            if not found:
                self.flower_patches.append([scout_bee, self.flower_patch_radius])

    def assign_foragers(self):
        self.foragers = []

        discovered = [False for _ in range(0, self.size_x * self.size_y)]
        flower_patch_positions = [x[0] for x in self.flower_patches]

        for scout_bee in self.scout_bees:
            forager_group = [scout_bee]
            discovered[scout_bee] = True
            num_foragers = 0
            if self.solutions[scout_bee] >= self.elit_site:
                num_foragers = self.nre
            elif self.solutions[scout_bee] >= self.best_site:
                num_foragers = self.nrb
            else:
                num_foragers = 1
        
            # find the flower patch and get the radius
            index = flower_patch_positions.index(scout_bee)
            radius = self.flower_patches[index][1]

            #get all the cells that are within the radius
            smallest = scout_bee - (self.size_x + 1) * radius
            largest = scout_bee + (self.size_x + 1) * radius
            if smallest < 0:
                smallest = 0
            if largest >= self.size_x * self.size_y:
                largest = (self.size_y * self.size_x) - 1
            bee_row = scout_bee / self.size_y
            bee_col = scout_bee % self.size_x
            possible_landings = []
            for i in range(smallest, largest+1):
                if i != scout_bee:
                    row = i / self.size_y
                    col = i % self.size_x
                    if abs(bee_row - row) <= radius and abs(bee_col - col) <= radius:
                        possible_landings.append(i)

            # assign all the foragers
            for _ in range(0, num_foragers):
                if len(possible_landings) > 0:
                    random_int = random.randint(0, len(possible_landings)-1)
                    if not discovered[random_int]:
                        forager_group.append(possible_landings[random_int])
                        discovered[possible_landings[random_int]] = True
                    del possible_landings[random_int]

            self.foragers.append(forager_group)
    
    def evaluate_forager_results(self):
        for forager_group in self.foragers:

            # index of the scout bee that belongs to the current foraging group
            index = self.scout_bees.index(forager_group[0])
            scout_position = index

            highest_solution = self.solutions[forager_group[0]]
            current_scout_index = 0 # index of the current scout within the group

            # get the highest value within the foraging group
            for i, bee in enumerate(forager_group):
                if self.solutions[bee] > highest_solution:
                    highest_solution = self.solutions[bee]
                    current_scout_index = i
            
            if current_scout_index == 0:
                radius = self.flower_patches[scout_position][1]
                if radius <= 1:
                    self.local_maximums.append([forager_group[0], self.solutions[forager_group[0]]])
                    self.new_scout_bees += 1
                    del self.scout_bees[scout_position]
                    del self.flower_patches[scout_position]
                else:
                    self.flower_patches[scout_position][1] -= 1
            else:
                self.flower_patches[scout_position][0] = forager_group[current_scout_index]
                self.scout_bees[scout_position] = forager_group[current_scout_index]
                    

            

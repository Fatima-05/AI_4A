import random
import math

class GA:
    def __init__(self, individual_size=8,population_size=200):
        self.n=individual_size
        self.population_size=population_size
        self.population={}
        self.total_fitness=0
        self.initialize_population()

    def initialize_population(self):
        for i in range(self.population_size):
            individual=list(range(self.n))
            random.shuffle(individual)
            fitness=self.calculate_fitness(individual)
            self.population[i]=[individual[:],fitness]
            self.total_fitness+=fitness

    def calculate_fitness(self,individual):
        attacks=0
        for i in range(self.n):
            for j in range(i+1,self.n):
                if abs(i-j)==abs(individual[i]-individual[j]):
                    attacks+=1
        total_pairs=self.n*(self.n-1)//2
        return total_pairs-attacks

    def update_population_fitness(self):
        self.total_fitness=0
        for i in range(self.population_size):
            fitness=self.calculate_fitness(self.population[i][0])
            self.population[i][1]=fitness
            self.total_fitness+=fitness

    def select_parents(self):
        roulette_wheel=[]
        wheel_size=self.population_size*5
        fitnesses=[self.population[i][1] for i in range(self.population_size)]
        total_f=sum(fitnesses) or 1

        for i in range(self.population_size):
            length=max(1,round(wheel_size*(fitnesses[i]/total_f)))
            roulette_wheel.extend([i]*length)
        random.shuffle(roulette_wheel)
        new_generation={}
        for i in range(self.population_size):
            parent_idx=roulette_wheel[random.randint(0,len(roulette_wheel)-1)]
            new_generation[i]=[self.population[parent_idx][0][:],self.population[parent_idx][1]]
        self.population = new_generation
        self.update_population_fitness()

    def generate_children(self,crossover_probability=0.8):
        num_pairs=round(crossover_probability*self.population_size/2)
        indices=list(range(self.population_size))
        random.shuffle(indices)
        i=0
        while i<num_pairs*2 and i+1<self.population_size:
            p1=self.population[indices[i]][0]
            p2=self.population[indices[i+1]][0]

            child1=self.order_crossover(p1,p2)
            child2=self.order_crossover(p2,p1)

            self.population[indices[i]]=[child1,0]
            self.population[indices[i+1]]=[child2,0]
            i+=2
        self.update_population_fitness()

    def order_crossover(self,parent1,parent2):
        size=len(parent1)
        start,end=sorted(random.sample(range(size),2))
        child=[None]*size
        child[start:end]=parent1[start:end]

        pos=end%size
        for gene in parent2:
            if gene not in child:
                while child[pos] is not None:
                    pos=(pos+1)%size
                child[pos]=gene
                pos=(pos+1)%size
        return child

    def mutate_children(self,mutation_probability=0.1):
        num_mutations=round(mutation_probability*self.population_size*self.n)
        total_indices=list(range(self.population_size*self.n))
        random.shuffle(total_indices)
        swap_locations=random.sample(total_indices,min(num_mutations,len(total_indices)))
        for loc in swap_locations:
            ind_idx=loc//self.n
            pos1=loc%self.n
            pos2=random.randint(0,self.n-1)
            while pos2==pos1:
                pos2=random.randint(0,self.n-1)
            individual=self.population[ind_idx][0]
            individual[pos1],individual[pos2]=individual[pos2],individual[pos1]
        self.update_population_fitness()

    def has_solution(self):
        target=self.n*(self.n-1)//2
        for i in range(self.population_size):
            if self.population[i][1]==target:
                return True,self.population[i][0]
        return False, None


def main():
    ga=GA(individual_size=8,population_size=200)
    generation=0
    max_gen=5000
    while generation<max_gen:
        ga.select_parents()
        ga.generate_children(0.85)
        ga.mutate_children(0.12)
        found,solution=ga.has_solution()
        if found:
            print(f"Solution found at generation {generation}")
            print("Queen column positions row 0-7:")
            print(solution)
            break
        if generation % 50 == 0:
            best=max(ga.population[i][1] for i in range(ga.population_size))
            print(f"Gen:{generation:3d}\nBest fitness: {best}/28")
        generation+=1
    else:
        print("Max generations reached without perfect solution")

if __name__ == "__main__":
    main()
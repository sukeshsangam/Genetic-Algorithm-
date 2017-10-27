import random
import numpy as np
import matplotlib.pyplot as plt

def ackley(x):
	arg1 = -0.2 * np.sqrt(0.5*(x[0]**2+x[1]**2))
	arg2 = 0.5 * (np.cos(2. *np.pi*x[0]) + np.cos(2. *np.pi*x[1]))
	return -20. * np.exp(arg1) - np.exp(arg2)
	

def check_bounds(vec, bounds):

    vec_new = []
    for i in range(len(vec)):
        if vec[i] < bounds[i][0]:
            vec_new.append(bounds[i][0])
        if vec[i] > bounds[i][1]:
            vec_new.append(bounds[i][1])
        if bounds[i][0] <= vec[i] <= bounds[i][1]:
            vec_new.append(vec[i])
    return vec_new
	
def de(fun,bounds,population_size,mutate,recombination,maxiter):
	
	minimum_points=[]
	x_plot=[]
	y_plot=[]
	for i in range(0,100):
		population=[]
		for c in range(0,population_size):
			new_point=[]
			for k in range(len(bounds)):
				new_point.append(random.uniform(bounds[k][0],bounds[k][1]))
			population.append(new_point)
		#print("Run no. ")
		#print(i)
		termination_flag=0
		#score_temp=0
		while(termination_flag<100):
			for j in range(0, population_size):
				indexes = list(range(0,population_size))
				indexes.remove(j)
				random_index = random.sample(indexes, 3)
				var_1 = population[random_index[0]]
				var_2 = population[random_index[1]]
				var_3 = population[random_index[2]]
				var_t = population[j]
				var_diff = [var_2_i - var_3_i for var_2_i, var_3_i in zip(var_2, var_3)]
				var_donor = [var_1_i + mutate * var_diff_i for var_1_i, var_diff_i in zip(var_1, var_diff)]
				var_donor = check_bounds(var_donor, bounds)
				var_temp = []
				for k in range(len(var_t)):
					crossover = random.uniform(0,1)
					if crossover <= recombination:
						var_temp.append(var_donor[k])

					else:
						var_temp.append(var_t[k])
				#print(var_temp)
				score_temp  = func(var_temp)
				score_target = func(var_t)

				if score_temp < score_target:
					#print(score_temp)
					#print(var_temp)
					population[j] = var_temp
					termination_flag=0
				else:
					termination_flag=termination_flag+1
		#print(score_temp)
		minimum_points.append(var_temp)
		x_plot.append(score_temp)
		y_plot.append(i)
	print(min(x_plot))
	print(minimum_points[x_plot.index(min(x_plot))])
	plt.xlabel('Runs')
	plt.ylabel('Minimum Value')
	plt.title('Differential Evolution')
	plt.plot(y_plot, x_plot)
	plt.show()	
		

		
func = ackley	                    # Cost function
bounds = [(-5,5),(-5,5)]            # Bounds [(x1_min, x1_max), (x2_min, x2_max),...]
population_size = 20                        # Population size, must be >= 4
mutation = 1.2                        # Mutation factor [0,2]
recombination = 0.7                 # Recombination rate [0,1]
maxiter = 100   
de(func,bounds,population_size,mutation,recombination,maxiter)
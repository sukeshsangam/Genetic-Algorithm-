import random
import numpy as np
import matplotlib.pyplot as plt

def get_random_point(x,y):
	x_new = (random.uniform(0,0.9999)-0.5)*0.1+x
	y_new = (random.uniform(0,0.9999)-0.5)*0.1+y
	return [x_new,y_new]
	


#print(x)
#print(y)

def ackley(x):
	arg1 = -0.2 * np.sqrt(0.5*(x[0]**2+x[1]**2))
	arg2 = 0.5 * (np.cos(2. *np.pi*x[0]) + np.cos(2. *np.pi*x[1]))
	return -20. * np.exp(arg1) - np.exp(arg2) 

	

#print(initial_value)
j=0
graphx=[]
graphy=[]
minimum_points=[]
for i in range(0,100):
	x = (random.uniform(-5,5)-0.5)*0.1

	y = (random.uniform(-5,5)-0.5)*0.1
	
	point=get_random_point(x,y)
	initial_value=ackley(point)
	
	while(j<100):
		point=get_random_point(x,y)
		value=ackley(point)
		if value<initial_value:
			j=0
			initial_value=value
			minimum_point=point
		else:
			j=j+1
	print(initial_value)
	graphx.append(i)
	graphy.append(initial_value)
	minimum_points.append(minimum_point)
	
print("minimum value from whole generations")
print(min(graphy))
print("at point")

temp=min(graphy)

#print("hello1")
index_m=graphy.index(temp)

#print(index_m)

final_point=minimum_points[index_m]

#print("hello3")
print(final_point)

#print(minimum_point)
plt.ylabel('Minimum Value')
plt.xlabel('Runs')
plt.title('Hill climbing Search')
plt.plot(graphx, graphy)
plt.show()
from itertools import accumulate
import sys
import itertools
import math
import random
from copy import deepcopy


if len(sys.argv) < 2:
	print ("you must provide a textfile in system argument")
	exit(0)




def read_file(textfile):
	f=open(textfile)
	for i in range(7):
		f.readline()
	lines = f.readlines()
	lines = lines[:-1]
	initial_points=[]
	for line in lines:
		temp=[]
		temp=line.split(' ')
		initial_points.append([float(temp[1]),float(temp[2].replace("\n",""))])
	f.close()
	return initial_points
	



def perform_crossover(list_for_crossover,a,b):
	# print("a,b")
	# print(a)
	# print(b)
	# print("initial_set inside perform_crossover")
	# for i in list_for_crossover:
		# print(i)
	first_list = [0] * len(list_for_crossover[0])
	#print("first_list inside perform_crossover")
	#print(first_list)
	
	start_index=random.randint(0,len(list_for_crossover[a])-3)
	end_index=random.randint(start_index+1,len(list_for_crossover[a])-1)
	# print("start_index")
	# print(start_index)
	# print("end_index")
	# print(end_index)
	temp_end_index=end_index+1
	temp_2=end_index+1
	for i in range(start_index,end_index+1):
		first_list[i]=list_for_crossover[a][i]
	for i in range(0,len(first_list)):
		if temp_end_index==len(list_for_crossover[b]):
			temp_end_index=0
		if temp_2==len(list_for_crossover[b]):
			temp_2=0
	
	
		if list_for_crossover[b][temp_end_index] not in first_list:
			first_list[temp_2]=list_for_crossover[b][temp_end_index]
			temp_2=temp_2+1
		
		temp_end_index=temp_end_index+1
	return first_list







	
	
def distance(p1,p2):
	distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
	#print(distance)
	return distance
	
city_points=read_file(sys.argv[1])

indices=list(range(0,len(city_points)))
initial_set=[]
count=0
	
while(count<20):
	temp=[]
	random.shuffle(indices)
	temp=indices[:]
	initial_set.append(temp)
	count = count + 1

final_minimum=9999999999
generation=0
while(1):
	
	initial_set_distance=[]
	for i in range(0,len(initial_set)):
		current_path=[]
		current_path=initial_set[i]
		total_distance_currentpath=[]
		for d in range(0,len(current_path)):
			p1=city_points[current_path[d]][:]
			try:
				p2=city_points[current_path[d+1]][:]
			except:
				p2=city_points[0][:]
			total_distance_currentpath.append(distance(p1,p2))		
		initial_set_distance.append(sum(total_distance_currentpath))

	# for i in initial_set_distance:
		# print(i)
	
	if final_minimum>min(initial_set_distance):
		final_minimum=min(initial_set_distance)
		path_index=initial_set_distance.index(final_minimum)
		final_shortest_path=initial_set[path_index]
		generation=0
	else:
		generation=generation+1
	
	if generation==5000:
		exit()
	# final_minimum=min(initial_set_distance)
	# path_index=initial_set_distance.index(final_minimum)
	# final_shortest_path=initial_set[path_index]
	
	
	print("minimum")
	print(final_minimum)

	inverse_distances=[]
	next_step_list_indices=[]
	next_step_list=[]
	next_step_list.extend([final_shortest_path,initial_set[initial_set_distance.index(min(initial_set_distance))]])
	for i in range(0,len(initial_set_distance)):
		inverse_distances.append((1/initial_set_distance[i]))
	sigma_inverse_distance=sum(inverse_distances)
	temp_probabilities=[]
	for i in range(0,len(inverse_distances)):
		temp_probabilities.append((inverse_distances[i])/sigma_inverse_distance)
	final_probabilities=list(accumulate(temp_probabilities))
	count=0
	while(count<18):
		rand=random.uniform(0,1)
		for i in range(0, len(final_probabilities)-1):
			if rand>=final_probabilities[i] and rand<=final_probabilities[i+1]:
				next_step_list_indices.append(i+1)
				break
			else:
				if(rand<final_probabilities[0]):
					next_step_list_indices.append(0)
					break
		count=count+1
	for i in range(0,len(next_step_list_indices)):
		next_step_list.append(initial_set[next_step_list_indices[i]])

	# print(next_step_list_indices)
		
	initial_set=deepcopy(next_step_list)
	# print("after selection")

	# for i in initial_set:
		# print(i)
		
	matured_index=[]
	for i in range(0,len(initial_set)):
		test=random.uniform(0,1)
		if test>0.5:
			matured_index.append(i)
	random.shuffle(matured_index)
	if len(matured_index)%2!=0:
		a_del=random.randint(0,len(matured_index)-1)
		matured_index.pop(a_del)
	# print("matured_index")
	# print(matured_index)
	iter=int(len(matured_index)/2)
	# print("iter")
	# print(iter)

	for i in range(0,iter):
		a=matured_index.pop(random.randint(0,len(matured_index)-1))
		b=matured_index.pop(random.randint(0,len(matured_index)-1))
		list_for_crossover_1=deepcopy(initial_set)
		list_for_crossover_2=deepcopy(initial_set)
		child_one=perform_crossover(list_for_crossover_1,a,b)
		child_two=perform_crossover(list_for_crossover_2,b,a)
		initial_set[a]=child_one
		initial_set[b]=child_two

	# print("after crossover")

	# for i in initial_set:
		# print(i)
		
	mutation_factor=0.5
	for i in range(0,len(initial_set)):
		test=random.uniform(0,1)
		if test>0.5:
			mylist=list(range(len(city_points)))
			a=mylist.pop(random.randint(0,len(mylist)-1))
			b=mylist.pop(random.randint(0,len(mylist)-1))
			temp_a=initial_set[i][a]
			initial_set[i][a]=initial_set[i][b]
			initial_set[i][b]=temp_a

	# print("after mutation")

	# for i in initial_set:
		# print(i)
	
	
	

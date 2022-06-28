# import csv
# import random

# number_of_processes = 250
  
# def randDistribution(upper_bound, lower_bound):
#     value = int(random.gauss(upper_bound, lower_bound))
#     result = value % (upper_bound - lower_bound + 1) + lower_bound
#     return result

#Function to define wait time
# def waitTime(number_of_processes, wait_time, burst_time):
#     wait_time[0] = 0
#     for i in range (1, number_of_processes):
#         wait_time[i] = burst_time[i-1] + wait_time[i-1]

# #Function to define turnaround time
# def turnaroundTime(number_of_processes, wait_time, burst_time, turn_around_time):
#     for i in range(number_of_processes):
#         turn_around_time[i] = burst_time[i] + wait_time[i]

# #Processor Parameters
# cpu_upper_bound = 6
# cpu_lower_bound = 1

# #Memory Size Parameters (in MB)
# memory_upper_bound = 2000
# memory_lower_bound = 1

# process_list = []

# wait_time = [0] * number_of_processes
# turn_around_time = [0] * number_of_processes
# burst_time = [random.randrange(10*10**6, 10*10**12) for i in range(number_of_processes)]

# for i in range(number_of_processes):
#   cpu_cycles = randDistribution(cpu_upper_bound, cpu_lower_bound)
#   memory = randDistribution(memory_upper_bound, memory_lower_bound)
  
#   waitTime(number_of_processes, wait_time, burst_time)
#   turnaroundTime(number_of_processes, wait_time, burst_time, turn_around_time)
  
#   process = [i + 1, cpu_cycles, memory, burst_time[i], wait_time[i], turn_around_time[i]]
#   process_list.append(process)

#   wait_time_total = 0
#   turn_around_time_total = 0
#   wait_time_total = wait_time_total + wait_time[i]
#   turn_around_time_total = turn_around_time_total + turn_around_time[i]
# # Open or Create File to Write Data
# with open('FIFO.csv', 'w', newline='') as csvfile:
#     # Initialize Writer Class
#     writer = csv.writer(csvfile, delimiter="\t")

#     # Write Column Headers
#     writer.writerow(['Process ID', 'CPU Cycles', 'Memory', 'Burst Times', 'Wait Times', 'Turn Around Times'])
#     # Write Process Data
#     writer.writerows(process_list)

# print("Average Wait Time = " + str(wait_time_total/number_of_processes))
# print("Average Turn Around Time = " + str(turn_around_time_total/number_of_processes))


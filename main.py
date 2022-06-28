import csv
import random

def customNormalDistribution(upper_bound, lower_bound, mean, std_deviation):
    value = int(random.gauss(mean, std_deviation))
    result = value % (upper_bound - lower_bound + 1) + lower_bound
    return result

number_of_processes = 250
def waitTime(number_of_processes, burst_time, wait_time, turn_around_time):
    wait_time[0] = 0
  
# CPU Cycle Distribution Parameters
cpu_upper_bound = 6
cpu_lower_bound = 1
cpu_mean = 4
cpu_std_deviation = 5

# Memory Requirement Distribution Parameters
memory_upper_bound = 2000
memory_lower_bound = 1
memory_mean = 8000
memory_std_deviation = 11000

process_list = []
burst_time = [random.randrange(10*10**6, 10*10**12) for i in range(number_of_processes)]

for i in range(number_of_processes):
    cpu_cycles = customNormalDistribution(cpu_upper_bound, memory_lower_bound, memory_mean, memory_std_deviation)
    memory = customNormalDistribution(memory_upper_bound, memory_lower_bound, memory_mean, memory_std_deviation)
  
    process = [i + 1, burst_time[i], memory]
    process_list.append(process)

# Open or Create File to Write Data
with open('processes.csv', 'w', newline='') as csvfile:
    # Initialize Writer Class
    writer = csv.writer(csvfile, delimiter="\t")

    # Write Column Headers
    writer.writerow(['Process ID', 'Burst Time (cycles)', 'Memory (MB)'])
    # Write Process Data
    writer.writerows(process_list)
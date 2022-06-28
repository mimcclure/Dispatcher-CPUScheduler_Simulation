import csv
import random
from csv import reader, writer

cpu_lower_bound = 1
cpu_upper_bound = 6
num_of_cpus = (cpu_upper_bound - cpu_lower_bound)

def cpuDistribution(upper_bound, lower_bound):
    value = int(random.gauss(upper_bound, lower_bound))
    result = value % (upper_bound - lower_bound + 1) + lower_bound
    return result

def get_next_process_index(rem_burst_time, current_cpus):
    # Determine the next process by order of appearance.

    # Make a list of all the processes on all of the CPUs
    # (prevents scheduling twice)
    all_procs_running = [-1] * num_of_cpus
    for j in range(num_of_cpus):
        all_procs_running[j] = current_cpus[j][0]

    for i in range(n):
        if (rem_burst_time[i] > 0):
            if i not in all_procs_running:
                return i

    return -1

def wt_find(processes, n, burst_time, wait_time, quantum):
    rem_burst_time = [0] * n
    
    for i in range(n):
        rem_burst_time[i] = burst_time[i]
    
    # Global time in units
    t = 0
    time_increment = quantum

    # Each CPU has a current process ID running + time left on those processes.
    # init to negative as process index of zero is valid
    cpus = [[-1]*2 for i in range(num_of_cpus)]
    
    done = False
    while(not done):
        # Schedules any process if there is room.
        for cpu_index in range(num_of_cpus):
            # Index 0 = process ID
            # Index 1 = remaining time
            if cpus[cpu_index][0] < 0 or cpus[cpu_index][1] <= 0:
                # Schedule the process if:
                # 1.) There is no process ID running on this CPU (-1)
                # 2.) The process is "done" on this CPU (0 time left)
                process_index = get_next_process_index(rem_burst_time, cpus)

                # Return -1 if there are no more tasks available to run.
                if process_index >= 0:
                    cpus[cpu_index][0] = process_index

                    if rem_burst_time[process_index] > quantum:
                        # Schedule one process for the time being if there is
                        # more than one quantum of processing time left.
                        cpus[cpu_index][1] = quantum
                    else:
                        # Less than quantum: schedule the remaining
                        cpus[cpu_index][1] = rem_burst_time[process_index]
                else:
                    done = True
                    break
        
        # Advance the time now that all tasks are scheduled.
        for cpu_index in range(num_of_cpus):
            process_index = cpus[cpu_index][0]
            cpus[cpu_index][1] = cpus[cpu_index][1] - time_increment

            if cpus[cpu_index][1] < 0 :
                cpus[cpu_index][1] = 0

            rem_burst_time[process_index] = rem_burst_time[process_index] - time_increment

            if rem_burst_time[process_index] < 0:
                rem_burst_time[process_index] = 0
                wait_time[process_index] = (t + time_increment) - burst_time[process_index]

        t = t + time_increment


def tat_find(processes, n, burst_time, wait_time, turnaround_time):
    for i in range(n):
        turnaround_time[i] = burst_time[i] + wait_time[i]

process_list = []

def avg_time(processes, n, bt, quantum):
    wait_time = [0] * n
    turnaround_time = [0] * n

    wt_find(processes, n, burst_time, wait_time, quantum)
    tat_find(processes, n, burst_time, wait_time, turnaround_time)

    total_wt = 0
    total_tat = 0

    for i in range(n): 
        cpu_cycles = cpuDistribution(cpu_upper_bound, cpu_lower_bound)
        process = [i+1, wait_time[i], turnaround_time[i]]
        process_list.append(process)

        total_wt = total_wt + wait_time[i]
        total_tat = total_tat + turnaround_time[i]

    print("Average waiting time:", (total_wt / n))
    print("Average turn around time:", (total_tat / n))

proc = []
burst_time = []

input_file = open("processes (final).csv")
input_file.readline()
input_reader = reader(input_file, delimiter="\t")

for line in input_reader:    
    proc.append(int(line[0]))
    burst_time.append(int(line[1]))

n = 250
quantum = (10*10**10)

print("Quantum:", quantum)
avg_time(proc, n, burst_time, quantum)

with open('RR.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile, delimiter="\t")
  writer.writerow(['Process ID', 'Wait Time', 'Turnaround Time'])
  writer.writerows(process_list)
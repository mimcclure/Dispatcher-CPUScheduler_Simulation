from csv import reader, writer
from queue import Queue

from CPU import CPU
from Process import Process
from SJF_helper_functions import get_next_cpu, remove_last_processes, complete_stats, sorting_criterion


# Main algorithm
def SJF_3(**args):
    # assumes sorted processes
    queue = Queue()
    duration = 0
    schedule = {}
    for i in range(len(processes)):
        schedule[i + 1] = {}
        
    for process in processes:
        next_cpu = get_next_cpu(args["cpus"])
        duration = next_cpu.ready_at
        if next_cpu.memory == 1 and process.memory > 8000:
            queue.put(process)
            continue
        
        while next_cpu.memory == 2 and not queue.empty():
            queued_process = queue.get()
            schedule[queued_process.id]["wait_time"] = duration
            finished_process = next_cpu.current_process
            if finished_process is not None:
                complete_stats(cpu=next_cpu, process=finished_process, schedule=schedule, duration=duration, waiting=True)
            
            next_cpu.current_process = queued_process
            next_cpu.ready_at = duration + int(queued_process.burst_time / next_cpu.speed)
            next_cpu = get_next_cpu(args["cpus"])
            duration = next_cpu.ready_at

        if next_cpu.memory == 1 and process.memory > 8000:
            queue.put(process)
            continue
        
        schedule[process.id]["wait_time"] = duration
        finished_process = next_cpu.current_process
        if finished_process is not None:
            complete_stats(cpu=next_cpu, process=finished_process, schedule=schedule, duration=duration, waiting=True)
            
        next_cpu.current_process = process
        next_cpu.ready_at = duration + int(process.burst_time / next_cpu.speed)

    remove_last_processes(cpus=args["cpus"],duration=duration, schedule=schedule)
        
    return schedule

input_file = open("processes (final).csv")
input_file.readline() # toss the line containing the headers
input_reader = reader(input_file, delimiter="\t")

processes = []

for line in input_reader:
    process = Process({
        "id":int(line[0]),
        "burst_time":int(line[1]),
        "memory":int(line[2])
    })
    processes.append(process)

processes.sort(key=sorting_criterion)

cpus = []
for i in range(3):
    cpu = CPU({
        "current_process":None,
        "ready_at":0,
        "speed":1,
        "memory":1
    })
    cpus.append(cpu)

for i in range(3):
    cpu = CPU({
        "current_process":None,
        "ready_at":0,
        "speed":2,
        "memory":2
    })
    cpus.append(cpu)    
    
schedule = SJF_3(cpus=cpus)

output_file = open("SJF_3.csv", "w")
output_writer = writer(output_file, delimiter="\t")

output_writer.writerow(["Process ID", "Wait Time (cycles)","Turnaround Time (cycles)"])
for process_id, times in schedule.items():
    output_writer.writerow([process_id, *times.values()])
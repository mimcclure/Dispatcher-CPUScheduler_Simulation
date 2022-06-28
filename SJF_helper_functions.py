# Helper functions
def get_next_cpu(cpus,**args):
    next_cpu = None
    for cpu in cpus:
        if "memory" in args and cpu.memory != 2:
            continue
        if next_cpu is None:
            next_cpu = cpu
            continue
            
        if cpu.ready_at <= next_cpu.ready_at:
            next_cpu = cpu

    return next_cpu

def remove_last_processes(**args):
    cpus = args["cpus"]
    duration = args["duration"]
    schedule = args["schedule"]
    for cpu in cpus:
        finished_process = cpu.current_process
        if finished_process is not None:
            complete_stats(cpu=cpu, process=finished_process, schedule=schedule, duration=duration, waiting=False)
    pass

def complete_stats(**args):
    cpu = args["cpu"]
    duration = args["duration"]
    process = args["process"]
    schedule = args["schedule"]
    waiting = args["waiting"]
    
    stats = schedule[process.id]
    if waiting == True:
        stats["turnaround_time"] = duration
    else:
        stats["turnaround_time"] = stats["wait_time"] + int(process.burst_time / cpu.speed)
        
    cpu.current_process = None

def sorting_criterion(process):
        return process.burst_time
import csv
from time import sleep
import psutil

def read_cpu_usage():
    cpu_t = psutil.cpu_times()
    usr__sp_cputimes = cpu_t[0]
    idle_time = cpu_t.idle
    cpu_dict = {"idle_time": cpu_t.idle, "usr_time": cpu_t.user}
    cpu_dict["interrupt_time"] = cpu_t.irq
    return cpu_dict

def wirte_dict_to_csv(filename, dict_item, is_first_time):
    if is_first_time:
        f = open(filename, "w")
    else:
        f = open(filename, "a")
    w = csv.DictWriter(f, dict_item.keys())
    if is_first_time:
        w.writeheader()
    w.writerow(dict_item)
    f.close()

def read_disks_gb():
    disk = psutil.disk_usage("/")
    disk_dict = {
        "total": disk.total / (2**30),
        "used": disk.used / (2**30),
        "free": disk.free / (2**30),
    }
    return disk_dict

def read_memory_gb():
    mem = psutil.virtual_memory()
    mem_dict  = {
        "total": mem.total / (2**30),
        "used": mem.used / (2**30),
        "free": mem.free / (2**30),
    }
    return mem_dict

if __name__ == "__main__":
    is_first_time = True
    while True:
        cpu_t = read_cpu_usage()
        print(cpu_t)
        print(read_disks_gb())
        print(read_memory_gb())
        #print("user time: " + str(u_t ) + " idle time: " + str(i_t))
        #print("user time: %.2f idle time: %.2f" % (u_t, i_t))
        sleep(1)
        #wirte_dict_to_csv("cpu_usage.csv", cpu_t, is_first_time)
    print("fine")
import subprocess
import re
from db import insert_stat

PIDSTAT_REGEX = re.compile(
    r"\s*(\d+)\s+(\S+)\s+([\d\.]+)\s+([\d\.]+)\s+([\d\.]+)\s+(\d+)\s+(\d+)\s+([\d\.]+)\s+(.+)"
)

def parse_line(line):
    match = PIDSTAT_REGEX.match(line)
    if match:
        pid, user, usr, system, cpu, vsz, rss, mem, command = match.groups()
        return {
            "pid": int(pid),
            "user": user,
            "usr": float(usr),
            "system": float(system),
            "cpu": float(cpu),
            "vsz": int(vsz),
            "rss": int(rss),
            "mem": float(mem),
            "command": command.strip()
        }
    return None

def monitor_pid(pid, interval=1, count=60):
    cmd = ["pidstat", "-p", str(pid), str(interval), str(count)]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    for line in process.stdout:
        stat = parse_line(line)
        if stat:
            insert_stat(stat)
            print(stat)

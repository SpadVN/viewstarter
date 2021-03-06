import psutil
from restarter import restart


def checkifprocessrunning(processname):
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processname.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    restart();

import platform
import subprocess

def get_os_info():
    return platform.platform()

def run_command(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode()}"

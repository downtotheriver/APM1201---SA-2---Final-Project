import subprocess

def run_adb_command(command):
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout

# Run the adb command to pull all call logs
all_call_logs_output = run_adb_command(["adb", "shell", "content", "query", "--uri", "content://call_log/calls"])

# Split the output into individual call log entries
call_logs_entries = all_call_logs_output.strip().split('\n')

# Open a file in write mode
with open("call_logs.txt", "w") as file:
    # Write each call log entry to the file
    for call_log in call_logs_entries:
        file.write(call_log + "\n")

import subprocess

# List of Python files to run
file_list = ['a.py', 'b.py', 'c.py','update.py']

# Function to run a Python file
def run_python_file(file):
    subprocess.run(['python3', file])

# Run each file in a separate process
processes = []
for file in file_list:
    process = subprocess.Popen(['python3', file])
    processes.append(process)

# Wait for all processes to finish
for process in processes:
    process.wait()

print("All files executed.")

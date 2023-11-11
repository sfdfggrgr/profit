import subprocess

# List of Python files to run
file_list = ['a.py', 'b.py', 'c.py','update.py']

# Function to run a Python file
def run_python_file(file):
    subprocess.run(['python', file])

# Run each file in a separate process
processes = []
for file in file_list:
    process = subprocess.Popen(['python', file])
    processes.append(process)

# Wait for all processes to finish
for process in processes:
    process.wait()

print("All files executed.")

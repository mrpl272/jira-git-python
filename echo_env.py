# echo_env.py

import os

# Get the environment variable
name = os.getenv('NAME')

# Define the command as a list of strings
command = ['echo', name]

# Run the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the output
print(result.stdout)

# Check for errors
if result.returncode != 0:
    print(f"Error: {result.stderr}")

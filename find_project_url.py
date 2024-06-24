# find_project_url.py
import json
import sys

def main():
    with open('projects.json', 'r') as f:
        projects = json.load(f)

    found = False
    for project in projects:
        if project['name'] == 'Example2234757y784373':
            print(project['self'])
            found = True
            break

    if not found:
        print("Project 'Example2234757y784373' not found.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

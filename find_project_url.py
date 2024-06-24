# find_project_url.py
import json

def main():
    with open('projects.json', 'r') as f:
        projects = json.load(f)

    for project in projects:
        if project['name'] == 'Example2234757y784373':
            print(project['self'])

if __name__ == "__main__":
    main()

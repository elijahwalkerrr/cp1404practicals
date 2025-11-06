""" Time Estimation: 40mins """

from prac_07.project import Project

DEFAULT_FILE = "projects.txt"

def main():
    """Loads the default file"""
    projects = file_load(DEFAULT_FILE)
    print(f"Default file: {DEFAULT_FILE}\n"
          f"Currently loaded: {len(projects)} Projects ")
    choice = print_menu().lower()
    while choice != "q":
        if choice == "l":
            filename = input("Please Enter Filename To Load: ")
            projects = file_load(filename)
            display_projects_list(projects)
        elif choice == "s":
            filename = input("Please Enter Filename To Save: ")
            save_file(filename, projects)
        elif choice == "f":
            projects.sort
            display_projects_list(projects)
        elif choice == "a":
            projects.append(add_new_project())
        elif choice == "d":
            display_projects_status(projects, "completed")
            display_projects_status("incomplete")
        elif choice == "u":
            display_projects_list(projects)
            projects = update_project(projects)
        else:
            print("Invalid Input: Try Again")
        choice = print_menu().lower()

def print_menu():
    print("\n- (L)oad Projects\n"
          "- (S)ave Projects\n"
          "- (D)isplay Projects\n"
          "- (F)ilter Projects by Date\n"
          "- (A)dd New Project\n"
          "- (U)pdate Project\n"
          "- (Q)uit\n")
    choice = input("Select From Menu: ")
    return choice

def file_load(filename):
    projects = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects

def display_projects_list(projects):
    for i, project in enumerate(projects):
        print(f"{i+1}. {project.name}, start: {project.start_date} priority {project.priority}"
              f", estimate: ${project.cost_est}, completion: {project.completion}%")
def display_projects_status(projects, status):
    if {status} == "Completed":
        print(f"Projects Completed: ")
        for i, project in enumerate(projects):
            if project.completed():
                print(f"{i + 1}. {project.name}, start: {project.start_date} priority {project.priority}"
              f", estimate: ${project.cost_est}, completion: {project.completion}%")
    else:
        print("Projects Incomplete:")
        for i, project in enumerate(projects):
            if not project.completed():
                print(f"{i + 1}. {project.name}, start: {project.start_date} priority {project.priority}"
                  f", estimate: ${project.cost_est}, completion: {project.completion}%")

def save_file(filename, projects):
    """Saves file with headings included"""
    with open(filename, "w") as file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage")
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_est}\t"
                  f"{project.completion}\t")

def add_new_project():
    name = input("Name: ")
    start_date = input("Start Date: ")
    priority = int(input("Priority: "))
    cost_est = float(input("Cost Estimate: "))
    completion = float(input("Completion (%): "))
    return Project(name, start_date, priority,cost_est, completion)

def update_project(projects):
    project_selection = int(input("Select Number of Book to Alter"))
    project_choice = projects[project_selection]
    project_choice.update()
    return projects



main()
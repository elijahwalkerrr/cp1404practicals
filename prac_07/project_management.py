""" Time Estimation: 40mins """
from datetime import datetime
from prac_07.project import Project

DEFAULT_FILE = "projects.txt"

def main():
    """Loads the default file, displays the menu, and processes user choices.
    Allows the user to load, save, display, add filter and update projects."""
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
            filter_projects(projects)
        elif choice == "a":
            projects.append(add_new_project())
        elif choice == "d":
            display_projects_status(projects, "completed")
            display_projects_status(projects, "incomplete")
        elif choice == "u":
            display_projects_list(projects)
            projects = update_project(projects)
        else:
            print("Invalid Input: Try Again")
        choice = print_menu().lower()
    save_choice = input("Would you like to save to projects.txt?")
    if save_choice =="Yes":
        save_file(DEFAULT_FILE, projects)
        print("Thank you for using custom-built project management software.")
    else:
        print("Thank you for using custom-built project management software.")

def print_menu():
    """ Prints a Menu detailing options of input."""
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
    """Loads a user inputted program and returns the projects listed."""
    projects = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects

def display_projects_list(projects):
    """Iterates and prints the objects in the projects list"""
    for i, project in enumerate(projects):
        print(f"{i+1}. {project.name}, start: {project.start_date} priority {project.priority}"
              f", estimated cost: ${project.cost_est}, completion: {project.completion}%")

def filter_projects(projects):
    """ Filters the projects if they are dated before user specified input"""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = []
    for project in projects:
        if isinstance(project.start_date, str):
            project_date = datetime.strptime(project.start_date, "%d/%m/%Y").date()
        else:
            project_date = project.start_date

        if project_date > filter_date:
            filtered.append(project)

    filtered.sort()
    print("\nFiltered projects:")
    for i, project in enumerate(filtered, start=1):
        print(f"{i}. {project.name}, start: {project.start_date}, priority {project.priority}, "
              f"estimate: ${project.cost_est}, completion: {project.completion}%")

def display_projects_status(projects, status):
    """ Display the projects that are either completed or uncompleted """
    print(f"Projects {status}: ")
    for i, project in enumerate(projects):
        if int(project.completion) >= 100 and status == "completed" or (status == "incomplete" and
                                                                            int(project.completion) < 100):
            print(f"{i + 1}. {project.name}, start: {project.start_date} priority {project.priority}"
             f", estimate: ${project.cost_est}, completion: {project.completion}%")


def save_file(filename, projects):
    """Saves file with headings included"""
    with open(filename, "w") as file:
        file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_est}\t"
                  f"{project.completion}\t")

def add_new_project():
    """User Input adds returns a new Project object"""
    name = input("Name: ")
    start_date = input("Start Date: ")
    priority = int(input("Priority: "))
    cost_est = float(input("Cost Estimate: "))
    completion = float(input("Completion (%): "))
    return Project(name, start_date, priority,cost_est, completion)

def update_project(projects):
    """ Updates a project using class method"""
    project_selection = int(input("Select Number of Book to Alter"))
    project_choice = projects[project_selection]
    project_choice.update()
    return projects



main()
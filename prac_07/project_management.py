""" Time Estimation: 40mins """
from prac_07.project import Project


def main():
    projects =file_load("projects.txt")
    display_projects(projects)

def print_menu():
    print("(L)oad Projects: "
          "(S)ave Projects: "
          "(D)isplay Projects: "
          "(F)ilter Projects by Date: "
          "(A)dd New Project: "
          "(U)pdate Project: ")
    option = input("Select From Menu: ")
    return option

def file_load(filename):
    projects = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            parts = line.strip().split('\t')
            pject = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(pject)
    return projects

def display_projects(projects):
    for project in projects:
        print(project)

def save_file(filename, projects):
    """Saves file with headings included"""
    with open(filename, "w") as file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage")
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_est}\t"
                  f"{project.completion}\t")


main()
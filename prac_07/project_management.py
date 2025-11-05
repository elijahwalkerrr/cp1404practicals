""" Time Estimation: 40mins """
from prac_07.project import Project


def main():
    projects =file_load("projects.txt")
    display_projects(projects)


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

main()
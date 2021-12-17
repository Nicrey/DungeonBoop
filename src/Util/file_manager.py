import os
import sys

import numpy

from src.Model.project import Project


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class FileManager:

    def __init__(self):
        # Init Folder Structure
        # Create Projects folder
        try:
            os.mkdir(resource_path('Projects'))
            print("Projects Directory created.")
        except FileExistsError:
            print('Projects Directory already exists.')

    def load_projects(self):
        projects = os.listdir(resource_path('Projects/'))
        # Return list of projects by looking at folders in projects folder
        return [Project(project) for project in projects]

    def load_project(self, name):
        # Loads all data for a project into a project class
        # Todo.md: Check if save exists, if not return empty pixels array
        return numpy.loadtxt(f'Projects/{name}/save')

    def save_project(self, name):
        # Saves all data from a project
        pass


FILES = FileManager()
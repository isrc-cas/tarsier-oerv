import sys
import requests
import datetime
import csv
import configparser
import logging
from time import sleep
from xml.etree import ElementTree
from rich.progress import track
from rich.logging import RichHandler
from pathlib import Path

# Logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[RichHandler(show_time=False, show_path=False, keywords=[
                          "total", "packages", "Fetching"], rich_tracebacks=True)]
)
logger = logging.getLogger(__name__)

# Config
config = configparser.ConfigParser(delimiters=('='))
config.optionxform = str
config.read(["config.ini", "project.ini"])

startTimeStr = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
projects = []


class Package:
    def __init__(self, name: str):
        self.name = name
        self.version = ""


class Project:
    def __init__(self, name: str, repo: str, arch: str):
        self.name = name
        self.repository = repo
        self.arch = arch
        self.packageList = []


def fetchProjectList(username: str, password: str, baseURL: str) -> list:
    """
    Fetch all project names from OBS
    Return: list of project names
    """
    projectList = []
    logger.info("Fetching project list with account: %s", username)
    url = baseURL + "/source"
    headers = {"User-Agent": "PLCT-Tracker/0.1"}
    try:
        response = requests.get(url, headers=headers,
                                auth=(username, password))
        if response.status_code == 401:
            logger.error(
                "Authentication failed, please check your username and password")
            sys.exit(1)
        elif response.status_code == 200:
            xmlTree = ElementTree.fromstring(response.text)
            for project in xmlTree:
                projectList.append(project.attrib["name"])
        else:
            logger.error(
                "Failed to fetch project list with HTTP status code: %s", response.status_code)
            sys.exit(1)
    except Exception as e:
        logger.error("Failed to fetch project list")
        logger.error(e)
        sys.exit(1)
    return projectList


def fetchProjectRepos(projectName: str, username: str, password: str, baseURL: str) -> list:
    """
    Fetch all repositories in a project
    projectName: name of the project
    Return: list of repositories
    """
    repoList = []
    logger.info("Fetching repository list: %s", projectName)
    url = baseURL + "/build/" + projectName
    headers = {"User-Agent": "PLCT-Tracker/0.1"}
    try:
        response = requests.get(url, headers=headers,
                                auth=(username, password))
        if response.status_code == 200:
            xmlTree = ElementTree.fromstring(response.text)
            for repo in xmlTree:
                repoList.append(repo.attrib["name"])
        else:
            logger.error(
                "Failed to fetch repository list with HTTP status code: %s", response.status_code)
            sys.exit(1)
    except Exception as e:
        logger.error("Failed to fetch repository list")
        logger.error(e)
        sys.exit(1)
    return repoList


def addProject(projectName: str, projectRepo: list, arch: str, username: str, password: str, baseURL: str):
    """
    Add a project to the project list (projects)
    projectName: name of the project
    projectRepo: list of repositories
    arch: architecture
    """
    totalRepos = fetchProjectRepos(projectName, username, password, baseURL)

    # if projectRepo is empty, fetch all repositories
    if projectRepo == ['']:
        projectRepo = totalRepos.copy()
    # Check if the project has the specified repository
    for repo in projectRepo:
        if repo not in totalRepos:
            logger.error("Repository %s not found in project %s",
                         repo, projectName)
            sys.exit(1)
        project = Project(projectName, repo, arch)
        projects.append(project)
    return


def fetchPackageList(project: Project, username: str, password: str, baseURL: str):
    """
    Fetch all packages in a project
    project: project object
    """
    logger.info("Fetching package list: %s -> %s -> %s",
                project.name, project.repository, project.arch)
    url = baseURL + "/source/" + project.name
    headers = {"User-Agent": "PLCT-Tracker/0.1"}
    try:
        response = requests.get(url, headers=headers,
                                auth=(username, password))
        if response.status_code == 200:
            xmlTree = ElementTree.fromstring(response.text)
            for package in xmlTree:
                project.packageList.append(Package(package.attrib["name"]))
        else:
            logger.error("Failed to fetch package list in %s -> %s with HTTP status code: %s",
                         project.name, project.repository, response.status_code)
            sys.exit(1)
    except Exception as e:
        logger.error("Failed to fetch package list")
        logger.error(e)
        sys.exit(1)
    logger.info("Finished fetching package list: %s -> %s -> %s, total %s packages",
                project.name, project.repository, project.arch, len(project.packageList))
    return


def fetchAllPackageVersions(project: Project, username: str, password: str, baseURL: str):
    """
    Fetch all package versions in a project
    project: project object
    """
    for package in track(project.packageList, description=project.name + " -> " + project.repository + " -> " + project.arch):
        url = baseURL + "/build/" + project.name + "/" + \
            project.repository + "/" + project.arch + "/" + "_jobhistory"
        headers = {"User-Agent": "PLCT-Tracker/0.1"}
        payload = {"package": package.name, "limit": "1"}
        try:
            response = requests.get(
                url, headers=headers, params=payload, auth=(username, password))
            if response.status_code == 200:
                xmlTree = ElementTree.fromstring(response.text)
                for job in xmlTree:
                    package.version = job.attrib["versrel"]
                logger.debug("Package %s -> %s -> %s -> %s, Version: %s", project.name,
                             project.repository, project.arch, package.name, package.version)
            else:
                logger.error("Failed to fetch package version in %s -> %s -> %s -> %s with HTTP status code: %s",
                             project.name, project.repository, project.arch, package.name, response.status_code)
                return
        except Exception as e:
            logger.error("Failed to fetch package version")
            logger.error(e)
            return
        sleep(0.1)
    successCounter = 0
    failedCounter = 0
    for package in project.packageList:
        if package.version != "":
            successCounter += 1
        else:
            failedCounter += 1
    logger.info("Finished: %s -> %s -> %s, total [%s] packages, [%s] [bold green]success[/], [%s] [bold red]failed[/]", project.name,
                project.repository, project.arch, len(project.packageList), successCounter, failedCounter, extra={"markup": True})
    return


def outputProjectToCSV(project: Project):
    """
    Output project to CSV file
    project: project object
    """
    filename = Path(startTimeStr + "/" + project.name.replace(':', '+') +
                    "+" + project.repository.replace(':', '+') + ".csv")
    filename.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Package", "Version"])
            for package in project.packageList:
                writer.writerow([package.name, package.version])
        logger.info("Output to CSV file: %s", filename)
    except Exception as e:
        logger.error("Failed to output project to CSV")
        logger.error(e)
        sys.exit(1)
    return


def main():
    username = config["OBS"]["username"]
    password = config["OBS"]["password"]
    baseURL = config["OBS"]["baseurl"]

    # Get All Projects Section in project.ini
    projectList = config.sections()[1:]
    totalProjectList = fetchProjectList(username, password, baseURL)
    for project in projectList:
        if project not in totalProjectList:
            logger.error("Project %s not found", project)
            sys.exit(1)
        else:
            projectRepo = [item.strip()
                           for item in config[project]["repo"].split(",")]
            addProject(project, projectRepo,
                       config[project]["arch"], username, password, baseURL)

    # Fetch package list and package version
    for project in projects:
        fetchPackageList(project, username, password, baseURL)
        fetchAllPackageVersions(project, username, password, baseURL)
        outputProjectToCSV(project)
    return


if __name__ == "__main__":
    main()

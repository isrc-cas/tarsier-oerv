import random
import sys
import logging
import datetime
from time import sleep
import pytz
import requests
import json
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import configparser
from rich.progress import track

configFile = 'config.ini'
configer = configparser.RawConfigParser()
configer.read(configFile)


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class User:
    def __init__(self, userName: str):
        self.userID = ""
        self.userName = userName
        self.PRs = []


class PR:
    def __init__(self):
        self.link = ""
        self.startTime = ""
        self.updateTime = ""
        self.title = ""
        self.status = ""
        self.sig = ""


def getUserIDByUsername(user: User):
    """
    Get User ID by Username
    user: User object
    user.userName Must be set
    """
    access_token = configer['Gitee']['token']
    url = 'https://gitee.com/api/v5/users/{username}?access_token={access_token}' \
        .format(username=user.userName, access_token=access_token)
    headers = {'user-agent': 'PLCT-Tracker/0.1'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user.userID = response.json()['id']
            logger.info('Get userID for ' + user.userName +
                        ': ' + str(user.userID))
        elif response.status_code == 403:
            logger.error('Get userID for ' + user.userName + ' failed, status code: ' +
                         str(response.status_code) + ', might rate limited')
        else:
            logger.error('Get userID for ' + user.userName +
                         ' failed, status code: ' + str(response.status_code))
        response.close()
    except Exception as e:
        logger.error('Get userID for ' + user.userName +
                     ' failed, error: ' + str(e))
        sys.exit(1)
    return


def getUserPRList(user: User, org: str, startTime: datetime, endTime: datetime, pages: int = 1):
    """
    Get PR list for a user using web spider
    user: User object
    org: str, organization name, e.g. 'src-openeuler'
    """
    if user.userID == "":
        logger.error('User ' + user.userName + ' has no userID, pass')
        return

    cookie = configer['Gitee']['cookie']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'gitee.com',
        'Cookie': cookie
    }
    url = 'https://gitee.com/organizations/{org}/pull_requests?assignee_id=&author_id={userID}&label_ids=&label_text=&milestone_id=&page={pages}&priority=&project_id=&project_type=&search=&single_label_id=&single_label_text=&skip_user=true&sort=created_at+desc&status=all&target_project=' \
        .format(userID=user.userID, org=org, pages=pages)

    format = '%Y-%m-%d %H:%M:%S %z'
    logger.info('Get PR list for ' + user.userName +
                ' in ' + org + ' on page ' + str(pages))
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            c = soup.find(
                class_="panel-list mt-2").findAll(class_='panel-list')
            # No more PRs found by this user
            if len(c) == 0:
                logger.info('No PR found for ' + user.userName +
                            ' in page ' + str(pages))
                return
            for PRData in c:
                _PR = PR()
                _PR.link = PRData.find("a", class_="title")['href']
                _PR.startTime = datetime.datetime.strptime(PRData.find(
                    "span", class_="timeago latest-timeago")['title'], format)
                # Remove PRs that are newer than endTime
                if _PR.startTime > endTime:
                    continue
                # Find the last PR before the start time
                if _PR.startTime < startTime:
                    logger.info('PR ' + _PR.link + ' was created on ' +
                                str(_PR.startTime) + ' and it is older than set, done')
                    return
                user.PRs.append(_PR)
        else:
            logger.error('Get PRs for ' + user.userName +
                         ' failed, status code: ' + str(response.status_code))
    except Exception as e:
        logger.error('Get PRs for ' + user.userName +
                     ' failed, error: ' + str(e))
    sleep(1)
    getUserPRList(user=user, org=org, startTime=startTime,
                  endTime=endTime, pages=pages + 1)


def getPRDetails(PR: PR):
    """
    Get PR details by PR link
    PR: PR object
    """
    PRLink = PR.link.split('/')
    access_token = configer['Gitee']['token']
    url = 'https://gitee.com/api/v5/repos/{owner}/{repo}/pulls/{number}?access_token={access_token}' \
        .format(owner=PRLink[1], repo=PRLink[2], number=PRLink[4], access_token=access_token)
    headers = {'user-agent': 'PLCT-Tracker/0.1'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            details = response.json()
            PR.startTime = datetime.datetime.strptime(
                details['created_at'], '%Y-%m-%dT%H:%M:%S%z')
            PR.updateTime = datetime.datetime.strptime(
                details['updated_at'], '%Y-%m-%dT%H:%M:%S%z')
            PR.status = details['state']
            PR.title = details['title']
            for label in details['labels']:
                if label['name'].find('sig/') != -1:
                    PR.sig = label['name']
        else:
            logger.error('Get PR details for ' + PR.link +
                         ' failed, status code: ' + str(response.status_code))
    except Exception as e:
        logger.error('Get PR details for ' + PR.link +
                     ' failed, error: ' + str(e))
    return


def outputASCIITable(userData):
    x = PrettyTable()
    x.field_names = ["用户名", "组织名", "仓库名", "标题", "发起时间", "更新时间", "状态", "SIG"]
    for user in userData:
        for PR in user.PRs:
            x.add_row([user.userName, PR.link.split('/')[1], PR.link.split('/')[2], PR.title,
                      PR.startTime, PR.updateTime, PR.status, PR.sig])
    print(x)


def outputCSV(userData):
    url = 'https://gitee.com'
    x = PrettyTable()
    x.field_names = ["用户名", "组织名", "仓库名", "标题",
                     "发起时间", "更新时间", "状态", "SIG", "请求链接", ]
    for user in userData:
        for PR in user.PRs:
            x.add_row([user.userName, PR.link.split('/')[1], PR.link.split('/')[2], PR.title,
                      PR.startTime, PR.updateTime, PR.status, PR.sig, url + PR.link])
    with open(str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")) + '.csv', 'w', newline='') as f_output:
        f_output.write(x.get_csv_string())


def testGiteeLogin() -> bool:
    """
    Test if the Gitee cookie is valid
    Return: True if the cookie is valid, False otherwise
    """
    cookie = configer['Gitee']['cookie']
    if cookie == '':
        logger.error('No cookie found, please set it in config.ini')
        return False
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'gitee.com',
        'Cookie': cookie
    }
    url = 'https://gitee.com/profile/account_information'
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            logger.info('Login to Gitee successfully')
            try:
                configer.set('Gitee', 'cookie', response.headers['Set-Cookie'])
                configer.write(open(configFile, 'w'))
                return True
            except Exception as e:
                logger.error('Save cookie failed, error: ' + str(e))
                return False
        else:
            logger.error('Login to Gitee failed, status code: ' +
                         str(response.status_code))
    except Exception as e:
        logger.error('Login to Gitee failed, error: ' + str(e))
    return False


def testGiteeToken() -> bool:
    """
    Test if the Gitee token is valid
    Return: True if the token is valid, False otherwise
    """
    token = configer['Gitee']['token']
    access_token = configer['Gitee']['token']
    url = 'https://gitee.com/api/v5/user?access_token={access_token}' \
        .format(access_token=access_token)
    headers = {'user-agent': 'PLCT-Tracker/0.1'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            logger.info('Gitee token test successfully')
            return True
        else:
            logger.error('Gitee token test failed, status code: ' +
                         str(response.status_code))
    except Exception as e:
        logger.error('Gitee token test failed, error: ' + str(e))
    return False


def getUserNamesFromFile(filename: str) -> list:
    """
    Get user names from file
    Return: a list of user names
    """
    userNames = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                userNames.append(line.strip())
    except Exception as e:
        logger.error('Get user names from file failed, error: ' + str(e))
        sys.exit(1)
    return userNames


def main():
    if testGiteeLogin() == False or testGiteeToken() == False:
        sys.exit(1)

    usernames = getUserNamesFromFile('usernames.txt')

    if len(sys.argv) <= 3 and len(usernames) == 0:
        logger.error(
            'Missing args, Usage: main.py StartTime EndTime Usernames, or set the usernames in usernames.txt')
        sys.exit(1)
    elif len(usernames) == 0:
        usernames = sys.argv[3:]

    format = '%Y-%m-%d'
    utc = pytz.UTC
    try:
        startTime = utc.localize(
            datetime.datetime.strptime(sys.argv[1], format))
        endTime = utc.localize(datetime.datetime.strptime(sys.argv[2], format))
    except ValueError:
        logger.error('Invalid date format, should be YYYY-MM-DD')
        sys.exit(1)

    userData = []
    # Get All user data
    for username in usernames:
        user = User(username)
        getUserIDByUsername(user)
        getUserPRList(user, 'src-openeuler',
                      startTime=startTime, endTime=endTime)
        getUserPRList(user, 'openeuler-risc-v',
                      startTime=startTime, endTime=endTime)
        logger.info('Get ' + str(len(user.PRs)) +
                    ' PRs Details for ' + user.userName)
        # Get Each PR Details Per User
        for PR in track(user.PRs, description="Getting PR Details of " + user.userName + ' ...'):
            getPRDetails(PR)
            # sleep(1 + random.randint(1, 3)) # Sleep 1-3 seconds when no token set
            sleep(0.1)
        userData.append(user)

    # Output ascii table
    outputASCIITable(userData)
    # Output csv
    outputCSV(userData)


if __name__ == "__main__":
    main()

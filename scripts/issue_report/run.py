import requests
import json
import csv
import datetime
import time
import pandas as pd
import os


member_file = '../../members.md'
headers = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': 'token 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'
    }
issue_url = 'https://api.github.com/repos/plctlab/openEuler-riscv/issues'


def get_namelist(member_file):
    with open(member_file, encoding='utf-8') as f:
        lines = f.readlines()

    newlines = [line for line in lines if line != '\n']

    def string_process(x):
        y = x.replace(' ','')
        z = y.split('|')
        return z

    newlines = list(map(string_process, newlines))
    # namelist = [{newlines[i][1]:newlines[i][5]} for i in range(3, len(newlines))]
    namedict = {}
    for i in range(3, len(newlines)):
        namedict.update({newlines[i][5]:newlines[i][1]})
    print ('namedict', namedict)
    return namedict
    
def get_issues(headers, issue_url):
    i = 1
    issue_list = []
    while True:
        params = {'page': i, 'direction': 'asc'}
        response = requests.get(issue_url, headers=headers, params=params)
        issues = json.loads(response.text)
        print ('issues length', len(issues))
        if len(issues) > 0:
            issue_list = issue_list + issues
            i = i+1 
        else:
            break
    print ('issue_list length', len(issue_list))
    return issue_list

def get_comments(id, headers):
    comment_url ='https://api.github.com/repos/plctlab/openEuler-riscv/issues/{}/comments'.format(id)
    comment_list = []
    i = 1
    while True:
        params = {'page': i}
        response = requests.get(comment_url, headers=headers, params=params)
        comments = json.loads(response.text)
        # print ('comments length', len(comments))
        if len(comments) > 0:
            comment_list = comment_list + comments
            i = i+1 
        else:
            break
    # print ('comment_list length', len(comment_list))
    return comment_list
    
def get_localtime(utc_time):
    utc_time = datetime.datetime.strptime(utc_time, '%Y-%m-%dT%H:%M:%SZ')
    now_stamp = time.time()
    local_st = datetime.datetime.fromtimestamp(now_stamp)
    utc_st = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_st - utc_st
    local_time = utc_time + offset
    local_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
    # print ('local_time', local_time)
    return local_time

def get_issuetable(issues):
    namedict = get_namelist(member_file)
    issue_data = [[],[],[],[],[],[],[],[]]
    for issue in issues:
        issue_id = issue['number']
        # print('issue id', issue_id)
        title = issue['title']
        labels_list = [label['name'] for label in issue['labels']]
        labels = ','.join(labels_list)
        issue_link = issue['url']
        created_time = get_localtime(issue['created_at'])
        assignees_list = [member['login'] for member in issue['assignees']]
        # print('assignees_list', assignees_list)
        if len(assignees_list) > 0:
            assignees_list = [namedict[assignee] if assignee in namedict.keys() else assignee for assignee in assignees_list]
            # print ('newassignees_list', assignees_list)
        assignees = ','.join(assignees_list)
        if issue['comments'] > 0:
            comments_list = get_comments(issue['number'], headers)
            lastcomment_time = get_localtime(comments_list[-1]['created_at'])
            if comments_list[-1]['user']['login'] in namedict.keys():
                lastcomment_member = namedict[comments_list[-1]['user']['login']]
            else:
                lastcomment_member = comments_list[-1]['user']['login']
        else:
            lastcomment_time = ''
            lastcomment_member = ''
        issue_data[0].append(issue_id)
        issue_data[1].append(title)
        issue_data[2].append(labels)
        issue_data[3].append(issue_link)
        issue_data[4].append(created_time)
        issue_data[5].append(assignees)
        issue_data[6].append(lastcomment_time)
        issue_data[7].append(lastcomment_member)
        table_header = ['ID', 'Title', 'Labels', 'Issue Link', 'Created Time', 'Assignees', 'Time For Last Comment', 'Member For Last Comment']
        issue_table = dict(zip(table_header, issue_data))
        # issue_data = [issue_id, title, labels, issue_link, created_time, assignees, lastcomment_time, lastcomment_member]
        # issue_table.append(issue_data)
    # print ('issue_table length', len(issue_table['ID']))
    # print ('issue_table', issue_table)
    return issue_table
    
def save_csvfile(data):
    filepath = os.path.join(os.getcwd(), 'issues_report.csv')
    dataframe = pd.DataFrame(data)
    dataframe['Title'] = dataframe['Title'].apply(lambda t: (' '*(10-len(str(t)))+str(t)))
    dataframe['Labels'] = dataframe['Labels'].apply(lambda t: (' '*(10-len(str(t)))+str(t)))
    dataframe['Issue Link'] = dataframe['Issue Link'].apply(lambda t: (' '*(15-len(str(t)))+str(t)))
    dataframe['Created Time'] = dataframe['Created Time'].apply(lambda t: (' '*(20-len(str(t)))+str(t)))
    dataframe['Assignees'] = dataframe['Assignees'].apply(lambda t: (' '*(2-len(str(t)))+str(t)))
    dataframe['Time For Last Comment'] = dataframe['Time For Last Comment'].apply(lambda t: (' '*(20-len(str(t)))+str(t)))
    dataframe['Member For Last Comment'] = dataframe['Member For Last Comment'].apply(lambda t: (' '*(2-len(str(t)))+str(t)))
    dataframe.to_csv(filepath, index=False, encoding="utf_8_sig")



if __name__=="__main__":
   issues = get_issues(headers, issue_url)
   table_data = get_issuetable(issues)
   save_csvfile(table_data)

import requests
import os
import constant
import json
from requests.auth import HTTPBasicAuth
import re
import datetime
import csv

def get_obsdata(account,repolist):
    pkgs_url = 'https://build.openeuler.org/source/openEuler:Mainline:RISC-V'
    pkgs_resp = requests.get(pkgs_url,auth=HTTPBasicAuth(account['user'],account['password']))
    pkgs_data = pkgs_resp.text
    pkgslist = re.findall('".*"', pkgs_data)
    del pkgslist[0]
    pkgslist = [x.replace('"','') for x in pkgslist]
    # print (pkgslist)
    # print ('pkgs length', len(pkgslist))
    pkginfo_list = []
    for pkg in pkgslist:
        print ('obs package', pkg)
        service_url = 'https://build.openeuler.org/source/openEuler:Mainline:RISC-V/{}/_service'.format(pkg)
        service_resp = requests.get(service_url,auth=HTTPBasicAuth(account['user'],account['password']))
        service_data = service_resp.text
        # print ('service_data', service_data)
        git_pattern = '<param name="url">.*</param>'
        revision_pattern = '<param name="revision">.*</param>'
        try:
            gitinfo = re.search(git_pattern, service_data).group()
            revision = re.search(revision_pattern, service_data).group()
            # print (gitinfo)
            # print (revision)
            gitinfo = re.search('>.*<', gitinfo).group()[1:-1]
            revision = re.search('>.*<', revision).group()[1:-1]
            if len(revision) == 0:
                revision = 'None'
            # print ('git', gitinfo)
            # print ('revision', revision)
        except:
            gitinfo = 'None'
            revision = 'None'
            print ('Cannot get url and revision!')
        statuslist = []
        rpmlist = []
        for repo in repolist:
            status_url = 'https://build.openeuler.org/build/openEuler:Mainline:RISC-V/{}/riscv64/{}/_status'.format(repo,pkg)
            status_resp = requests.get(status_url,auth=HTTPBasicAuth(account['user'],account['password']))
            status_data = status_resp.text
            # print ('status_data', status_data)
            status = re.search('code=".*"', status_data).group()
            status = status.split('"')[1]
            # print ('status', status)
            statuslist.append(status)
            rpm_url = 'https://build.openeuler.org/build/openEuler:Mainline:RISC-V/{}/riscv64/{}'.format(repo,pkg)
            rpm_resp = requests.get(rpm_url,auth=HTTPBasicAuth(account['user'],account['password']))
            rpm_data = rpm_resp.text
            # print ('rpm_data', rpm_data)
            rpm_pattern = 'filename=.*.src.rpm'
            try:
                rpm_ver = re.search(rpm_pattern, rpm_data).group()[10:]
                # print ('rpm_ver', rpm_ver)
                rpm_history = 'Yes'
            except:
                rpm_history = 'No'
                rpm_ver = 'None'
                # print ('rpm_ver', rpm_ver)
            rpmlist.extend([rpm_history, rpm_ver])
        pkgdict = dict(package=pkg,git=gitinfo,revision=revision,status=statuslist,rpm=rpmlist)
        # print ('pkgdict', pkgdict)
        pkginfo_list.append(pkgdict)
        print ('pkginfo_list length', len(pkginfo_list))
    return pkginfo_list

def get_giteedata(pkgsinfo,branchlist,headers,token,org):
    pkgsver_list = []
    for pkg in pkgsinfo:
        print ('gitee package', pkg)
        gitee_verlist = []
        lastest_datelist = []
        for branch in branchlist:
            branch_url = 'https://gitee.com/api/v5/repos/{}/{}/branches/{}'.format(org,pkg['package'],branch)
            params = {
                'access_token': token,
            }
            # print ('branch_url', branch_url)
            branch_resp = requests.get(branch_url, headers=headers, params=params)
            data = json.loads(branch_resp.text)
            # print ('data', data)
            try:
                commitid = data['commit']['url'].split('/')[-1]
                # print ('commitid',commitid)
                commitdate = data['commit']['commit']['author']['date']
                # print ('commitdate1', commitdate)
                commitdate = datetime.datetime.fromisoformat(commitdate).timestamp()
                # print ('commitdate2', commitdate)
            except:
                commitid = 'None'
                commitdate = 0
                print ('Branch {} does not exist'.format(branch))
            # print ('branch', branch)
            gitee_verlist.append(commitid)
            lastest_datelist.append(commitdate)
            # print ('gitee_verlist', gitee_verlist)
            # print ('lastest_datelist', lastest_datelist)
        if gitee_verlist == ['None', 'None', 'None']:
            lastest_date = 'None'
            update_priority = 'None'
        else:
            if pkg['revision'] != 'None': 
                commit_url = 'https://gitee.com/api/v5/repos/{}/{}/commits/{}'.format(org,pkg['package'],pkg['revision'])
                # print ('commit_url', commit_url)
                commit_resp = requests.get(commit_url, headers=headers, params=params)
                commit_data = json.loads(commit_resp.text)
                # print ('commit_data', commit_data)
                try:
                    obscommit_date = commit_data['commit']['author']['date']
                    # print ('obscommit_date1', obscommit_date)
                    obscommit_date = datetime.datetime.fromisoformat(obscommit_date).timestamp()
                    # print ('obscommit_date2', obscommit_date)
                except:
                    obscommit_date = 0
            else:
                obscommit_date = 0
            compare_verlist = gitee_verlist
            compare_verlist = compare_verlist + [pkg['revision']]
            # print ('gitee_verlist', gitee_verlist)
            lastest_datelist.insert(0,obscommit_date)
            # print ('lastest_datelist', lastest_datelist)
            lastest_date = lastest_datelist.index(max(lastest_datelist))
            # print ('lastest_date', lastest_date)
            compare_verlist = [x for x in compare_verlist if x != 'None']
            update_priority = len(list(set(compare_verlist)))
            # print ('update_priority', update_priority)
        pkglist = [pkgsinfo.index(pkg)+1,pkg['package'],pkg['git'],pkg['revision']]
        pkglist.extend(pkg['status'])
        pkglist.extend(gitee_verlist)
        pkglist.extend([lastest_date, update_priority])
        pkglist.extend(pkg['rpm'])
        # print ('pkglist', pkglist)
        pkgsver_list.append(pkglist)
        # print ('pkgsver_list', pkgsver_list)
        print ('pkgsver_list length', len(pkgsver_list))  
    return pkgsver_list

def create_csvfile(pkgsver,report_header,csvfile):
    with open(csvfile, 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(report_header) 
        csv_writer.writerows(pkgsver)


if __name__=="__main__":
    obs_account = constant.obs_account
    repolist = constant.repolist
    pkgsinfo = get_obsdata(obs_account,repolist)
    headers = constant.headers
    token = constant.token
    org = constant.org
    branchlist = constant.branchlist
    pkgsver = get_giteedata(pkgsinfo,branchlist,headers,token,org)
    report_header = constant.report_header
    csvfile = constant.csvfile
    create_csvfile(pkgsver,report_header,csvfile)
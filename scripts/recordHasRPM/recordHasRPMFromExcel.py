import recordHasRPM
import openpyxl
import configparser

if __name__ == '__main__':
    config=configparser.RawConfigParser()
    config.read('config.ini',encoding='utf-8-sig')
    project=config.get('default','project')
    print(project)
    repo=config.get('default','repo')
    print(repo)
    filename=config.get('default','filename')
    sheetname=config.get('default','sheetname')
    beginrow=int(config.get('default','beginrow'))

    wb_src=openpyxl.load_workbook(filename)
    ws_src=wb_src.get_sheet_by_name(sheetname)

    recordHasRPM.my_cookie=config.get('default','cookie')

    recordHasRPM.recordHasRPM(ws_src,beginrow,project,repo)

    wb_src.save(filename)
import os

pkg_filepath = os.path.join(os.getcwd(), 'java_pkgs.txt')
tag = 'f29'
pkginfo_filepath = os.path.join(os.getcwd(), 'pkgs_info.json')
rpminfo_filepath = os.path.join(os.getcwd(), 'rpm_info.json')
excelfile = os.path.join(os.getcwd(), 'pkgs_rpm_result.xlsx')
report_header = ['Package', 'RPM Name', 'Get Result']
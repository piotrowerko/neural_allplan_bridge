
import os
import shutil
import fnmatch
import subprocess

exe = "C:/Program Files/Allplan/Allplan 2021/Prg/AllplanBridge_2022.exe"
wdir="C:/ppp"
#file_path = 'C:\ppp\_Reports\Construction 1\Dynamics\EIGEN.xlsx'


#start loop
starting_angle = 0
step = 15
for i in range(starting_angle, 30, step):
    file_name = f'angle_{i}.tcl'
    #fname="angle_0.tcl"

    args = []
    args.append('-batch')
    args.append('-norecent')
    args.append('-nostartup')
    args.append('-regression')

    args.append('-tclimport:'+file_name)

    print('run')
    try:
        cmdline = [exe]+args
        proc = subprocess.Popen(cmdline, cwd=wdir)
        proc.wait()
    except:
        pass
    original = r'C:\ppp\_Reports\Construction 1\Dynamics'
    target = r'C:\Python\git_projects\neural_allplan_bridge'
    file_name = 'EIGEN.xlsx'
    file_name2 = f'EIGEN{i}.xlsx'
    full_file_name = os.path.join(original, file_name)
    new_full_file_name = os.path.join(target, file_name2)
    shutil.copy(full_file_name, new_full_file_name)

# i = 15
# file_name = f'angle_{i}.tcl'
# fname="angle_0.tcl"

# args = []
# args.append('-batch')
# args.append('-norecent')
# args.append('-nostartup')
# args.append('-regression')

# args.append('-tclimport:'+fname)

# print('run')
# try:
#     cmdline = [exe]+args
#     proc = subprocess.Popen(cmdline, cwd=wdir)
#     proc.wait()
# except:
#     pass
# original = r'C:\ppp\_Reports\Construction 1\Dynamics'
# target = r'C:\Python\git_projects\neural_allplan_bridge'
# file_name = 'EIGEN.xlsx'
# file_name2 = f'EIGEN{i}.xlsx'
# full_file_name = os.path.join(original, file_name)
# new_full_file_name = os.path.join(target, file_name2)
# shutil.copy(full_file_name, new_full_file_name)

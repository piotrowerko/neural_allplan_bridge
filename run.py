
import subprocess

exe = "C:/Program Files/Allplan/Allplan 2021/Prg/AllplanBridge_2022.exe"
wdir="C:/ppp"

#start loop
fname="angle_0.tcl"

args = []
args.append('-batch')
args.append('-norecent')
args.append('-nostartup')
args.append('-regression')

args.append('-tclimport:'+fname)

print('run')
try:
    cmdline = [exe]+args
    proc = subprocess.Popen(cmdline, cwd=wdir)
    proc.wait()

except:
    pass
#end loop 
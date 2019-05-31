import os
import glob

def sbstr(str, c1, c2):
    return str[str.find(c1)+1 : str.find(c2)]
    

while True:
    cmd = input()
    if cmd.startswith('create_dir'):
        address = sbstr(cmd, '(', ',').strip()
        name = sbstr(cmd, ',', ')').strip()
        os.mkdir(address+"/"+name)
    if cmd.startswith('create_file'):
        address = sbstr(cmd, '(', ',').strip()
        name = sbstr(cmd, ',', ')').strip()
        f = open(address+'/'+name,"w+")
        f.close()
    if cmd.startswith('delete'):
        address = sbstr(cmd, '(', ',').strip()
        name = sbstr(cmd, ',', ')').strip()
        os.remove(address+"/"+name)
    if cmd.startswith('find'):
        address = sbstr(cmd, '(', ',').strip()
        name = sbstr(cmd, ',', ')').strip()
        for f in glob.glob(address+'/**/'+name, recursive=True):
            print(f)

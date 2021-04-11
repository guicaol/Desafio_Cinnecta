import pandas as pd
from pathlib import Path
from os import listdir
from os.path import isfile, join
import win32api
import win32con
import win32security
    

class PathSerch():
    
    def __init__(self, path):
        self.path = path
    def __str__(self):
        return '<%s, %s>' % (self.path)
        
    def list_file_and_owner(self):
        try:    
            list_files = []
            list_owners = []
            files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
            for files in files:
                pathfile=(self.path+"/"+files)
                sd = win32security.GetFileSecurity (pathfile, win32security.OWNER_SECURITY_INFORMATION)
                owner_sid = sd.GetSecurityDescriptorOwner ()
                name, domain, type = win32security.LookupAccountSid (None, owner_sid)
                owner = domain + '/' + name
                list_files.append(pathfile)
                list_owners.append(owner)
            return list_owners, list_files
        except:
            return('Caminho nao identificado')
    def dictionary_list_owner(self):
        dic ={}
        list_owners, list_files = self.list_file_and_owner()
        
        df = pd.DataFrame({"owner":list_owners,
                            "file":list_files})
        for owner in list_owners:
            listadicionario = df[df["owner"] == owner]["file"].tolist()  
            dic.update({owner: listadicionario })
        return dic

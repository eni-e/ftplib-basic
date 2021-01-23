import ftplib

def get_list_ftp_subdir(ftp, cwd, files = []):
    data = []
    ftp.cwd(cwd)
    ftp.dir(data.append)
    for item in data:
        pos = item.rfind(' ')
        name = cwd + item[pos+1:]
        #WINDOW - <DIR> , LINUX - drw
        if item.find('<DIR>') > -1:
            data2 = []
            ftp.cwd(cwd + item[pos+1:])
            ftp.dir(data2.append)
            for item2 in data2:
                pos2 = item.rfind(' ')
                name2 = cwd + item[pos+1:] + "/" + item2[pos2+1:]
                files.append(name2)
        else:
            files.append(name)
    return files
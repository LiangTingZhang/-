import hashlib
from imp import reload
import os
from collections import Counter
import sys

reload(sys)


def get_md5_01(file_path):
    md5 = None
    if os.path.isfile(file_path):
        f = open(file_path,'rb')
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
    return md5

def get_md5_02(file_path):
    f = open(file_path,'rb')
    md5_obj = hashlib.md5()
    while True:
        d = f.read(8096)
        if not d:
            break   
        md5_obj.update(d)
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
    return md5

if __name__ == "__main__":
    output_list=[]
    #input_path=r"e:\xx\新建文件夹"
    #output_path = unicode(input_path , “utf8”)
    output_path=os.getcwd()
    g = os.walk(output_path)
    for path,dir_list,file_list in g:
        for file_name in file_list:
            output_list.append(os.path.join(path, file_name) )
    md5_list= [get_md5_01(i) for i in output_list]
    Counter_list=Counter(md5_list)
    for i in Counter_list.items():
        if i[1] >1:
            duplicate_list=[ a for a in range(len(md5_list)) if md5_list[a] == i[0]]
            print ('-'*50)
            print (i[0])
            for j in duplicate_list:
                with open('duplicate.log', mode='a+') as f:
                    f.write(i[0]+'\t'+output_list[j]+'\n')
                print (output_list[j])
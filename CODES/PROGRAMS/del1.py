import hashlib
import os

def md5(f):
    """takes one file f as an argument and generates an md5checksum for that file"""
    return hashlib.md5(open(f,'rb').read()).hexdigest()

def rm_dup(path):
    """relies on the md5 function above to remove duplicate files"""
    if not os.path.isdir(path):
        print('specified directory does not exist!')
    else:
        md5_dict={}
        for root, dirs, files in os.walk(path):
            for f in files:
                if not md5(os.path.join(root,f)) in md5_dict:
                    md5_dict.update({md5(os.path.join(root,f)):[os.path.join(root,f)]})
                else:
                    md5_dict[md5(os.path.join(root,f))].append(os.path.join(root,f))
        for key in md5_dict:
            while len(md5_dict[key])>1:
                for item in md5_dict[key]:
                    os.remove(item)
                    md5_dict[key].remove(item)
        print('Done!')


if __name__=='__main__':     
    #path=input(r'Please provide the target path\directory... for example: c: or c:\directory...')
    path=os.getcwd()
    print()
    rm_dup(path)

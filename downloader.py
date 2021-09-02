import requests, sys, os, errno
verbose=True

def downld(self,dlclass,dldir):
        # if verbose: print(dlclass.br)
        fpath=os.path.join(dldir,str(dlclass.filename))
        if verbose: print(fpath)
        headers={}
        loop=1
        if verbose: print("thread initiated")
        if os.path.exists(fpath):
            if verbose: print("existing instance")
            otf = open(fpath,"ab")
            existSize = os.path.getsize(fpath)
            sizeper=(int(existSize)/int(dlclass.flen))*100
            if verbose: print(sizeper)
            # self.updateBar(dlclass,(int(existSize)/int(dlclass.flen))*100) '''signal slot needed'''
            # dlclass.progressBar.setValue((int(existSize)/int(dlclass.flen))*100)
            if verbose: print(existSize)
            if int(existSize) == int(dlclass.flen):
                loop = 0
                if verbose: print("Already Downloaded")
            else:
                headers = {'Range': 'bytes=%d-' % (existSize)}
                dlclass.dlen=int(existSize)
                if verbose: print("Appending")

        # headers = {'Range': 'bytes=%d-%d' % (0, 4197044)}
        else:
            otf = open(fpath,"wb")
            if verbose: print("New Download")
        if loop:
            try:
                r = requests.get(dlclass.link, headers=headers, stream = True)
                if verbose: print("request made")
                # r = requests.get(dlclass.link, stream = True)
            except:
                print("Oops!", sys.exc_info()[0], f"Cant download {dlclass.filename}")
                otf.close()
                return
            else:
                a=0
                if verbose: print(fpath)
                # with open(str(dlclass.filename),"ab") as otf:
                for chunk in r.iter_content(chunk_size=dlclass.csize):
                    # global BREAK
                    if self.br:
                        if verbose: print("break")
                        break
                    if chunk:
                        otf.write(chunk)
                        dlclass.dlen+=dlclass.csize
                        if verbose: print((dlclass.dlen/int(dlclass.flen))*100)
                        if round((dlclass.dlen/int(dlclass.flen)*100),1)>a:
                            a=round((dlclass.dlen/int(dlclass.flen)*100),1)
                            # dlclass.progressBar.setValue(a)
                            # self.updateBar(dlclass, a)
                            if a>100:
                                a=100
                            dlclass.updatesize(a)

        # self.br=False
        otf.close()
        self.nthr-=1
        dlclass.nlabel.deleteLater()
        dlclass.plabel.deleteLater()
        self.done+=1
        if verbose: print(self.total)
        # print(self.total)
        self.ui.label_7.setText(f"{self.done}/{self.total}")
        self.gui_connection.signal_val.emit(int((self.done/self.total)*100))
        # self.ui.progressBar.setValue(int((self.done/self.total)*100))
        if verbose: print(f"download thread for {dlclass.filename} has been terminated")

ERROR_INVALID_NAME = 123

def is_pathname_valid(pathname: str) -> bool:
    
    try:
        if not isinstance(pathname, str) or not pathname:
            return False

        _, pathname = os.path.splitdrive(pathname)

        root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
            if sys.platform == 'win32' else os.path.sep
        assert os.path.isdir(root_dirname) 
        root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

        for pathname_part in pathname.split(os.path.sep):
            try:
                os.lstat(root_dirname + pathname_part)
            except OSError as exc:
                if hasattr(exc, 'winerror'):
                    if exc.winerror == ERROR_INVALID_NAME:
                        return False
                elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                    return False
    except TypeError as exc:
        return False
    else:
        return True

def is_path_creatable(pathname: str) -> bool:
    dirname = os.path.dirname(pathname) or os.getcwd()
    return os.access(dirname, os.W_OK)

def is_path_exists_or_creatable(pathname: str) -> bool:
    try:
        return is_pathname_valid(pathname) and (
            os.path.exists(pathname) or is_path_creatable(pathname))
    except OSError:
        return False
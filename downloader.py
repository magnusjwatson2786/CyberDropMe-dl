from dlic import Dlitem
import requests, sys, os

verbose=False

def downld(self,dlclass:Dlitem,dldir:str)->None:
        # if verbose: print(dlclass.br)
        fpath=os.path.join(dldir,str(dlclass.filename))
        if verbose: print(fpath)

        if dlclass.flen in range(0,(1024*1024)+1):
            dlclass.csize=100*1024
        elif dlclass.flen in range((1024*1024)+1,(10*1024*1024)+1):
            dlclass.csize=512*1024
        elif dlclass.flen in range((10*1024*1024)+1,(512*1024*1024)+1):
            dlclass.csize=1024*1024
        else:
            dlclass.csize=5*1024*1024
        if verbose: print(dlclass.csize)

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
                os.remove(fpath)
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
                self.fails.append(dlclass.filename)
                del dlclass
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
        del dlclass
        return


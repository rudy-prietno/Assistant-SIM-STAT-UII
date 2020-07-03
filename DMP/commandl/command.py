import subprocess

class commandline:
    def __init__(self, statement):
        self.statement = statement

    def execute(self):
        s = subprocess.getstatusoutput(self.statement)
        print(s[1])
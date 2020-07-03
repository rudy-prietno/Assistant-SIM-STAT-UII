import subprocess
import docker

class commandline:
    def __init__(self, statement):
        self.statement = statement

    def execute(self):
        s = subprocess.getstatusoutput(self.statement)
        print(s[1])

class commandexec:
    def __init__(self, statement, num):
        self.statement = statement
        self.num = num

    def exec_container(self):
        # Reference the command into docker container
        client = docker.from_env()
        p2=client.containers.list()
        display(p2[self.num].exec_run(self.statement, stdout=True, stderr=True))


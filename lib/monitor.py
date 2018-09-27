import utilities
from time import sleep

class monitor(object):

    def __init__(self):
        self.u = utilities.utilities()
        f = open('files.txt', 'r')
        self.files = f.readlines()
        for f in self.files:
            self.u.copy_file(f.strip())

    def file_monitor(self):
        while True:
            for f in self.files:
                self.u.compare_files(f.strip())
            sleep(5)
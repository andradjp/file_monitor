import os
from shutil import rmtree
from lib import monitor


if __name__ == "__main__":

    if os.path.isdir('files'):
        rmtree('files')
    os.mkdir('files')
m = monitor.monitor()
m.file_monitor()
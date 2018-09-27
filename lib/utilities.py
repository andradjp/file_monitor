# coding=utf-8

import filecmp, difflib, config
from shutil import copyfile, rmtree
from os import mkdir, system, remove, uname
from json import dumps

class utilities(object):

    def __init__(self):
        rmtree('files')
        mkdir('files')

    def compare_files(self, file):

        if not filecmp.cmp(file, 'files/'+file.split('/')[-1]):
            alteracoes = ''
            f1 = open(file, 'r').readlines()
            f2 = open('files/'+file.split('/')[-1], 'r').readlines()
            for i, f in enumerate(f1):
                f1[i] = f.strip()
            for i, f in enumerate(f2):
                f2[i] = f.strip()
            result = difflib.unified_diff(f2, f1, n=0)
            for x in result:
                alteracoes += x + '\n'
            msg1 = '{"grupo":"nucom","mensagem":"*Alerta de alteração de Zona*\n\n' \
                   '*Servidor: *' + uname()[1] + '\n\n*Arquivo alterado:*\n' + file +'\n\n' \
                                                            '*--Alterações--*\n '+ alteracoes + '\n\n"}'
            system('curl -H "Content-Type: application/json" -d {} {}'.format(dumps(msg1), config.telegram_server))
            remove('files/'+file.split('/')[-1])
            copyfile(file, 'files/' + file.split('/')[-1])

    def copy_file(self, file):
        copyfile(file, 'files/'+file.split('/')[-1])

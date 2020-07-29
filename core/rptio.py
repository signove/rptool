#!/usr/bin/env python3


# -*- coding: utf-8 -*-
import os
from datetime import datetime


class FileManager:

    def __init__(self):
        self.tag = 'FileManager'

    def getCurrentFolder(self):
        return os.getcwd()

    def write(self, file, data):
        # self.debug('writing {0} - {1}'.format(file, data))
        try:
            outputFile = open(file, 'a')
            outputFile.write(data)
            outputFile.close()
        except:
            self.debug('error writing file {0}'.format(file))

    def read(self, file):
        self.debug('reading {0}'.format(file))
        try:
            with open(file) as content:
                lines = []
                for line in content:
                    line = line.replace('\n', '')
                    lines.append(line)
                return lines
        except FileNotFoundError as err:
            self.debug('error {0}'.format(err))

    def delete(self, filename):
        try:
            self.debug('deleting file {}'.format(filename))
            os.remove(filename)
        except:
            self.debug('err removing file'.format(filename))

    def list(self, folder):
        files = []
        for r, d, f in os.walk(folder):
            for file in f:
                if '.png' not in file:
                    files.append(file)
        return files

    def debug(self, message):
        now = datetime.now()
        log = '[{0}] {1} - {2}'.format(now.strftime("%d/%m/%Y %H:%M:%S"), self.tag, message)
        print(log)
#!/usr/bin/env python3


# -*- coding: utf-8 -*-
import os
from datetime import datetime
from src.core.rptio import FileManager


class Logger:

    def __init__(self, tag):
        self.tag = tag
        self.writter = FileManager()
        self.folder = '{0}/logs'.format(os.getcwd())
        self.logfile = '{0}/{1}.log'.format(self.folder, tag.lower())
        self.makeLogDir()
        self.debug('started logger for {0}'.format(tag))

    def makeLogDir(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def debug(self, message):
        now = datetime.now()
        log = '[{0}] {1} - {2}'.format(now.strftime("%d/%m/%Y %H:%M:%S"), self.tag, message)
        print(log)
        self.writter.write(self.logfile, '{0}\n'.format(log))

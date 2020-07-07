# -*- coding: utf-8 -*-
from core.rptio import FileManager
from core.logger import Logger

class RPTool:

    def __init__(self):
        self.log = Logger('RPTool')
        self.fileManager = FileManager()

    def getTestFolder(self):
        return '{}/tests'.format(self.fileManager.getCurrentFolder())

    def getTestFiles(self):
        return self.fileManager.list(self.getTestFolder())

    def rec(self, testname):
        self.log.debug('recording \'{0}\'...'.format(testname))
        self.saveTestFile(testname, '')

    def delete(self, testname):
        self.log.debug('deleting \'{0}\'...'.format(testname))
        self.fileManager.delete('{0}/{1}'.format(self.getTestFolder(), testname))

    def playback(self, testname):
        self.log.debug('playback \'{0}\'...'.format(testname))

    def saveTestFile(self, testname, data):
        filename = '{0}/{1}'.format(self.getTestFolder(), testname)
        self.fileManager.write(filename, data)
        self.log.debug('saving test file {0}'.format(filename))
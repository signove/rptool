# -*- coding: utf-8 -*-
from core.rptio import FileManager
from core.logger import Logger
from core.recorder import Recorder
from core.playback import PlayBack


class RPTool:

    def __init__(self):
        self.playback = None
        self.recorder = None
        self.log = Logger('RPTool')
        self.fileManager = FileManager()
        self.file = ''

    def getTestFolder(self):
        return '{}/tests'.format(self.fileManager.getCurrentFolder())

    def getTestFiles(self):
        return self.fileManager.list(self.getTestFolder())

    def rec(self, test_name):
        self.recorder = Recorder(self.fileManager)
        self.log.debug('recording \'{0}\'...'.format(test_name))
        self.saveTestFile(test_name)
        self.recorder.start(self.file)

    def delete(self, test_name):
        self.log.debug('deleting \'{0}\'...'.format(test_name))
        self.fileManager.delete(self.getFullFileName(test_name))

    def play(self, test_name):
        self.playback = PlayBack(self.fileManager)
        self.log.debug('playback \'{0}\'...'.format(test_name))
        self.playback.play(self.getFullFileName(test_name))

    def saveTestFile(self, test_name):
        self.file = self.getFullFileName(test_name)
        self.fileManager.write(self.file, '')
        self.log.debug('saving test file {0}'.format(self.file))

    def getFullFileName(self, test_name):
        return '{0}/{1}'.format(self.getTestFolder(), test_name)
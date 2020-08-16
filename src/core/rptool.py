#!/usr/bin/env python3


# -*- coding: utf-8 -*-
from src.core.rptio import FileManager
from src.core.logger import Logger
from src.core.recorder import Recorder
from src.core.playback import PlayBack
from src.core.alert import Alert
from src.core.testlinkapi import TestlinkAPI
from src.core.settings import Settings


class RPTool:

    def __init__(self):
        self.playback = None
        self.recorder = None
        self.log = Logger('RPTool')
        self.fileManager = FileManager()
        self.file = ''
        self.alert = Alert('RPTool')
        self.api = TestlinkAPI()
        self.setting = Settings('testlink.cfg')

    def getTestFolder(self):
        return '{}/tests'.format(self.fileManager.getCurrentFolder())

    def getTestFiles(self):
        return self.fileManager.list(self.getTestFolder())

    def rec(self, test_name):
        self.alert.notify('Recording {} ...'.format(test_name))
        self.recorder = Recorder(self.fileManager)
        self.log.debug('recording \'{0}\'...'.format(test_name))
        self.saveTestFile(test_name)
        self.recorder.start(self.file)

    def delete(self, test_name):
        self.log.debug('deleting \'{0}\'...'.format(test_name))
        self.fileManager.delete(self.getFullFileName(test_name))
        self.alert.notify('Deleting {} ...'.format(test_name))

    def play(self, test_name):
        self.alert.notify('Playback {0}'.format(test_name))
        self.playback = PlayBack(self.fileManager)
        self.log.debug('playback \'{0}\'...'.format(test_name))
        self.playback.play(self.getFullFileName(test_name))

    def saveTestFile(self, test_name):
        self.file = self.getFullFileName(test_name)
        self.fileManager.write(self.file, '')
        self.log.debug('saving test file {0}'.format(self.file))

    def getFullFileName(self, test_name):
        return '{0}/{1}'.format(self.getTestFolder(), test_name)

    def notifyLoop(self, time):
        self.alert.notify('Loop enabled to repeat in {} s'.format(time))

    def getUsername(self):
        return self.api.getUsername()

    def getApiKey(self):
        return self.api.getApiKey()

    def getUrl(self):
        return self.api.getUrl()

    def getProjects(self):
        return self.api.getProjects()

    def getPlans(self, project_id):
        return self.api.getPlans(project_id)

    def getPlatforms(self, project_id):
        platforms = []
        map = self.api.getPlatforms(project_id)
        for key in map:
            platforms.append(map[key])
        return platforms

    def getBuilds(self, plan_id):
        return self.api.getBuilds(plan_id)

    def saveConfig(self, config):
        print('saving config', config)
        self.setting.saveConfig(config)

    def getConfig(self):
        cfg = self.setting.readConfig()
        if cfg is None:
            return {}
        else:
            return cfg

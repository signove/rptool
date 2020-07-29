import subprocess
import pyautogui

from core.alert import Alert
from core.settings import Settings
from core.testlinkapi import TestlinkAPI

class Verifier:

    def __init__(self):
        self.checkPointIndex = 0
        self.alert = Alert('Verifier')
        self.setting = Settings('testlink.cfg')
        self.config = self.setting.readConfig()
        self.api = TestlinkAPI()

    def printScreen(self, filename):
        print('check {0}'.format(filename))
        filename = '{0}_{1}.png'.format(filename, self.checkPointIndex)
        print('Saved as {}'.format(filename))
        subprocess.run(['scrot', '-s', filename])
        self.checkPointIndex += 1
        return filename

    def check(self, checkpoint):
        checked = pyautogui.locateOnScreen(checkpoint)
        if checked:
            self.alert.notify('checked Ok')
            self.report(checkpoint, 'p')
        else:
            self.alert.notify('checked Fail')
            self.report(checkpoint, 'f')

    #
    # A test should be in the following format:
    # 'PREFIX-ID_NAME' , Where PREFIX is the project prefix.
    # ID is the external id
    #
    def report(self, checkpoint, status):
        identifier = checkpoint.split('/')[-1]
        test = identifier.split('_')[0]
        plan = self.config['plan_id']
        build = self.config['build_name']
        notes = '...'
        user = self.config['username']
        platform = self.config['platform_id']
        self.api.reportTCResult(None, plan, build, status, notes, user, platform, test)
        print('reporting ... ', checkpoint)


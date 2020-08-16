import subprocess
import pyautogui

from src.core.alert import Alert
from src.core.settings import Settings
from src.core.testlinkapi import TestlinkAPI


class Verifier:

    def __init__(self):
        self.checkPointIndex = 0
        self.alert = Alert('Verifier')
        self.setting = Settings('testlink.cfg')
        self.config = self.setting.readConfig()
        self.api = TestlinkAPI()

    def printScreen(self, filename):
        """ F2 key pressed should to capture the selected area on screen """
        print('check {0}'.format(filename))
        filename = '{0}_{1}.png'.format(filename, self.checkPointIndex)
        print('Saved as {}'.format(filename))
        subprocess.run(['scrot', '-s', filename])
        self.checkPointIndex += 1
        return filename

    def check(self, checkpoint):
        """ Check if the checkpoint image in visible on screen """
        checked = pyautogui.locateOnScreen(checkpoint)
        if checked:
            self.alert.notify('checked Ok')
            self.report(checkpoint, 'p')
        else:
            self.alert.notify('checked Fail')
            self.report(checkpoint, 'f')


    def report(self, checkpoint, status):
        """ Sends the test result to Testlink """
        identifier = checkpoint.split('/')[-1]
        test = identifier.split('_')[0]
        plan = self.config['plan_id']
        build = self.config['build_name']
        notes = '...'
        user = self.config['username']
        platform = self.config['platform_id']
        self.api.reportTCResult(None, plan, build, status, notes, user, platform, test)
        print('reporting ... ', test)


import sys
import subprocess
import os

class Verifier:

    def __init__(self):
        print('init verifier')
        self.checkPointIndex = 0

    def printScreen(self, filename):
        print('check {0}'.format(filename))
        filename = '{0}_{1}.png'.format(filename, self.checkPointIndex)
        print('Saved as {}'.format(filename))
        subprocess.run(['scrot', '-s', filename])
        self.checkPointIndex += 1
        return filename

    def report(self):
        print('reporting to testlink')

# -*- coding: utf-8 -*-
import pyautogui
from pynput.keyboard import Key
from pynput.keyboard import Listener as KeyboardListener
from core.logger import Logger

class Trace:

    def __init__(self, raw):
        self.type = ''
        self.x = 0
        self.y = 0
        self.key = 0
        self.time = 0
        self.parse(raw)

    def parse(self, raw):
        raw = raw.replace('\n', '').replace(',', '')
        trace_parts = raw.split(' ')
        self.type = trace_parts[0]
        if self.type == 'click':
            self.parseClick(trace_parts)
        elif self.type == 'press':
            self.parsePress(trace_parts)
        else:
            pass

    def parsePress(self, trace_parts):
        self.key = trace_parts[1].split('=')[1].replace('\'', '')

        if '.' in self.key:
            self.key = self.key.split('.')[1]

        if self.key in ['shift_r', 'shift_l']:
            self.key = 'shift'

        print('parsed key', self.key)

    def parseClick(self, trace_parts):
        self.x = int(trace_parts[1].split('=')[1])
        self.y = int(trace_parts[2].split('=')[1])
        self.time = float(trace_parts[3].split('=')[1])

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getTime(self):
        return self.time

    def getType(self):
        return self.type

    def getKey(self):
        return self.key

    def isHotKey(self):
        return self.key in ['ctrl', 'alt', 'del', 'tab', 'shift']


class PlayBack:

    def __init__(self, file_manager):
        self.fileManager = file_manager
        self.log = Logger('PlayBack')
        self.traces = []
        self.hostKeys = []
        self.keyboardListener = KeyboardListener(on_press=self.onPress, on_release=self.onRelease)
        self.stopped = False
        self.running = False

    def onPress(self, *args):
        pass

    def onRelease(self, *args):
        # Stop recording when  press 'esc'
        if args[0] == Key.esc:
            self.keyboardListener.stop()
            self.stopped = True
            self.running = False
            return False
        print('release')

    def traceBack(self):
        for trace in self.traces:
            if not self.stopped:
                if trace.getType() == 'click':
                    self.click(trace)
                if trace.getType() == 'press':
                    self.press(trace)
                else:
                    pass
            else:
                print('Stopped playback')
                return

    def press(self, trace):
        if trace.isHotKey():
            self.hostKeys.append(trace.getKey())
        else:
            if len(self.hostKeys) > 0:
                self.hostKeys.append(trace.getKey())
                print(self.hostKeys)
                if len(self.hostKeys) == 2:
                    pyautogui.hotkey(self.hostKeys[0], self.hostKeys[1])
                if len(self.hostKeys) == 3:
                    pyautogui.hotkey(self.hostKeys[0], self.hostKeys[1], self.hostKeys[2])
                self.hostKeys = []
            else:
                pyautogui.typewrite(trace.getKey(), 0.1)

    def click(self, trace):
        pyautogui.moveTo(trace.getX(), trace.getY(), trace.getTime())
        pyautogui.click()

    def play(self, file):
        # Avoid start twice the same thread
        if not self.running:
            self.running = True
            self.keyboardListener.start()
        self.traceReader(file)
        self.traceBack()

    def traceReader(self, file):
        try:
            with open(file) as traces:
                for rawTrace in traces:
                    trace = Trace(rawTrace)
                    self.traces.append(trace)
        except FileNotFoundError as err:
            self.log.debug('Error {}'.format(err))

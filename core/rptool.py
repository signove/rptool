# -*- coding: utf-8 -*-
import time
import pyautogui
from core.rptio import FileManager
from core.logger import Logger
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener


class Clock:

    def __init__(self):
        self.time = time.time()
        self._start = 0
        self._end = 0
        self._elapsed = 0

    def start(self):
        if self._start == 0:
            self._start = time.time()
        else:
            self.stop()

    def stop(self):
        self._end = time.time()
        self._elapsed = (self._end - self._start)
        self._start = self._end

    def getTime(self):
        return round(self._elapsed, 2)


class Recorder:

    def __init__(self, file_manager):
        self.file = ''
        self.fileManager = file_manager
        self.log = Logger('Recorder')
        self.mouseListener = MouseListener(on_click=self.onClick, on_scroll=self.onScroll, on_move=self.onMove)
        self.keyboardListener = KeyboardListener(on_press=self.onPress, on_release=self.onRelease)
        self.clock = Clock()

    def save(self, trace):
        self.fileManager.write(self.file, trace)

    def onClick(self, *args):
        self.clock.start()
        pressed = args[3]
        if pressed:
            trace = 'click x={}, y={}, time={}\n'.format(args[0], args[1], self.clock.getTime())
            self.save(trace)
        else:
            pass

    def onScroll(self, *args):
        pass
        #  x, y, dx, dy
        # self.save('scroll {}\n'.format(args))

    def onMove(self, *args):
        pass
        # x, y
        # self.save('move {}\n'.format(args))

    def onPress(self, *args):
        # key
        print(args)
        self.save('press key={}\n'.format(args[0]))

    def onRelease(self, *args):
        pass
        # key
        # self.save('release key={}\n'.format(args[0].char))

    def start(self, file):
        self.file = file
        self.mouseListener.start()
        self.keyboardListener.start()
        self.log.debug('start recording')

    def stop(self):
        self.mouseListener.stop()
        self.keyboardListener.stop()
        self.log.debug('stop recording')


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
        print('parse key', self.key)

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


class PlayBack:

    def __init__(self, file_manager):
        self.fileManager = file_manager
        self.log = Logger('PlayBack')
        self.traces = []

    def traceBack(self):
        for trace in self.traces:
            if trace.getType() == 'click':
                self.click(trace)
            if trace.getType() == 'press':
                self.press(trace)
            else:
                pass

    def press(self, trace):
        pyautogui.typewrite(trace.getKey(), 0.1)

    def click(self, trace):
        pyautogui.moveTo(trace.getX(), trace.getY(), trace.getTime())
        pyautogui.click()

    def play(self, file):
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


class RPTool:

    def __init__(self):
        self.log = Logger('RPTool')
        self.fileManager = FileManager()
        self.file = ''
        self.recorder = Recorder(self.fileManager)
        self.playback = PlayBack(self.fileManager)

    def getTestFolder(self):
        return '{}/tests'.format(self.fileManager.getCurrentFolder())

    def getTestFiles(self):
        return self.fileManager.list(self.getTestFolder())

    def rec(self, test_name):
        self.log.debug('recording \'{0}\'...'.format(test_name))
        self.saveTestFile(test_name)
        self.recorder.start(self.file)

    def delete(self, test_name):
        self.log.debug('deleting \'{0}\'...'.format(test_name))
        self.fileManager.delete(self.getFullFileName(test_name))

    def play(self, test_name):
        self.log.debug('playback \'{0}\'...'.format(test_name))
        self.playback.play(self.getFullFileName(test_name))

    def saveTestFile(self, test_name):
        self.file = self.getFullFileName(test_name)
        self.fileManager.write(self.file, '')
        self.log.debug('saving test file {0}'.format(self.file))

    def getFullFileName(self, test_name):
        return '{0}/{1}'.format(self.getTestFolder(), test_name)
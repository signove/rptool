#!/usr/bin/env python3


# -*- coding: utf-8 -*-
from pynput.keyboard import Key
from core.clock import Clock
from core.logger import Logger
from core.alert import Alert
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener


class Recorder:

    def __init__(self, file_manager):
        self.file = ''
        self.fileManager = file_manager
        self.log = Logger('Recorder')
        self.mouseListener = MouseListener(on_click=self.onClick, on_scroll=self.onScroll, on_move=self.onMove)
        self.keyboardListener = KeyboardListener(on_press=self.onPress, on_release=self.onRelease)
        self.clock = Clock()
        self.alert = Alert('RPTool - Recording')
        self.drag_start = (0, 0)
        self.drag_start = (0, 0)


    def save(self, trace):
        self.fileManager.write(self.file, trace)

    def onClick(self, *args):
        self.clock.start()
        print('click: {}'.format(args))
        pressed = args[3]
        if pressed:
            self.drag_start = (args[0], args[1])
            trace = 'click x={}, y={}, time={}\n'.format(args[0], args[1], self.clock.getTime())
            self.alert.notify(trace)
            self.save(trace)
        else:
            self.drag_end = (args[0], args[1])
            if self.drag_start != self.drag_end:
                x1, y1 = self.drag_start
                x2, y2 = self.drag_end
                trace = 'drag x1={0}, y1={1}, x2={2}, y2={3}\n'.format(x1, y1, x2, y2)
                self.alert.notify(trace)
                self.save(trace)
            else:
                pass

    def onScroll(self, *args):
        dx, dy = args[2], args[3]
        trace = 'scroll dx={0}, dy={1}\n'.format(dx, dy)
        self.save(trace)

    def onMove(self, *args):
        pass
        # x, y
        # self.save('move {}\n'.format(args))

    def onPress(self, *args):
        # key
        trace = 'press key={}\n'.format(args[0])
        self.alert.notify(trace)
        self.save(trace)

    def onRelease(self, *args):
        # Stop recording when press 'esc'
        if args[0] == Key.esc:
            self.stop()
            self.log.debug('stopped recording, ESC key was pressed')
            self.alert.notify('Recording stopped!')
            return False
        if args[0] == Key.f2:
            self.alert.notify('print screen')

    def start(self, file):
        self.file = file
        self.mouseListener.start()
        self.keyboardListener.start()
        self.log.debug('start recording')

    def stop(self):
        self.mouseListener.stop()
        self.keyboardListener.stop()
        self.log.debug('stop recording')

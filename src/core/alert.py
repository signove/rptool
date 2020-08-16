#!/usr/bin/env python3


# -*- coding: utf-8 -*-
import notify2
import os
from src.core.logger import Logger


class Alert:

    def __init__(self, title):
        self.log = Logger
        self.iconPath = '{0}/rptool.png'.format(os.getcwd())
        notify2.init("RPTool Notifier")
        self.n = notify2.Notification(None, icon=self.iconPath)
        self.title = title

    def notify(self, message):
        self.n.set_urgency(notify2.URGENCY_NORMAL)
        self.n.set_timeout(3000)
        self.n.update(self.title, message)
        self.n.show()

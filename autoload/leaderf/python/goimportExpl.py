#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import vim
import os
import os.path
from leaderf.utils import *
from leaderf.explorer import *
from leaderf.manager import *


#*****************************************************
# GoimportExplorer
#*****************************************************
class GoimportExplorer(Explorer):
    def __init__(self):
        pass

    def getContent(self, *args, **kwargs):
        return lfEval("split(system('gopkgs'), '\n')")

    def getStlCategory(self):
        return "Goimport"

    def getStlCurDir(self):
        return escQuote(lfEncode(os.getcwd()))

    def isFilePath(self):
        return False


#*****************************************************
# GoimportExplManager
#*****************************************************
class GoimportExplManager(Manager):
    def __init__(self):
        super(GoimportExplManager, self).__init__()
        self._match_ids = []
        self.flag_import_as = 0

    def _getExplClass(self):
        return GoimportExplorer

    def _defineMaps(self):
        lfCmd("call leaderf#Goimport#Maps()")

    def _setImportAs(self, import_as):
        self.flag_import_as = import_as

    def _cmdExtension(self, cmd):
        if equal(cmd, '<C-D>'):
            self.flag_import_as = 1
            self.accept()
        return True

    def _acceptSelection(self, *args, **kwargs):
        if len(args) == 0:
            return
        line = args[0]

        if self.flag_import_as == 1:
            local_name = lfEval("input('Enter local name: ')")
            lfCmd("GoImportAs " + local_name + " " + line)
        else:
            lfCmd("GoImport " + line)

        self.flag_import_as = 0

    def _getDigest(self, line, mode):
        """
        specify what part in the line to be processed and highlighted
        Args:
            mode: 0, 1, 2, return the whole line
        """
        return line

    def _getDigestStartPos(self, line, mode):
        """
        return the start position of the digest returned by _getDigest()
        Args:
            mode: 0, 1, 2, return 1
        """
        return 1

    def _createHelp(self):
        help = []
        help.append('" <C-D> : switch to ImportAs mode')
        help.append('" i : switch to input mode')
        help.append('" q : quit')
        help.append('" <F1> : toggle this help')
        help.append('" ---------------------------------------------------------')
        return help

    def _afterEnter(self):
        super(GoimportExplManager, self)._afterEnter()
        id = int(lfEval('''matchadd('Lf_hl_goimportTitle', '^mark line .*$')'''))
        self._match_ids.append(id)
        id = int(lfEval('''matchadd('Lf_hl_goimportLineCol', '^\s*\S\+\s\+\zs\d\+\s\+\d\+')'''))
        self._match_ids.append(id)
        id = int(lfEval('''matchadd('Lf_hl_goimportText', '^\s*\S\+\s\+\d\+\s\+\d\+\s*\zs.*$')'''))
        self._match_ids.append(id)

    def _beforeExit(self):
        super(GoimportExplManager, self)._beforeExit()
        for i in self._match_ids:
            lfCmd("silent! call matchdelete(%d)" % i)
        self._match_ids = []


#*****************************************************
# goimportExplManager is a singleton
#*****************************************************
goimportExplManager = GoimportExplManager()

__all__ = ['goimportExplManager']

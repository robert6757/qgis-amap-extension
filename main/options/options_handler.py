# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AMapExtension
                                 Options Handler
 implement ActionHandler class, provide options dialog.
                              -------------------
        begin                : 2025-09-05
        copyright            : (C) 2025 by phoenix-gis
        email                : phoenixgis@sina.com
        website              : phoenix-gis.cn
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from ..action_handler import ActionHandler
from .options_dlg import OptionsDlg

class OptionsHandler(ActionHandler):

    def __init__(self):
        self.iface = None

    def attach(self, iface):
        """attach qgis python interface."""
        self.iface = iface

    def handle_action(self, params):
        # show options dialog.
        dlg = OptionsDlg()
        dlg.setModal(True)
        dlg.show()
        dlg.exec()

    def unload(self):
        """unload this action handler"""
        pass

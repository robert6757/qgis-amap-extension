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
from qgis.PyQt import uic


from ..action_handler import ActionHandler
from ..global_helper import GlobalHelper

import os
import webbrowser

class OptionsHandler(ActionHandler):

    def __init__(self):
        self.iface = None
        self.options_widget = None
        self.options_form = None

    def attach(self, iface):
        """attach qgis python interface."""
        self.iface = iface

    def handle_action(self, params):
        # show options dialog.
        generated_class, base_class = uic.loadUiType(os.path.join(
            os.path.dirname(__file__), '../../ui/OptionsDlg.ui'))
        if generated_class is None or base_class is None:
            return None

        # get amap key from QgsSettings
        amap_key = GlobalHelper.get_access_key()

        # initialize dialog ui
        self.options_widget = base_class()
        self.options_form = generated_class()
        self.options_form.setupUi(self.options_widget)

        self.options_form.btnOK.clicked.connect(self.handle_click_ok)
        self.options_form.btnCancle.clicked.connect(self.handle_click_cancle)
        self.options_form.btnGetKey.clicked.connect(self.handle_click_get_key)
        self.options_form.lineEditKey.setText(amap_key)

        self.options_widget.setModal(True)
        self.options_widget.show()
        self.options_widget.exec_()

    def handle_click_ok(self):
        input_amap_key = self.options_form.lineEditKey.text()
        GlobalHelper.set_access_key(input_amap_key)
        self.options_widget.close()

    def handle_click_cancle(self):
        self.options_widget.close()

    def handle_click_get_key(self):
        url = "https://lbs.amap.com/"
        webbrowser.open(url)

    def unload(self):
        """unload this action handler"""
        if self.options_widget is not None:
            self.options_widget.close()

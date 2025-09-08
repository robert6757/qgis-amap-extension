# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AMapExtension
                                 Options Dialog
 This file defines a dialog for amap options.
                              -------------------
        begin                : 2025-09-08
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

import os
import webbrowser

from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog

from ..global_helper import GlobalHelper

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), '../../ui/OptionsDlg.ui'))

class OptionsDlg(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(OptionsDlg, self).__init__(parent)

        self.setupUi(self)

        # get amap key from QgsSettings
        amap_key = GlobalHelper.get_access_key()

        self.btnOK.clicked.connect(self.handle_click_ok)
        self.btnCancle.clicked.connect(self.handle_click_cancle)
        self.btnGetKey.clicked.connect(self.handle_click_get_key)
        self.lineEditKey.setText(amap_key)

    def handle_click_ok(self):
        input_amap_key = self.lineEditKey.text()
        GlobalHelper.set_access_key(input_amap_key)
        self.close()

    def handle_click_cancle(self):
        self.close()

    def handle_click_get_key(self):
        url = "https://lbs.amap.com/"
        webbrowser.open(url)
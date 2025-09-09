# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AMapExtension
                                 Basemap Handler
 implement ActionHandler class, provide AMap basemap
                              -------------------
        begin                : 2025-09-04
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
from qgis.core import QgsProject, QgsRasterLayer
from qgis.PyQt import uic
from ..global_helper import GlobalHelper
from qgis.PyQt.QtCore import QObject

import os

class BasemapHandler(ActionHandler):

    def __init__(self):
        self.iface = None
        self.addlayer_widget = None
        self.addlayer_form = None

    def attach(self, iface):
        """attach qgis python interface."""
        self.iface = iface

    def handle_action(self, params : str):
        """main process for handling action."""
        if params == GlobalHelper.tr(u"Satellite Layer"):
            layer = QgsRasterLayer(
                'type=xyz&url=https://webst01.is.autonavi.com/appmaptile?style%3D6%26x%3D%7Bx%7D%26y%3D%7By%7D%26z%3D%7Bz%7D&zmax=18&zmin=0',
                '高德卫星图', 'wms')
            if layer.isValid():
                QgsProject.instance().addMapLayer(layer)
        elif params == GlobalHelper.tr(u"Satellite Label Layer"):
            layer = QgsRasterLayer(
                'type=xyz&url=https://webst01.is.autonavi.com/appmaptile?style%3D8%26x%3D%7Bx%7D%26y%3D%7By%7D%26z%3D%7Bz%7D&zmax=18&zmin=0',
                '高德卫星图注记', 'wms')
            if layer.isValid():
                QgsProject.instance().addMapLayer(layer)
        elif params == GlobalHelper.tr(u"Vector Layer"):
            layer = QgsRasterLayer(
                'type=xyz&url=https://webrd01.is.autonavi.com/appmaptile?x%3D%7Bx%7D%26y%3D%7By%7D%26z%3D%7Bz%7D%26lang%3Dzh_cn%26size%3D1%26scl%3D1%26style%3D8&zmax=18&zmin=0',
                '高德矢量图', 'wms')
            if layer.isValid():
                QgsProject.instance().addMapLayer(layer)
        elif params == GlobalHelper.tr(u"Select Layer"):
            # show layer select dialog.
            generated_class, base_class = uic.loadUiType(os.path.join(
                os.path.dirname(__file__), '../../ui/AddLayerDlg.ui'))
            if generated_class is None or base_class is None:
                return None

            # build Qt widget
            self.addlayer_widget = base_class()
            self.addlayer_form = generated_class()
            self.addlayer_form.setupUi(self.addlayer_widget)
            self.addlayer_form.btnAdd.clicked.connect(self.handle_add_layer)
            self.addlayer_form.listWidget.itemDoubleClicked.connect(self.handle_add_layer)

            self.addlayer_form.listWidget.addItem(GlobalHelper.tr(u"Satellite Layer"))
            self.addlayer_form.listWidget.addItem(GlobalHelper.tr(u"Satellite Label Layer"))
            self.addlayer_form.listWidget.addItem(GlobalHelper.tr(u"Vector Layer"))

            self.addlayer_widget.setModal(True)
            self.addlayer_widget.show()
            self.addlayer_widget.exec_()

    def handle_add_layer(self):
        if self.addlayer_form is None:
            return
        current_item = self.addlayer_form.listWidget.currentItem()
        if current_item is None:
            return
        layer_name = current_item.text()
        self.handle_action(layer_name)
        self.addlayer_widget.close()

    def unload(self):
        """unload this action handler"""
        if self.addlayer_widget is not None:
            self.addlayer_widget.close()


# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AMapExtension
                                 Select Region Dialog
 This file defines a dialog for selecting the region used by the search docking widget.
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

import os

from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QHeaderView, QDialog, QTreeWidgetItem, QMessageBox
from .region_dictionary import RegionDictionary
from ..compat import *

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), '../../ui/SelectRegionDlg.ui'))

class SelectRegionDlg(QDialog, FORM_CLASS):
    def __init__(self, prevRegionName, parent=None):
        super(SelectRegionDlg, self).__init__(parent)

        self.setupUi(self)

        self.btnOK.clicked.connect(self.handle_click_ok)
        self.btnNationwide.clicked.connect(self.handle_click_nationwide)
        self.lineEdit.textChanged.connect(self.handle_query_key_changed)

        self.init_tree()

        if prevRegionName is None:
            self.selected_region_name = self.tr(u"Nationwide")
        else:
            # use previous region name.
            self.selected_region_name = prevRegionName
            self.locate_node(prevRegionName)

    def init_tree(self):
        self.treeWidget.header().setSectionResizeMode(ResizeToContents)

        dic_data = RegionDictionary.get_json()

        # enumerate every province
        for province_data in dic_data:
            # create province node.
            province_item = QTreeWidgetItem(self.treeWidget)
            province_item.setText(0, province_data["provice"])

            if "city" not in province_data:
                continue

            # enumerate city
            for city in province_data["city"]:
                # create city node.
                city_item = QTreeWidgetItem(province_item)
                city_item.setText(0, city["name"])

    def handle_click_ok(self):
        selected_treeitem = self.treeWidget.currentItem()
        if selected_treeitem is None:
            QMessageBox.information(self.setting_widget,
                                    self.tr(u"Warning"),
                                    self.tr(u"Please select a region."), QMessageBoxOk)
            return;
        self.selected_region_name = selected_treeitem.text(0)
        self.accept()

    def handle_click_nationwide(self):
        self.selected_region_name = self.tr(u"Nationwide")
        self.accept()

    def handle_query_key_changed(self, text : str):
        self.locate_node(text)

    def get_selected_region(self) -> str:
        return self.selected_region_name

    def locate_node(self, name):
        top_node_i = 0
        for top_node_i in range(0, self.treeWidget.topLevelItemCount()):
            top_node = self.treeWidget.topLevelItem(top_node_i)
            if name in top_node.text(0):
                self.treeWidget.setCurrentItem(top_node)
                return

            # find children node
            child_i = 0
            for child_i in range(0, top_node.childCount()):
                child_node = top_node.child(child_i)
                if name in child_node.text(0):
                    self.treeWidget.setCurrentItem(child_node)
                    return
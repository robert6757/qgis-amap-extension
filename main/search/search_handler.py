# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AMapExtension
                                 Search Handler
 implement ActionHandler class, provide poi search.
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
from qgis.core import QgsSettings, QgsNetworkAccessManager, QgsProject, QgsCoordinateTransform, QgsCoordinateReferenceSystem, QgsPointXY
from qgis.PyQt.QtCore import Qt, QUrl, QUrlQuery, QObject
from qgis.PyQt.QtNetwork import QNetworkRequest, QNetworkReply
from qgis.PyQt.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from ..action_handler import ActionHandler
from .select_region_dlg import SelectRegionDlg
from ..global_helper import GlobalHelper
from .canvas_dot_item import CanvasDotItem
from ..access_key_checker import check_access_key
from ..compat import *

import os
import json

class SearchHandler(ActionHandler):

    def __init__(self):
        self.iface = None
        self.search_widget = None
        self.search_form = None
        self.selected_region_name = None
        self.location_dot = None

        self.__key_tag = "qgis-amap-extension/search/region"

        self.network_manager = QgsNetworkAccessManager.instance()

        self.__poi_longitude_item_role = 300
        self.__poi_latitude_item_role = 301

    def attach(self, iface):
        """attach qgis python interface."""
        self.iface = iface

    def handle_action(self, params):
        if self.search_widget is not None:
            self.search_widget.show()
            return

        # show search dock widget.
        generated_class, base_class = uic.loadUiType(os.path.join(
            os.path.dirname(__file__), '../../ui/SearchDockWidget.ui'))
        if generated_class is None or base_class is None:
            return None

        # get previous region from QgsSettings
        g_setting = QgsSettings()
        self.selected_region_name = g_setting.value(self.__key_tag)

        # initialize dialog ui
        self.search_widget = base_class()
        self.search_form = generated_class()
        self.search_form.setupUi(self.search_widget)

        self.search_form.tableWidget.setColumnCount(3)
        column_headers = [GlobalHelper.tr("Name"), GlobalHelper.tr("City"), GlobalHelper.tr("Address")]
        self.search_form.tableWidget.setHorizontalHeaderLabels(column_headers)

        if self.selected_region_name is not None:
            self.search_form.btnRegion.setText(self.selected_region_name)

        self.search_form.btnRegion.clicked.connect(self.handle_switch_region)
        self.search_form.btnSearch.clicked.connect(self.handle_search)
        self.search_form.btnClear.clicked.connect(self.handle_clear)
        self.search_form.lineEditKey.returnPressed.connect(self.handle_search)
        self.search_form.tableWidget.cellDoubleClicked.connect(self.handle_double_click_table_item)

        # show dock widget
        self.iface.addDockWidget(LeftDockWidgetArea, self.search_widget)

    def unload(self):
        """unload this action handler"""
        if self.search_widget is not None:
            self.iface.removeDockWidget(self.search_widget)
            self.search_widget.close()
            self.search_widget = None
            self.search_form = None

        if self.location_dot is not None:
            self.location_dot.clear()
        map_canvas = self.iface.mapCanvas()
        if map_canvas is not None:
            map_canvas.refresh()

    @check_access_key
    def handle_search(self):
        # clear result list
        while self.search_form.tableWidget.rowCount() > 0:
            self.search_form.tableWidget.removeRow(0)

        if len(self.search_form.lineEditKey.text()) == 0:
            return

        # url = f"https://restapi.amap.com/v5/place/text?key=e7f1bd64ec16414f947f2c508e511c40&keywords=尖沙咀&region=香港特别行政区"
        url = QUrl("https://restapi.amap.com/v5/place/text")
        url_query = QUrlQuery()
        url_query.addQueryItem("page_size", '25')
        url_query.addQueryItem("key", GlobalHelper.get_access_key())
        url_query.addQueryItem("keywords", self.search_form.lineEditKey.text())
        if self.selected_region_name is not None and self.selected_region_name != GlobalHelper.tr(u"Nationwide"):
            url_query.addQueryItem("region", self.selected_region_name)
        url.setQuery(url_query)
        request = QNetworkRequest(url)
        reply = self.network_manager.blockingGet(request)
        if reply.error() != NoError:
            return
        try:
            reply_json = json.loads(reply.content().data())
        except json.decoder.JSONDecodeError:
            self.iface.messageBar().pushWarning(
                GlobalHelper.tr(u"AMap Search Error"),
                GlobalHelper.tr(u"Fail to parse poi results responding from AMap server.")
            )

        if int(reply_json['status']) != 1:
            QMessageBox.information(self.search_widget,
                                    GlobalHelper.tr(u"AMap Search Error"),
                                    GlobalHelper.tr(u"Your request to AMap server is unavailable."), QMessageBoxOk)
            return

        # add result to table widget.
        self.search_form.tableWidget.setRowCount(len(reply_json['pois']))
        row_i = 0
        for poi_item in reply_json['pois']:
            name_item = QTableWidgetItem(poi_item["name"])
            self.search_form.tableWidget.setItem(row_i, 0, name_item)
            city_item = QTableWidgetItem(poi_item["cityname"])
            self.search_form.tableWidget.setItem(row_i, 1, city_item)
            address_item = QTableWidgetItem(poi_item["address"])
            self.search_form.tableWidget.setItem(row_i, 2, address_item)

            # location is stored in Name item.
            location = poi_item["location"].split(',')
            name_item.setData(self.__poi_longitude_item_role, location[0])
            name_item.setData(self.__poi_latitude_item_role, location[1])

            row_i += 1
        self.search_form.tableWidget.resizeColumnsToContents()

    def handle_clear(self):
        # clear dot on map.
        if self.location_dot is not None:
            self.location_dot.clear()

        # clear result table.
        while self.search_form.tableWidget.rowCount() > 0:
            self.search_form.tableWidget.removeRow(0)

        # clear key input.
        self.search_form.lineEditKey.setText("")

        # refresh map canvas.
        map_canvas = self.iface.mapCanvas()
        if map_canvas is not None:
            map_canvas.refresh()

    def handle_switch_region(self):
        sel_region_dlg = SelectRegionDlg(prevRegionName=self.selected_region_name, parent=self.search_widget)
        sel_region_dlg.setModal(True)
        sel_region_dlg.show()
        if sel_region_dlg.exec() != Accepted:
            return

        self.selected_region_name = sel_region_dlg.get_selected_region()
        self.search_form.btnRegion.setText(self.selected_region_name)

        # save region to QgsSettings
        g_setting = QgsSettings()
        g_setting.setValue(self.__key_tag, self.selected_region_name)

    def handle_double_click_table_item(self, row, column):
        # retrieve location from Name item.
        name_table_item = self.search_form.tableWidget.item(row, 0)
        longitude = float(name_table_item.data(self.__poi_longitude_item_role))
        latitude = float(name_table_item.data(self.__poi_latitude_item_role))

        # transform position
        current_project_crs = QgsProject.instance().crs()
        coord_trans = QgsCoordinateTransform(
            QgsCoordinateReferenceSystem("EPSG:4326"),
            current_project_crs,
            QgsProject.instance(),
        )

        position_in_current_proj = coord_trans.transform(QgsPointXY(longitude, latitude))

        # draw dot to canvas
        map_canvas = self.iface.mapCanvas()
        if map_canvas is None:
            return

        if self.location_dot is None:
            # create a blinking dot
            self.location_dot = CanvasDotItem(map_canvas)
        self.location_dot.set_location(position_in_current_proj)
        map_canvas.refresh()

        # pan to the location
        map_canvas.setCenter(position_in_current_proj)





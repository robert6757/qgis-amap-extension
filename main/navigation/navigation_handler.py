# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AMapExtension
                                 Navigation Handler
 implement ActionHandler class, provide navigation.
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

from qgis.PyQt import uic
from qgis.core import QgsNetworkAccessManager, QgsProject, QgsCoordinateTransform
from qgis.core import QgsVectorLayer, QgsFields, QgsCoordinateReferenceSystem, QgsField, QgsFeature, QgsGeometry, QgsPointXY
from qgis.PyQt.QtCore import Qt, QUrl, QUrlQuery, QVariant, QObject, QMetaType
from qgis.PyQt.QtNetwork import QNetworkRequest, QNetworkReply
from qgis.PyQt.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton
from qgis.gui import QgsMapToolEmitPoint

from ..global_helper import GlobalHelper
from ..action_handler import ActionHandler
from ..access_key_checker import *
from .navigation_pin_item import NavigationPinItem
from ..compat import *

import os
import json

class NavigationHandler(ActionHandler):

    def __init__(self):
        self.iface = None
        self.navigation_widget = None
        self.navigation_form = None
        self.origin_location = None
        self.destination_location = None
        self.navigation_pin = None

        # supply to vector layer
        self.layer_name_index = 1
        self.layer_fields = QgsFields()
        self.layer_fields.append(QgsField("road_name", QMetaType.Type.QString))
        self.layer_fields.append(QgsField("orientation", QMetaType.Type.QString))
        self.layer_fields.append(QgsField("instruction", QMetaType.Type.QString))
        self.layer_fields.append(QgsField("step_distance", QMetaType.Type.Int))

        # waypoints
        self.waypoint_index = 1
        self.locating_waypoint_item = None

        self.network_manager = QgsNetworkAccessManager.instance()

        self.__waypoints_location_item_role = 300
        self.__waypoints_id_item_role = 301

    def attach(self, iface):
        """attach qgis python interface."""
        self.iface = iface

    def handle_action(self, params):
        canvas = self.iface.mapCanvas()
        if canvas is not None:
            self.navigation_pin = NavigationPinItem(canvas)

        if self.navigation_widget is not None:
            self.navigation_widget.show()
            return

        # show navigation dock widget.
        generated_class, base_class = uic.loadUiType(os.path.join(
            os.path.dirname(__file__), '../../ui/NavigationDockWidget.ui'))
        if generated_class is None or base_class is None:
            return None

        # initialize dialog ui
        self.navigation_widget = base_class()
        self.navigation_form = generated_class()
        self.navigation_form.setupUi(self.navigation_widget)

        self.navigation_form.cbTransportationType.addItem(GlobalHelper.tr(u"Driving"))
        self.navigation_form.cbTransportationType.addItem(GlobalHelper.tr(u"Walking"))
        self.navigation_form.cbTransportationType.addItem(GlobalHelper.tr(u"Bicycling"))

        self.navigation_form.btnSelOrigin.clicked.connect(self.handle_clicked_origin_btn)
        self.navigation_form.btnSelDestination.clicked.connect(self.handle_clicked_destination_btn)
        self.navigation_form.btnNavigate.clicked.connect(self.handle_clicked_navigate_btn)
        self.navigation_form.btnClear.clicked.connect(self.handle_clicked_clear_btn)
        self.navigation_form.btnAddWaypoints.clicked.connect(self.handle_add_waypoint)
        self.navigation_form.btnRemoveWaypoints.clicked.connect(self.handle_delete_waypoint)
        self.navigation_form.cbTransportationType.currentTextChanged.connect(self.handle_transportation_changed)

        # show dock widget
        self.iface.addDockWidget(LeftDockWidgetArea, self.navigation_widget)

        self.sel_origin_tool = QgsMapToolEmitPoint(self.iface.mapCanvas())
        self.sel_origin_tool.canvasClicked.connect(self.handle_origin_tool_capture)
        self.sel_destination_tool = QgsMapToolEmitPoint(self.iface.mapCanvas())
        self.sel_destination_tool.canvasClicked.connect(self.handle_destination_tool_capture)
        self.sel_waypoint_tool = QgsMapToolEmitPoint(self.iface.mapCanvas())
        self.sel_waypoint_tool.canvasClicked.connect(self.handle_locate_waypoint_capture)

    def unload(self):
        """unload this action handler"""
        if self.navigation_widget is not None:
            self.iface.removeDockWidget(self.navigation_widget)
            self.navigation_widget.close()
            self.navigation_widget = None
            self.navigation_form = None

        self.origin_location = None
        self.destination_location = None
        if self.navigation_pin is not None:
            self.navigation_pin.clear()

        map_canvas = self.iface.mapCanvas()
        if not map_canvas:
            map_canvas.refresh()

    def handle_clicked_origin_btn(self):
        canvas = self.iface.mapCanvas()
        if canvas is None:
            return
        canvas.mapTool()
        canvas.setMapTool(self.sel_origin_tool)

    def handle_clicked_destination_btn(self):
        canvas = self.iface.mapCanvas()
        if canvas is None:
            return
        canvas.mapTool()
        canvas.setMapTool(self.sel_destination_tool)

    def handle_origin_tool_capture(self, point):
        # convert to EPSG:4326
        current_project_crs = QgsProject.instance().crs()
        coord_trans = QgsCoordinateTransform(
            current_project_crs,
            QgsCoordinateReferenceSystem("EPSG:4326"),
            QgsProject.instance(),
        )

        # draw the origin dot
        map_canvas = self.iface.mapCanvas()
        self.navigation_pin.set_location(point, 0)
        map_canvas.refresh()

        self.origin_location = coord_trans.transform(point)

        # unset map tool
        map_canvas.unsetMapTool(self.sel_origin_tool)

    def handle_destination_tool_capture(self, point):
        # convert to EPSG:4326
        current_project_crs = QgsProject.instance().crs()
        coord_trans = QgsCoordinateTransform(
            current_project_crs,
            QgsCoordinateReferenceSystem("EPSG:4326"),
            QgsProject.instance(),
        )

        # draw the origin dot
        map_canvas = self.iface.mapCanvas()
        self.navigation_pin.set_location(point, 1)
        map_canvas.refresh()

        self.destination_location = coord_trans.transform(point)

        # unset map tool
        map_canvas.unsetMapTool(self.sel_destination_tool)

    def handle_add_waypoint(self):
        row_index = self.navigation_form.tableWidgetWaypoints.rowCount()
        self.navigation_form.tableWidgetWaypoints.setRowCount(row_index+1)

        waypoint_item = QTableWidgetItem(GlobalHelper.tr("waypoint") + "_" + str(self.waypoint_index))
        waypoint_item.setData(self.__waypoints_id_item_role, self.waypoint_index)
        self.navigation_form.tableWidgetWaypoints.setItem(row_index, 0, waypoint_item)

        locate_btn = QPushButton(GlobalHelper.tr("Pin"))
        locate_btn.clicked.connect(lambda : self.handle_locate_waypoint(waypoint_item))
        self.navigation_form.tableWidgetWaypoints.setCellWidget(row_index, 1, locate_btn)

        self.waypoint_index += 1

    def handle_delete_waypoint(self):
        selected_waypoint_items = self.navigation_form.tableWidgetWaypoints.selectedItems()
        if len(selected_waypoint_items) == 0:
            return

        # find the waypoint widget item.
        current_waypoint_item = self.navigation_form.tableWidgetWaypoints.item(selected_waypoint_items[0].row(), 0)

        # remove pin from map
        waypoint_id = current_waypoint_item.data(self.__waypoints_id_item_role)
        self.navigation_pin.remove_waypoint_location(waypoint_id)
        canvas = self.iface.mapCanvas()
        if canvas is not None:
            canvas.refresh()

        self.navigation_form.tableWidgetWaypoints.removeRow(current_waypoint_item.row())

    def handle_locate_waypoint(self, selected_item):
        self.locating_waypoint_item = selected_item
        canvas = self.iface.mapCanvas()
        if canvas is None:
            return
        canvas.mapTool()
        canvas.setMapTool(self.sel_waypoint_tool)

    def handle_locate_waypoint_capture(self, point):
        # convert to EPSG:4326
        current_project_crs = QgsProject.instance().crs()
        coord_trans = QgsCoordinateTransform(
            current_project_crs,
            QgsCoordinateReferenceSystem("EPSG:4326"),
            QgsProject.instance(),
        )

        # draw the waypoint dot
        waypoint_id = self.locating_waypoint_item.data(self.__waypoints_id_item_role)
        map_canvas = self.iface.mapCanvas()
        self.navigation_pin.set_waypoint_location(point, waypoint_id)
        map_canvas.refresh()

        waypoint_location = coord_trans.transform(point)

        # save converted location to talbewidget item.
        self.locating_waypoint_item.setData(self.__waypoints_location_item_role, waypoint_location)

        # unset map tool
        map_canvas.unsetMapTool(self.sel_waypoint_tool)

    def handle_clicked_clear_btn(self):
        self.origin_location = None
        self.destination_location = None
        map_canvas = self.iface.mapCanvas()
        if map_canvas is not None:
            map_canvas.refresh()

        self.waypoint_index = 1
        self.locating_waypoint_item = None
        self.navigation_pin.clear()
        while self.navigation_form.tableWidgetWaypoints.rowCount() > 0:
            self.navigation_form.tableWidgetWaypoints.removeRow(0)

    @check_access_key
    def handle_clicked_navigate_btn(self):
        if self.origin_location is None or self.destination_location is None:
            QMessageBox.information(self.navigation_widget,
                                    GlobalHelper.tr(u"Warning"),
                                    GlobalHelper.tr(u"Please select origin and destination on the map."), QMessageBoxOk)
            return;

        transportation_type = self.navigation_form.cbTransportationType.currentText()

        # build request params
        if transportation_type == GlobalHelper.tr("Driving"):
            url = QUrl("https://restapi.amap.com/v5/direction/driving")
        elif transportation_type == GlobalHelper.tr("Walking"):
            url = QUrl("https://restapi.amap.com/v5/direction/walking")
        elif transportation_type == GlobalHelper.tr("Bicycling"):
            url = QUrl("https://restapi.amap.com/v5/direction/bicycling")
        url_query = QUrlQuery()
        url_query.addQueryItem("key", GlobalHelper.get_access_key())
        url_query.addQueryItem("show_fields", "polyline")
        url_query.addQueryItem("origin", "{0},{1}".format(self.origin_location.x(), self.origin_location.y()))
        url_query.addQueryItem("destination", "{0},{1}".format(self.destination_location.x(), self.destination_location.y()))
        url_query.addQueryItem("waypoints", self.__build_waypoint_url_query())
        url.setQuery(url_query)
        request = QNetworkRequest(url)
        reply = self.network_manager.blockingGet(request)
        if reply.error() != NoError:
            return
        try:
            reply_json = json.loads(reply.content().data())

            ##############################################
            # debug
            # with open('d:/output.txt', 'w', encoding='utf-8') as file:
            #     file.write(json.dumps(reply_json, indent=2, ensure_ascii=False))
            ##############################################
        except json.decoder.JSONDecodeError:
            self.iface.messageBar().pushWarning(
                GlobalHelper.tr(u"AMap Navigation Error"),
                GlobalHelper.tr(u"Fail to parse navigation results responding from AMap server.")
            )

        if int(reply_json['status']) != 1:
            QMessageBox.information(self.navigation_form,
                                    GlobalHelper.tr(u"AMap Search Error"),
                                    GlobalHelper.tr(u"Your request to AMap server is unavailable."), QMessageBoxOk)
            return

        reply_route = reply_json["route"]
        if not reply_route:
            return

        reply_route_paths = reply_route["paths"]
        if not reply_route_paths:
            return

        for route_path in reply_route_paths:
            navi_vector_layer = self.__create_route_layer("navi_result_{}".format(self.layer_name_index))
            navi_vector_layer.startEditing()

            # Add every step as a feature that is inserted into the layer.
            route_path_steps = route_path["steps"]
            for path_step in route_path_steps:
                self.__add_road_into_layer(navi_vector_layer, path_step)

            navi_vector_layer.commitChanges()
            self.layer_name_index += 1

            # add layer to map
            QgsProject.instance().addMapLayer(navi_vector_layer)

    def handle_transportation_changed(self, transportation):
        waypoint_enable = False
        if transportation == GlobalHelper.tr(u"Driving"):
            waypoint_enable = True

        self.navigation_form.tableWidgetWaypoints.setEnabled(waypoint_enable)
        self.navigation_form.btnAddWaypoints.setEnabled(waypoint_enable)
        self.navigation_form.btnRemoveWaypoints.setEnabled(waypoint_enable)
        self.navigation_pin.set_waypoint_enabled(waypoint_enable)

        canvas = self.iface.mapCanvas()
        if canvas is not None:
            canvas.refresh()

    def __create_route_layer(self, layer_name) -> QgsVectorLayer:
        # specific vector parameters.
        geometry_name = "LineString"
        crs_name = "EPSG:4326"

        # create vector layer by memory provider.
        navi_result_layer = QgsVectorLayer(f"{geometry_name}?crs={crs_name}", layer_name, "memory")
        navi_result_layer.dataProvider().addAttributes(self.layer_fields)
        navi_result_layer.updateFields()

        return navi_result_layer

    def __add_road_into_layer(self, layer : QgsVectorLayer, road_params):
        """
        road_params: {
            "instruction": "沿科荟路向西骑行153米左转",
            "orientation": "西",
            "road_name": "科荟路",
            "step_distance": 153,
            "polyline": "116.392734,40.009757;116.392661,40.009757;116.392661,40.009757;116.391801,40.009753;116.391801,40.009753;116.391163,40.00974;116.391163,40.00974;116.391029,40.00974;116.391029,40.00974;116.390911,40.009744"
        }
        """

        # build line geometry
        point_array = road_params["polyline"].split(";")
        qgspointxy_array = []
        for point_str in point_array:
            point_splited = point_str.split(',')
            qpxy = QgsPointXY(float(point_splited[0]), float(point_splited[1]))
            qgspointxy_array.append(qpxy)

        line_geometry = QgsGeometry.fromPolylineXY(qgspointxy_array)

        # build feature
        feature = QgsFeature()
        feature.setGeometry(line_geometry)
        feature.setFields(self.layer_fields)

        if "road_name" in road_params:
            road_name = road_params["road_name"]
        else:
            road_name = ""
        if "instruction" in road_params:
            instruction = road_params["instruction"]
        else:
            instruction = ""
        if "orientation" in road_params:
            orientation = road_params["orientation"]
        else:
            orientation = ""
        if "step_distance" in road_params:
            step_distance = int(road_params["step_distance"])
        else:
            step_distance = 0

        # set attribute
        feature.setAttributes([road_name, orientation, instruction, step_distance])

        layer.addFeature(feature)

    def __build_waypoint_url_query(self) -> str:
        if not self.navigation_form.tableWidgetWaypoints.isEnabled():
            return ""

        query_str = ""
        row_count = self.navigation_form.tableWidgetWaypoints.rowCount()
        for row_i in range(row_count):
            waypoint_item = self.navigation_form.tableWidgetWaypoints.item(row_i, 0)
            location = waypoint_item.data(self.__waypoints_location_item_role)
            if location is None:
                continue
            query_str += "{0},{1};".format(location.x(), location.y())

        return query_str

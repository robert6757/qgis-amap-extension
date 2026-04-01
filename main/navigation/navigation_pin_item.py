# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AMapExtension
                                 Navigation Pin Item
 provide a pin drawing on the QGIS map canvas.
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

from qgis.gui import QgsMapCanvasItem
from qgis.PyQt.QtGui import QColor
from ..compat import *

class NavigationPinItem(QgsMapCanvasItem):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.canvas = canvas
        self.radius = 5

        self.origin_pin_location = None
        self.destination_pin_location = None
        self.waypoint_enable = True

        self.waypoint_pins = {}

    def set_location(self, location, pin_type):
        # 0: origin pin
        # 1: destination pin
        if pin_type == 0:
            self.origin_pin_location = location
        elif pin_type == 1:
            self.destination_pin_location = location

    def set_waypoint_location(self, location, waypoint_id):
        self.waypoint_pins[waypoint_id] = location

    def remove_waypoint_location(self, waypoint_id):
        if waypoint_id not in self.waypoint_pins:
            return
        self.waypoint_pins.pop(waypoint_id)

    def set_waypoint_enabled(self, enabled):
        self.waypoint_enable = enabled

    def clear(self):
        self.origin_pin_location = None
        self.destination_pin_location = None
        self.waypoint_pins = {}

    def paint(self, painter, option, widget):
        if self.origin_pin_location is not None:
            # convert from coordinates to canvas position.
            point = self.toCanvasCoordinates(self.origin_pin_location)
            painter.setBrush(QColor(0, 255, 0))
            painter.setPen(NoPen)
            painter.drawEllipse(point, self.radius, self.radius)

        if self.destination_pin_location is not None:
            # convert from coordinates to canvas position.
            point = self.toCanvasCoordinates(self.destination_pin_location)
            painter.setBrush(QColor(255, 0, 0))
            painter.setPen(NoPen)
            painter.drawEllipse(point, self.radius, self.radius)

        if self.waypoint_enable:
            for waypoint_pin_index in self.waypoint_pins.keys():
                # convert from coordinates to canvas position.
                point = self.toCanvasCoordinates(self.waypoint_pins[waypoint_pin_index])
                painter.setBrush(QColor(0, 255, 255))
                painter.setPen(NoPen)
                painter.drawEllipse(point, self.radius, self.radius)



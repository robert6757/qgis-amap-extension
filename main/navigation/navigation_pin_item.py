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
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QColor

class NavigationPinItem(QgsMapCanvasItem):
    def __init__(self, pin_type : int, canvas):
        super().__init__(canvas)
        self.canvas = canvas
        self.location = None
        self.radius = 10

        # 0: origin pin
        # 1: destination pin
        self.pin_type = pin_type

    def set_location(self, location):
        self.location = location

    def clear(self):
        self.location = None

    def paint(self, painter, option, widget):
        if self.location is None:
            return

        # convert from coordinates to canvas position.
        point = self.toCanvasCoordinates(self.location)

        # draw pin with red or green.
        if self.pin_type == 0:
            painter.setBrush(QColor(0, 255, 0))
        else:
            painter.setBrush(QColor(255, 0, 0))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(point, self.radius, self.radius)

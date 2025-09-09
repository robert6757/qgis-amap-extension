# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AMapExtension
                                 CanvasDotItem
 provide a red dot drawing on the QGIS map canvas.
                              -------------------
        begin                : 2025-09-06
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

class CanvasDotItem(QgsMapCanvasItem):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.canvas = canvas
        self.radius = 5

    def set_location(self, location):
        self.location = location

    def clear(self):
        self.location = None

    def paint(self, painter, option, widget):
        if self.location is None:
            return

        # convert from coordinates to canvas position.
        point = self.toCanvasCoordinates(self.location)

        # draw yellow point
        painter.setBrush(QColor(255, 255, 0))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(point, self.radius, self.radius)

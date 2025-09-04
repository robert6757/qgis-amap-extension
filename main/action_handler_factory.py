# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AMapExtension
                                 Action Handler Factory
 this is a factory class that creates implement of action handler.
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

from .basemap.basemap_handler import BasemapHandler

class ActionHandlerFactory:

    def __init__(self):
        pass

    @staticmethod
    def create_basemap_handler(iface):
        basemap_handler = BasemapHandler()
        basemap_handler.attach(iface)
        return basemap_handler
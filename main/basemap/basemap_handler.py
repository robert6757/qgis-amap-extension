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

class BasemapHandler(ActionHandler):

    def __init__(self):
        self.iface = None
        pass

    def attach(self, iface):
        """attach qgis python interface."""
        self.iface = iface

    def handle_action(self, params : str):
        """main process for handling action."""
        if params == "Satellite Layer":
            pass
        elif params == "Satellite Label Layer":
            pass
        elif params == "Vector Layer":
            pass
        elif params == "Select Layer":
            # show layer select dialog.
            pass


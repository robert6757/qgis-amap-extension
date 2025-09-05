# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AMapExtension
                                 Action Handler
 This is an abstract class that provides QAction handler.
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

from abc import ABC, abstractmethod

class ActionHandler(ABC):
    @abstractmethod
    def attach(self, iface):
        """attach qgis python interface."""
        pass

    @abstractmethod
    def handle_action(self, params):
        """main process for handling action."""
        pass

    @abstractmethod
    def unload(self):
        """unload this action handler"""
        pass

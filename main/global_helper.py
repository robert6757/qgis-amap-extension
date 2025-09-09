# -*- coding: utf-8 -*-
"""
/***************************************************************************
                               GlobalHelper
 supply some significant function for global environment.

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

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import QgsSettings

class GlobalHelper():

    __access_key_tag = "qgis-amap-extension/key"

    @staticmethod
    def get_access_key():
        g_setting = QgsSettings()
        return g_setting.value(GlobalHelper.__access_key_tag)

    @staticmethod
    def set_access_key(key):
        g_setting = QgsSettings()
        g_setting.setValue(GlobalHelper.__access_key_tag, key)

    @staticmethod
    def tr(message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate("GlobalHelper", message)

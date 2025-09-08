# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AMapExtension
                                 Access Key Checker
 Check the AMap access key and show the options dialog.
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

from functools import wraps

from .global_helper import GlobalHelper
from .options.options_dlg import OptionsDlg

def check_access_key(func):
    @wraps(func)
    def wrapper(params):
        access_key = GlobalHelper.get_access_key()
        if not access_key:
            # show options dialog.
            options_dlg = OptionsDlg()
            options_dlg.setModal(True)
            options_dlg.show()
            options_dlg.exec()

        # check access again.
        access_key = GlobalHelper.get_access_key()
        if not access_key:
            return False

        # execute decorated function.
        return func(params)

    return wrapper


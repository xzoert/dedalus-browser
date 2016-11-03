#!/bin/bash
pyside-uic navigator.ui -o navigator_widget.py
pyside-rcc -py3 -o resources_rc.py resources.qrc


#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication

from model.model import model
from view.view import view
from controller.controller import controller

if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = model(1)
    view = view()
    controller = controller()

    view.setModel(model)
    view.setController(controller)

    model.setView(view)

    controller.setView(view)
    controller.setModel(model)

    sys.exit(app.exec_())

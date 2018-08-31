import sys

from PyQt5.QtCore import QAbstractListModel,QModelIndex,QUrl,QTimer
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView


class Model(QAbstractListModel):
    def __init__(self, schema, parent=None):
        super(Model, self).__init__(parent)

        # Each item is a dictionary of key/value pairs
        self.items = list()

        # QML requires a model to define upfront
        # exactly which roles it can supply. I refer
        # to this as the models "schema".
        self.schema = schema

    def append(self, item):
        """Append item to end of model"""
        self.beginInsertRows(QModelIndex(),
                             self.rowCount(),
                             self.rowCount())

        self.items.append(item)
        self.endInsertRows()

    def data(self, index, role):
        """Return value of item[`index`] of `role`"""
        key = self.schema[role]
        return self.items[index.row()].get(key)

    def setData(self, index, value, role):
        """Set item[`index`] of `role` to `value`"""
        key = self.schema[role]
        self.items[index.row()][key] = value
        self.dataChanged.emit(index, index)

    def rowCount(self, parent=QModelIndex()):
        return len(self.items)

    def roleNames(self):
        """Role names are used by QML to map key to role"""
        return dict(enumerate(self.schema))

def main():
    app = QGuiApplication(sys.argv)

    view = QQuickView()

    schema = [
        "pyLabel",
        "pyColor",
    ]

    model = Model(schema)

    items = [
        {
            "pyLabel": "First Item",
            "pyColor": "white",
        },
        {
            "pyLabel": "Second Item",
            "pyColor": "white",
        }
    ]

    for item in items:
        model.append(item)

    engine = view.engine()
    context = engine.rootContext()
    context.setContextProperty("pyModel", model)

    view.setSource(QUrl("app.qml"))
    view.setResizeMode(view.SizeRootObjectToView)
    view.show()

    # Appending to the model
    QTimer.singleShot(2000, lambda: model.append({
        "pyLabel": "Third Item",
        "pyColor": "steelblue"
    }))

    # Modifying an item in the model
    QTimer.singleShot(3000, lambda: model.setData(
        model.createIndex(1, 0),  # 1th item, 0th column
        "New pLabel!",
        schema.index("pyLabel"),
    ))

    app.exec_()
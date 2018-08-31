from PyQt5.QtCore import QObject, QTimer, pyqtProperty, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlListProperty, QQmlApplicationEngine, qmlRegisterType
from sys import argv

import sys
import os
from walk_dir import walk

obj = walk()


class Channel(QObject):
    nameChanged = pyqtSignal()

    def __init__(self, name='', *args, **kwargs):
        print('Channel')
        super().__init__(*args, **kwargs)
        self._name = name

    @pyqtProperty('QString', notify=nameChanged)
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name != self._name:
            self._name = name
            self.nameChanged.emit()


class Store(QObject):
    channelsChanged = pyqtSignal()

    def __init__(self, *args, **kwargs):
        print('Store')
        super().__init__(*args, **kwargs)
        self._channels = []
        #     Channel('Foo'),
        #     Channel('Bar')
        # ]

    @pyqtSlot(int, str, name="sum")
    def sum(self, index, checked):
        pass
        list_file_for_copy = []
        for i in obj.get_walk_dbsta(index):
            list_file_for_copy.append(i)
        for i in list_file_for_copy:
            print(i)

    @pyqtProperty(QQmlListProperty, notify=channelsChanged)
    def channels(self):
        return QQmlListProperty(Channel, self, self._channels)

    @channels.setter
    def channels(self, channels):
        if channels != self._channels:
            self._channels = channels
            self.channelsChanged.emit()

    def appendChannel(self, channel):
        self._channels.append(channel)
        self.channelsChanged.emit()


def qml(scan_dir):
    path_to_qml = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'qml', 'button', 'main.qml')
    app = QGuiApplication(argv)

    # qmlRegisterType(Channel, 'Example', 1, 0, 'Channel')
    # qmlRegisterType(Store, 'Example', 1, 0, 'Store')

    store = Store()

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty('store', store)
    engine.load(path_to_qml)

    # After 3 seconds, we append a new Channel
    for i in os.listdir(scan_dir):
        store.appendChannel(Channel(i))

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

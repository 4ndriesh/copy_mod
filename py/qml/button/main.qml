import QtQuick 2.7
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import QtQuick.Controls.Styles 1.4


ApplicationWindow {
    color: "#C0C0C0"
    visible: true
    x: 400
    y: 200
    width: 1000
    height: 550
    title: qsTr("WoW")


    ColumnLayout {
        anchors.fill: parent
        ListView {
            objectName : "lvob"
            model: store.channels

            delegate: Item {
            id: item
            anchors.left: parent.left
            anchors.right: parent.right
            height: 45

            GridLayout{
                anchors.fill: parent
                columns: 2

                Rectangle {
                    border.color: "black"
                    Text{
                       text: name
                       anchors.centerIn: parent
//                       anchors { fill: parent; margins: 10 }

                       font.pixelSize: 20
                       color: "black"
                    }
                    color: "#DCDCDC"
                    Layout.fillHeight: true
                    Layout.fillWidth: true
//                    Layout.columnSpan: 2
//                    Layout.rowSpan: 1
                    Layout.row: 1
                    Layout.column: 1
                }

                Rectangle {
                    Button {
                        id: control
                        text: qsTr("Обновить")
                        contentItem: Text {
                            text: control.text
                            font: control.font
                            opacity: enabled ? 1.0 : 0.3
                            color: control.down ? "red" : "black"
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                            elide: Text.ElideRight
                        }
                            background: Rectangle {
                                implicitWidth: 80
                                implicitHeight: 40
                                opacity: enabled ? 1 : 0.3
                                border.color: control.down ? "red" : "black"
                                border.width: 2
                                radius: 10

                            // I want to change text color next
                            }
                        onClicked: {
                            store.sum(index, checked)
                        }
                    anchors.centerIn: parent
                    }
                    color: "grey"
                    width: 100;
                    Layout.fillHeight: true
//                    Layout.fillWidth: true
                    Layout.row: 1
                    Layout.column: 2
                }

            }
        }
            Layout.fillWidth: true
            Layout.fillHeight: true
            ScrollBar.vertical: ScrollBar {}
        }
    }
}
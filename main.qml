import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.12

ApplicationWindow {
    width: 940;
    height: 580;
    visible: true;
    title: qsTr("Hello World");

    background: Rectangle {
        color: 'lightgray';
    }

    ColumnLayout{
        anchors.fill: parent;
        spacing: parent.height / 10;

        Item{
            Layout.fillHeight: true;
        }

        TextField {
            id: dataWord;
            Layout.alignment: Qt.AlignCenter;
            placeholderText: 'Data Word';
            selectByMouse: true;
            selectionColor: 'lightgray';
            font.pointSize: 18;
            implicitWidth: 300;
            implicitHeight: 50;

            onTextChanged: {
                let flag1;
                let flag2;
                if(text === '')
                    btn1.enabled = false;
                else flag1 = true;

                if(/[a-z2-9]/.test(text)){
                    btn1.enabled = false;
                    resLbl.font.pointSize = 18;
                    resLbl.color = 'red';
                    resLbl.text = 'Only 0 and 1 accepted...';
                }
                else{
                    flag2 = true;
                    resLbl.font.pointSize = 14;
                    resLbl.text = '';
                }

                if(flag1 && flag2)
                    btn1.enabled = true;
            }
        }
        Button {
            id: btn1;
            Layout.alignment: Qt.AlignCenter;
            enabled: false;
            background: Rectangle{
                implicitWidth: 90;
                implicitHeight: 40;
                color: 'gray';
            }
            Text{
                anchors.centerIn: parent;
                text: 'Submit';
            }

            onClicked: {
                hamming.setDataWord(dataWord.text);
                let data = hamming.getDataWord;

                let m = data.length;
                hamming.calcRedundantBits(m);

                hamming.posRedundantBits(data);

                hamming.calcParityBits();

                codeWord.text = hamming.getCodeWord;

                btn2.visible = true;

            }
        }

        TextField{
            id: codeWord;
            Layout.alignment: Qt.AlignCenter;
            placeholderText: 'Received Code Word';
            selectByMouse: true;
            selectionColor: 'lightgray';
            font.pointSize: 18;
            implicitWidth: 300;
            implicitHeight: 50;
        }

        Button{
            id: btn2;
            visible: false;
            Layout.alignment: Qt.AlignCenter;
            background: Rectangle{
                implicitWidth: 90;
                implicitHeight: 40;
                color: 'gray';
            }

            Text{
                anchors.centerIn: parent;
                text: 'Compare';
            }

            onClicked: {
                hamming.detectError(codeWord.text);
                let data = hamming.getCodeWord;
                const errPos = hamming.getErrPos;
                if(errPos !== 0){
                    resLbl.color = 'red';
                    resLbl.text = 'The position of error is ' + errPos +
                                      ' from the left';
                }
                else {
                    resLbl.color = 'green';
                    resLbl.text = 'There is no error in the received data.'
                }
            }
        }

        Label{
            id: resLbl;
            Layout.fillHeight: true;
            Layout.alignment: Qt.AlignCenter;
            font.pointSize: 14;
        }
    }
}

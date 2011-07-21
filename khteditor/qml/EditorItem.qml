import QtQuick 1.1
import com.nokia.meego 1.0
import net.khertan.qmlcomponents 1.0

Page {
    property string filepath;
    property string filename;

    anchors.fill:parent
    Rectangle {
            id:titlebar
            width:parent.width
            height:48
            anchors.top: parent.top
            color:'black'
            Text {
                id:titlelabel
                anchors.fill: parent
                anchors.leftMargin: 5
                font { bold: true; family: "Nokia Pure Text"; pixelSize: 18 }
                color:"#cc6633"
                text:((editor.modification) ? '* ':'')+filepath
                verticalAlignment: "AlignVCenter"
            }        
        }    

    Flickable {
        id:flicker
        width: parent.width; height: parent.height - 48
        contentWidth: editor.width; contentHeight: editor.height
        clip: true
        anchors.top: titlebar.bottom
        boundsBehavior:Flickable.DragOverBounds

        QmlTextEditor {
        //TextEdit{
           id:editor

            //width: 850
            //height:480

            onWidthChanged:{
                flicker.contentWidth=editor.width
            }
            onHeightChanged:{
                flicker.contentHeight=editor.height
            }
        }
    }

    function loadFile(filePath){
       filepath = filePath
       editor.loadFile(filePath)
    }

}
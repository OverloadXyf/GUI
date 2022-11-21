from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QApplication, QMainWindow
import sys


def oneClickButton():
    print('这里的x,y是弹出框的')
    print("widget.x()=%d" % widget.x())
    print("widget.y()=%d" % widget.y())
    print("widget.width()=%d" % widget.width())
    print("widget.height()=%d" % widget.height())

    print('这里的x,y是工作区的')
    print("widget.geometry().x()=%d" % widget.geometry().x())
    print("widget.geometry().y()=%d" % widget.geometry().y())
    print("widget.geometry().width()=%d" % widget.geometry().width())
    print("widget.geometry().height()=%d" % widget.geometry().height())

    print('这里的是弹出框的尺寸')
    print("widget.frameGeometry().x()=%d" % widget.frameGeometry().x())
    print("widget.frameGeometry().y()=%d" % widget.frameGeometry().y())
    print("widget.frameGeometry().width()=%d" % widget.frameGeometry().width())
    print("widget.frameGeometry().height()=%d" % widget.frameGeometry().height())


app = QApplication(sys.argv)

widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')

btn.clicked.connect(oneClickButton)

btn.move(24, 52)

widget.resize(300, 200)  # 设置工作区的尺寸大小而不是整个弹出框
widget.move(250, 200)

widget.setWindowTitle('屏幕坐标系')
widget.show()

sys.exit(app.exec_())

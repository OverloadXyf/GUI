# QDesktopWidget

'''将主窗口居中的计算方式'''

from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow
import sys
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):

    # 继承 需要一个parent参数
    def __init__(self):
        super(CenterForm, self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle('窗口居中')

        # 设置窗口的尺寸
        self.resize(400, 300)

        # 设置窗口居中
        self.center()

        # 初始化一个状态栏
        self.status = self.statusBar()

        # 显示一个只存在5秒的消息
        self.status.showMessage('只存在五秒的消息', 5000)

    def center(self):
        # 得到屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 得到窗口的坐标系
        size = self.geometry()

        # 居中时 框的左上角位置坐标
        newLeft = (screen.width() - size.width()) // 2
        newTop = (screen.height() - size.height()) // 2

        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = CenterForm()

    mainWindow.show()
    sys.exit(app.exec_())

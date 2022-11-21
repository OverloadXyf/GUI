from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QIcon


class FirstMainWindow(QMainWindow):

    # 继承 需要一个parent参数
    def __init__(self):
        super(FirstMainWindow, self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')

        # 设置窗口的尺寸 
        self.resize(400, 300)

        # 初始化一个状态栏
        self.status = self.statusBar()

        # 显示一个只存在5秒的消息
        self.status.showMessage('只存在五秒的消息', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('play.jpeg'))
    mainWindow = FirstMainWindow()

    mainWindow.show()
    sys.exit(app.exec_())

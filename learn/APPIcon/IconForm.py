from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QApplication, QMainWindow
import sys
from PyQt5.QtGui import QIcon


class IconForm(QMainWindow):

    def __init__(self):
        super(IconForm, self).__init__()

        self.resize(300, 400)
        self.setWindowTitle('退出应用程序')

        # 添加一个Button
        self.button1 = QPushButton('退出应用程序')
        # 将信号与槽关联
        self.button1.clicked.connect(self.oneClick_Button)

        # 创建水平布局
        layout = QHBoxLayout()
        # 将空间加入到水平布局当中
        layout.addWidget(self.button1)

        # 搞一个frame容器
        mainFrame = QWidget()
        # 把布局放在容器里
        mainFrame.setLayout(layout)

        # 把主框架放在整个窗口上
        self.setCentralWidget(mainFrame)

        # 就这一句话（添加ICON）
        self.setWindowIcon(QIcon(r'C:\Users\NAME\Desktop\GUI\learn\WindowType\play.jpeg'))

    # 按钮单击事件方法（自定的槽）
    def oneClick_Button(self):
        # sender是一个QObject 是一个对象
        sender = self.sender()
        # 打印是哪一个对象被按下
        print(sender.text() + '按钮,被按下')
        # 返回的是一个QCoreApplication 返回应用程序核心
        app = QApplication.instance()
        # 退出应用
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # app.setWindowIcon(QIcon(r'C:\Users\NAME\Desktop\GUI\learn\WindowType\play.jpeg'))
    mainWindow = IconForm()

    mainWindow.show()
    sys.exit(app.exec_())


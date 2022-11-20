import sys
import Horizontal_Layout

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

if __name__ == '__main__':
    # 1.创建应用程序
    app = QApplication(sys.argv)

    # 2.创建主窗口 qt5中的类
    mainWindow = QMainWindow()

    # 3.实例化QTDesigner转换后的UI文件的类
    ui = Horizontal_Layout.Ui_MainWindow()

    # 4.用Horizontal_Layout类的方法创建UI
    # 传入的是窗口对象
    # 向主窗口传入控件
    ui.setupUi(mainWindow)

    # 5.显示
    mainWindow.show()

    # 6.程序循环 等待退出响应
    sys.exit(app.exec_())

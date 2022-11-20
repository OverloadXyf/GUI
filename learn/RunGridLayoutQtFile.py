import sys
import Grid_Layout
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # 创建APP
    app = QApplication(sys.argv)

    # 创建主窗口
    mainWindow = QMainWindow()

    # 创建设计出的UI
    ui = Grid_Layout.Ui_MainWindow()

    # 将主窗口设置为ui
    ui.setupUi(mainWindow)

    # 运行主窗口
    mainWindow.show()

    # 程序循环响应直到退出
    sys.exit(app.exec_())

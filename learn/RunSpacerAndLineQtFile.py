import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import SpacerAndLine

'''
显示的效果是给不同的按键之间加上间隙或者分割线
可以控制控件的最大最小尺度
'''

if __name__ == '__main__':
    # 创建APP
    app = QApplication(sys.argv)

    # 创建主窗口
    mainWindow = QMainWindow()

    # 拿到UI类
    ui = SpacerAndLine.Ui_MainWindow()

    # 对主窗口进行设置
    ui.setupUi(mainWindow)

    # 窗口显示
    mainWindow.show()

    # 程序循环
    sys.exit(app.exec_())

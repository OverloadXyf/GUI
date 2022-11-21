import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import PartnerRelationship.SignalAndSlot as SignalAndSlot


'''
主要是信号与槽 还有属性的选择
enable
setVisible
setEnable
click()
close()
toggle(bool)
'''
if __name__ == '__main__':
    # 创建APP
    app = QApplication(sys.argv)

    # 创建主窗口
    mainWindow = QMainWindow()

    # 拿到UI类
    ui = SignalAndSlot.Ui_MainWindow()

    # 对主窗口进行设置
    ui.setupUi(mainWindow)

    # 窗口显示
    mainWindow.show()

    # 程序循环
    sys.exit(app.exec_())

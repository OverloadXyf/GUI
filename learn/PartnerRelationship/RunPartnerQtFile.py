import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import PartnerRelationship.Partner as Partner


'''
这里按住alt+a alt+b alt+c 就可以使用伙伴关系
label后面的文本里加入(&A) (&B) (&C)
'''
if __name__ == '__main__':
    # 创建APP
    app = QApplication(sys.argv)

    # 创建主窗口
    mainWindow = QMainWindow()

    # 拿到UI类
    ui = Partner.Ui_MainWindow()

    # 对主窗口进行设置
    ui.setupUi(mainWindow)

    # 窗口显示
    mainWindow.show()

    # 程序循环
    sys.exit(app.exec_())

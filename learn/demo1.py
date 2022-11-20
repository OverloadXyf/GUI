import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplication的类实例
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()

    # 设置窗口尺寸 也就是宽高
    w.resize(300,150)

    # 移动窗口的
    w.move(300,300)

    # 设置窗口的标题
    w.setWindowTitle('第一个基于PyQt5的桌面应用')

    # 显示窗口
    w.show()

    # 进入程序的主循环 响应时间 通过exit函数确保主循环安全结束
    # 必须写
    sys.exit(app.exec_())

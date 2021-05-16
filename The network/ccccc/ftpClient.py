import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import os
from ftplib import FTP, all_errors
from PyQt5.QtGui import QIcon
import design  # Это наш конвертированный файл дизайна
import loginDesign

app_icon_path = os.path.join(os.path.dirname(__file__), 'icons')
qIcon = lambda name: QIcon(os.path.join(app_icon_path, name))


BACK_DIRECTORY = ' ..'
DIRECTORY_SEPARATOR = '/'


class LoginGUI(QtWidgets.QDialog, loginDesign.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)
        self.nameEdit.setEnabled(False)
        self.passEdit.setEnabled(False)
        self.pushButton.clicked.connect(self.close)
        self.visitorRadio.clicked.connect(self.disable_enter)
        self.registerRadio.clicked.connect(self.enable_enter)
        self.exec_()

    def disable_enter(self):
        self.nameEdit.setEnabled(False)
        self.passEdit.setEnabled(False)

    def enable_enter(self):
        self.nameEdit.setEnabled(True)
        self.passEdit.setEnabled(True)


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_local()
        self.ftp = FTP()
        self.local_pwd = 'local storage'
        self.remote_list = []   # список файлов текущего каталога
        self.remote_pwd = ''    # начальная удаленная директория
        self.pwd = ''           # текущая директория
        self.remote_path = []   # путь, начиная от начальноого каталога до текущего
        self.login_gui = None

    def create_local(self):
        """
        """
        self.connectButton.clicked.connect(self.connect)
        self.fileList.itemDoubleClicked.connect(self.click_item)
        self.uploadButton.clicked.connect(self.upload_file)

    def click_item(self, item, column):
        """
            обрабатывает клик по строке
        :param item: строка
        :param column: номер столбца
        :return:
        """
        header = self.fileList.headerItem()
        mode_i = 0
        for i in range(header.columnCount()):
            if header.text(i) == 'Mode':
                mode_i = i
                break
        content = item.text(mode_i)
        if column == 0:
            if content.startswith('d'):
                self.cd_to_dir(item.text(0))
            else:
                self.download_file(item.text(0))

    def cd_to_dir(self, dir_name):
        if dir_name == BACK_DIRECTORY:
            if self.pwd != self.remote_pwd:
                self.remote_path.pop()
                pathname = self.get_path()
            else:
                pathname = False
        else:
            self.remote_path.append(dir_name)
            pathname = self.get_path()

        if pathname:
            self.ftp.cwd(pathname)
            self.pwd = self.ftp.pwd()
            self.update_remote_list()

    def download_file(self, file_name):
        storage = self.local_pwd + DIRECTORY_SEPARATOR + file_name
        file = open(storage, 'wb')

        def callback(data):
            file.write(data)

        srcfile = self.get_path(file_name)

        self.ftp.set_pasv(True)
        try:
            self.ftp.retrbinary(cmd='RETR ' + srcfile, callback=callback)
        except Exception as error:
            print(error)

    def upload_file(self):
        pass

    def get_path(self, arr=""):
        """
            Формирует путь из массива каталгов
        :param arr:
        :return string:
        """
        if self.remote_path:
            pathname = ''
            for key in self.remote_path:
                pathname = os.path.join(pathname, key)
            if arr:
                pathname = os.path.join(pathname, arr)
            pathname = pathname.replace('\\', '/')
            return pathname
        else:
            return self.pwd

    def update_remote_list(self):
        self.fileList.clear()
        self.remote_list = []
        self.pwd = self.ftp.pwd()
        self.download_remote_list()

    def connect(self):
        """

        :return:
        """
        try:
            from urlparse import urlparse
        except ImportError:
            from urllib.parse import urlparse

        result = QtWidgets.QInputDialog.getText(self, 'Connect To Host', 'Host Address', QtWidgets.QLineEdit.Normal)
        if not result[1]:
            return
        try:
            host = str(result[0].toUtf8())
        except AttributeError:
            host = str(result[0])

        try:
            if urlparse(host).hostname:
                self.ftp.connect(host=urlparse(host).hostname, port=21, timeout=10)
            else:
                self.ftp.connect(host=host, port=21, timeout=10)
            self.login()
        except Exception as error:
            raise error

    def login(self):
        self.login_gui = LoginGUI()
        if self.login_gui.visitorRadio.isChecked():
            user = 'anonymous'
            passwd = 'anonymous'
        else:
            user = str(self.login_gui.nameEdit.text())
            passwd = str(self.login_gui.passEdit.text())
        self.ftp.user = user
        self.ftp.passwd = passwd
        self.ftp.login(user=user, passwd=passwd)
        self.initialize()

    def initialize(self):
        """
            обновляет список файлов и отображает его
        """
        self.remote_list = []
        self.pwd = self.ftp.pwd()
        self.remote_pwd = self.pwd
        self.remote_path.append(self.pwd)
        self.download_remote_list()

    def download_remote_list(self):
        item = QtWidgets.QTreeWidgetItem([BACK_DIRECTORY, '', '', '', '', 'd'])
        icon = qIcon('folder.png')
        item.setIcon(0, icon)
        self.remote_list.append(item)
        self.ftp.dir('.', self.add_item_to_file_list)
        for key in self.remote_list:
            self.fileList.addTopLevelItem(key)

    def add_item_to_file_list(self, content):
        mode, num, owner, group, size, date, filename = self.parse_file_info(content)
        if content.startswith('d'):
            icon = qIcon('folder.png')
        else:
            icon = qIcon('file.png')

        item = QtWidgets.QTreeWidgetItem([filename, size, owner, group, date, mode])
        item.setIcon(0, icon)
        self.remote_list.append(item)

    def parse_file_info(self, file):
        """
        parse files information "drwxr-xr-x 2 root wheel 1024 Nov 17 1993 lib" result like follower
                                "drwxr-xr-x", "2", "root", "wheel", "1024 Nov 17 1993", "lib"
        """
        item = [f for f in file.split(' ') if f != '']
        mode, num, owner, group, size, date, filename = (
            item[0], item[1], item[2], item[3], item[4], ' '.join(item[5:8]), ' '.join(item[8:]))
        return (mode, num, owner, group, size, date, filename)

    def home(self):
        pass

    def disconnect(self):
        try:
            self.ftp.quit()
        except all_errors:
            pass

    def __del__(self):
        self.disconnect()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

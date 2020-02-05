# -*- coding: utf-8 -*-
# author :HXM

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QMainWindow, QApplication, QWidget, Qt
import sys, math, requests, random, logging, qrcode
from lxml import etree


class Short_Url():

    def __init__(self, url, type):

        self.url = 'https://create.ft12.com/create.php?'

        self.data = {
            'url': url,
            'type': type,
            'random': 1184954713439208 + math.floor(2147483648 * random.random())
        }
        # 1184954713439208 +
        self.params = {
            'm': 'index',
            'a': 'urlCreate'
        }

    def shorted(self):

        responses = requests.post(url=self.url, params=self.params, data=self.data)

        if responses.status_code == 200:

            # print(responses.json().get('list'))

            return responses.json().get('list')

        else:
            logging.error("Fail")
            pass

    def get_user_agent(self):

        user_agent = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            " Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            " Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X ",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE",
        ]

        return random.choice(user_agent)


class Baidu_Url():

    def __init__(self, url):

        self.api = 'http://tool.pfan.cn/shorturl/create'

        self.data = {
            'url': url,
            'type': 'dwzcn',
        }

    def shorted(self):

        response = requests.post(url=self.api, data=self.data)

        try:
            if response.status_code == 200:
                # print(response.json())
                return response.json().get('shorturl')
        except Exception as e:

            logging.error(e)


class Sina_Url():

    def __init__(self, url):
        '''
        设置格式
        :param url:
        '''
        self.sina_url = 'https://www.98api.cn/api/sinaDwz.php'
        self.url = url

    def shorted(self):
        '''
        缩短链接
        :return:
        '''
        params = {
            'url': self.url
        }
        response = requests.get(url=self.sina_url, params=params)
        try:
            if response.status_code == 200:

                print(response.json())
                return response.json().get('short_url')

            else:
                logging.info('Fail')
        except Exception as e:
            logging.error(e)


class Tencent_url():
    '''
    暂时没有找到合适的接口,之前的接口已经失效
    '''
    def __init__(self, url):

        self.api = 'http://dwzapi.cccyun.cc/dwz.php'

        self.data = {
            'longurl': url,
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

            }

    def shorted(self):

        response = requests.post(url=self.api, data=self.data, headers=self.headers)
        if response.status_code == 200:
            print(response.json())
            return (response.json().get('ae_url'))

        else:
            strings = '不属于腾讯属下链接,请更换其他链接'
            return strings


class Ui_Form(object):
    '''
        主逻辑文件,已经设计好了,其实不用修改
        '''

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 500)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(Form)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_6 = QtWidgets.QRadioButton(Form)
        self.radioButton_6.setObjectName("radioButton_6")
        self.horizontalLayout_2.addWidget(self.radioButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.image = QtGui.QPixmap()
        self.palettes = QtGui.QPalette()
        self.clipboard = QtWidgets.QApplication.clipboard()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setWindowTitle(_translate("Form", "短链生成"))
        self.radioButton_4.setText(_translate("Form", "微博短链(推荐)"))
        self.radioButton_5.setText(_translate("Form", "百度短链(推荐)"))
        self.radioButton_3.setText(_translate("Form", "腾讯短链(推荐)"))
        self.radioButton.setText(_translate("Form", "u6.gg"))
        self.radioButton_6.setText(_translate("Form", "uee.me"))
        self.groupBox.setTitle(_translate("Form", "二维码"))
        self.pushButton.setText(_translate("Form", "生成"))
        self.pushButton_3.setText(_translate("Form", "二维码"))
        self.pushButton_2.setText(_translate("Form", "清空"))

        style = '''
                *{font: 14pt \"STKaiti\"}
                #groupBox {
                border-width:1.5px;   
                border-style:solid;
                border-color:lightGray;}  
                #pushButton{background-color:#3bb76d;color:#ffffff}
                #pushButton:hover{background-color:#119e49}
                #pushButton_2{background-color:#999;color:#ffffff}
                #pushButton_2:hover{background-color:#CDC9C9}
        '''
        Form.setStyleSheet(style)


class UI_Short(QWidget, Ui_Form):
    '''
    主源文件,要修改
    '''

    def __init__(self, parent=None):
        '''
        继承Ui_Form类
        :param parent:
        '''
        super(UI_Short, self).__init__(parent)
        self.setupUi(self)
        self.Init_UI()

    def Init_UI(self):
        '''
        优化界面
        :return:
        '''
        try:
            self.image.load('th.jpg')  # 设置背景图
            self.palettes.setBrush(self.backgroundRole(), QtGui.QBrush(self.image))
            self.setPalette(self.palettes)
            self.setAutoFillBackground(True)
            self.setWindowIcon(QtGui.QIcon('html.ico'))
            self.radioButton.toggled.connect(lambda: self.get_url(self.radioButton))
            self.pushButton.clicked.connect(lambda: self.short_url())
            self.pushButton_2.clicked.connect(lambda: self.clear())
            self.pushButton_3.clicked.connect(lambda: self.show_qrcode())
            self.radioButton_3.toggled.connect(lambda: self.get_url(self.radioButton_3))
            self.radioButton_4.toggled.connect(lambda: self.get_url(self.radioButton_4))

            self.radioButton_5.toggled.connect(lambda: self.get_url(self.radioButton_5))
            self.radioButton_6.toggled.connect(lambda: self.get_url(self.radioButton_6))
        except Exception as e:
            logging.error(e)
            pass

    def get_url(self, btn):
        '''
        获取按钮选择的短链类型
        :param btn:
        :return:
        '''
        try:
            if btn.isChecked() == True:
                print(btn.text())
                url_dict = {
                    '百度短链(推荐)': 'baidu',
                    '腾讯短链(推荐)': 'tencent',
                    '微博短链(推荐)': 'sina',
                    'u6.gg': 'u6',
                    'uee.me': 'uee'
                }
                self.trans_type = url_dict.get(btn.text())

        except Exception as e:

            logging.error(e)
            pass

    def short_url(self):
        '''
        判断短链类型
        并生成相应的结果
        :return:
        '''
        try:
            url = self.textEdit.toPlainText()
            if self.trans_type == 'baidu':
                short_url = Baidu_Url(url=url)
            elif self.trans_type == 'tencent':
                short_url = Tencent_url(url=url)
            elif self.trans_type == 'sina':
                short_url = Sina_Url(url=url)
            else:
                short_url = Short_Url(url=url, type=self.trans_type)
            self.url = short_url.shorted()
            self.textEdit.setText(self.url)
            self.clipboard.setText(self.url)

        except Exception as e:
            logging.error(e)
            pass

    def show_qrcode(self):
        '''
        展示二维码,其实是简单的二维码转码
        利用了qrcode库
        :return:
        '''
        try:
            self.label.setAlignment(Qt.AlignCenter)
            img = QtGui.QImage()  # 图片的自适应
            qrcodes = qrcode.make(self.url)
            qrcodes.save('code.png')
            if img.load('code.png'):
                # 自适应图片
                # self.label_4.setGeometry(0, 0, 400, 400)
                width = img.width()
                height = img.height()

                if width / 350 >= height / 350:
                    ratio = width / 350
                else:
                    ratio = height / 350
                new_width = width / ratio
                new_height = height / ratio
                new_img = img.scaled(new_width, new_height, Qt.KeepAspectRatio)
                self.label.setPixmap(QtGui.QPixmap.fromImage(new_img))
        except Exception as e:
            logging.error(e)

    def clear(self):
        '''
        清除链接和二维码
        :return:
        '''
        self.textEdit.clear()
        self.label.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = UI_Short()
    myWin.show()
    sys.exit(app.exec_())

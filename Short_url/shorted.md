


今天我在写文章的时候,碰到了一个问题,有个链接并没有备案,因此会导致微信的公众号后台无法保存自动回复,所以我上网查了查,好像短链接可以通过微信的防红链接检测,所以我想了想,决定着手开发一个短链接生成器,方便我以后的操作。下面是作品:

![1sEqfA.png](https://s2.ax1x.com/2020/02/05/1sEqfA.png)

### 设计流程

- [x] 设计界面`PyQt5`的`Qtdesigner`

- [x] 简单的网络通信系统`requests库`

- [x] 优化界面以及底层逻辑函数

- [x] 尽可能实现方便化


### 设计界面

首先需要明确我们的程序需要什么样的功能

- 输入网址
- 选择链接类型
- 转换链接,生成后自动复制系统剪切板
- 可以提供二维码形式

这个,我们首先来确定各个组件的摆放位置,这个其实也就是手动就可以完成的了,一个是文本控件,一个是按钮筛选`radio Button`,还有生成按钮`pushButton`,一个标签控件即可,确定这些之后,然后在`Qt designer`上的模板图进行拖放,设置大小即可。

![1sETTe.png](https://s2.ax1x.com/2020/02/05/1sETTe.png)
选择设计界面好后,直接保存,然后用`pycharm`配置好的`pyuic`直接转换为`python`源文件即可,由于使用了网格布局,所以无需考虑各个控件的大小形式,只要做好底层各个控件之间的连接通信即可,窗口代码大致如下:

![1sVPYj.jpg](https://s2.ax1x.com/2020/02/05/1sVPYj.jpg)

### 简单的网络通信

虽然现在我们已经提供了最初的设计界面,但是,我们还要实现如何让底层源代码与UI界面结合在一起,也就是说:当我输入一串网址的时候,点击生成,就会有新的网址生成,并展示在前端,还可以随心所欲的转换短链的类型,比如百度短链,新浪短链等。

![1sEvOf.png](https://s2.ax1x.com/2020/02/05/1sEvOf.png)

这样的话,我们为了简单一点通信,直接使用单线程请求短链的生成接口即可,然后后端服务会返回缩短后的链接,再经过简单的提取处理,就能展示在前端界面上了,这里我使用的是`requests`库,毕竟相信大伙有对爬虫进行了解,`requests`库还是蛮好用的。关键的程序大致如下:
```Python

class Sina_Url():

    def __init__(self, url):
        '''
        设置格式
        :param url:
        '''
        self.sina_url='https://www.98api.cn/api/sinaDwz.php'
        self.url=url


    def shorted(self):
        '''
        缩短链接
        :return:
        '''
        params={
            'url':self.url
        }
        response=requests.get(url=self.sina_url,params=params)
        try:
            if response.status_code == 200:

                print(response.json())
                return response.json().get('short_url')

            else:
                logging.info('Fail')
        except Exception as e:
            logging.error(e)

```
关键请求程序中,`shorted`函数中就是请求返回短链接结果,`self.url`即是你想要缩短的长链接,这样我们只需要提供我们需要生成的网址即可获取到我们想要的结果,由于接口原因,可能生成有点慢,不过不要介意,我的函数里还提供了几种短链类型的生成函数,以致于方便我随时切换短链类型,来满足我的需求。


### 优化界面逻辑

这里,我就已经大概完成了网络请求以及设计界面基础模型,接下来,我们要开始着手对设计界面和源代码进行相应的底层关联结合,以及美化一下设计界面的模型和字体。
之前生成的界面源代码有两大类:`Ui_Form`和`UI_Short`,`Ui_Form`是已经生成好的界面代码,其实就是各个控件之间的简单布局,我们这里就不用修改,我们要修改结合的是`UI_Short`这个类,`UI_Short`里面有`__init__`初始化参数,这里我仅仅只是用于继承`UI_From`设计界面而已,`Init_UI`函数才是相关的关联函数,如下

![1sEXlt.png](https://s2.ax1x.com/2020/02/05/1sEXlt.png)

`Init_UI`函数大致如下,主要功能是关联按钮以及文本文件的操作功能,主要代码如下:
```Python

    def Init_UI(self):
        '''
        优化界面
        :return:
        '''
        try:
            self.image.load('th.jpg')   #设置背景图
            self.palettes.setBrush(self.backgroundRole(),QtGui.QBrush(self.image))
            self.setPalette(self.palettes)
            self.setAutoFillBackground(True)
            self.setWindowIcon(QtGui.QIcon('html.ico'))
            self.radioButton.toggled.connect(lambda: self.get_url(self.radioButton))        #类型选择按钮连接
            self.pushButton.clicked.connect(lambda: self.short_url())
            self.pushButton_2.clicked.connect(lambda: self.clear())
            self.pushButton_3.clicked.connect(lambda: self.show_qrcode())
            # self.radioButton_3.toggled.connect(lambda: self.get_url(self.radioButton_3))
            self.radioButton_4.toggled.connect(lambda: self.get_url(self.radioButton_4))
            self.radioButton_5.toggled.connect(lambda: self.get_url(self.radioButton_5))
            self.radioButton_6.toggled.connect(lambda: self.get_url(self.radioButton_6))
        except Exception as e:
            logging.error(e)
            pass
```
接下来的函数,主要是判断短链类型的函数,以及显示结果函数,如下:
- 判断选择短链类型

![1sVS0S.jpg](https://s2.ax1x.com/2020/02/05/1sVS0S.jpg)

- 显示结果类型

>我们记得关联上之前写过的接口请求,直接调用那个接口返回的结果,用文本控件显示操作`setText`结果即可,这里,我为了方便,直接将结果复制到系统剪切板上,生成链接的同时已经复制好了,节约时间。

![1sEzm8.jpg](https://s2.ax1x.com/2020/02/05/1sEzm8.jpg)


- 最后也要写上清除函数,为了方便链接的清除和二维码的清除。

![1sVCkQ.png](https://s2.ax1x.com/2020/02/05/1sVCkQ.png)

## 新功能拓展

这里,为了我的工具更加好用,我直接生成成二维码形式的话,微信后台检测的风险性就更加大大降低了,所以,我这里用了qrcode库,将链接转码为二维码形式,便于生成二维码。主要代码:
```Python

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
            qrcodes.save('code.png')#保存文件在本地的code.png
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

```

## 总结一下

虽然看似这些过程略微简单一些,但是,我从中修改了很多错误,也学习到了很多新知识,并且对于版本的修改也进行了几次,可以说使我受益匪浅,大伙也可以尝试去实现一下我的代码,能自己写一个比较好用的小程序还是挺有成绩感的。

## 源代码

你要是觉得文章写的不错,就star本项目一下呗。

- [源代码传送门]()

- [成品下载](https://www.lanzous.com/i8xmwid)

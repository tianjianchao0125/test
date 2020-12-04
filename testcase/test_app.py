import os
import time
import  unittest

from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium import webdriver

class MyTests(unittest.TestCase):
    # 测试开始前执行的方法
    def setUp(self) -> None:
        desired_caps = {
            'platformName': 'Android',  # 被测手机是安卓
            'platformVersion': '7',  # 手机安卓版本
            'deviceName': 'TAS-AN00',  # 设备名，安卓手机可以随意填写
            'appPackage': 'com.tencent.mm',  # 启动APP Package名称
            'appActivity': '.ui.LauncherUI',  # 启动Activity名称
            'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
            'resetKeyboard': True,  # 执行完程序恢复原来输入法
            'noReset': True,  # 不要重置App
            'newCommandTimeout': 6000,
            'automationName': 'UiAutomator2'
            # 'app': r'd:\apk\bili.apk',
        }

        # 连接appium server 初始化自动化环境
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # 设置缺省等待时间
        self.driver.implicitly_wait(20)

    def test_wxapp(self):
        '''微信小程序测试'''
        time.sleep(3)
        # 获取屏幕的宽，高
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        # 点击文件传输助手
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("文件传输助手")').click()
        # 点击中国移动小程序
        self.driver.find_element_by_id('com.tencent.mm:id/ajh').click()
        time.sleep(2)
        # 假如没有登录让他先登录




        # 等待页面加载
        # 点击左上角分类icon
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.widget.Image[2]').click()
        # 选择职位类别 综合类
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("综合类")').click()
        # 职位列表：
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("人力资源")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("工会管理")').click()
        self.driver.swipe(21, 749, 21, 1, 800)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("采购管理")').click()
        # 点击返回左侧
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[15]/android.widget.Image').click()
        time.sleep(6)
        # 点击轮播图
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View').click()
        # 点击
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("走进移动")').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("欢迎信")').click()
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("走进移动")').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("时光回顾")').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("招聘大厅")').click()
        # 出现一个温馨提示  点击右上角小x号
        time.sleep(1)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View[2]/android.view.View[3]').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("云端宣讲")').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("空中双选")').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("空中双选")').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("就业微课")').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("媒体播报")').click()
        time.sleep(2)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout').click()
        time.sleep(2)
        # 点击招聘公告
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[6]/android.widget.Image').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        print('111111')
        # 点击热门职位 技术工程师
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[9]/android.view.View[1]').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("公司详情")').click()
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.widget.Image').click()
        time.sleep(1)
        # 从热门职位  让他往下滑
        self.driver.swipe(42, 783, 42, 1, 1000)
        # 点击底部 社会招聘
        print('首页执行完了~~~')
        time.sleep(1)
        print('点击社会招聘页')
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("社会招聘")').click()
        # 点击职位
        time.sleep(1)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[7]/android.view.View[1]/android.view.View[1]').click()
        time.sleep(1)
        self.driver.swipe(42, 811, 42, 0, 1000)
        # 滑动最底部 看到任职条件
        self.driver.swipe(42, 774, 42, 0, 1000)
        # **************************************************************************************************************
        # 点击收藏
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout[1]').click()
        time.sleep(1)
        # 点击分享职位
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout[2]').click()
        # 分享给***
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("田建朝")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("发送")').click()  # 点击发送
        self.driver.swipe(21, 126, 21, 900, 1000)
        self.driver.swipe(21, 126, 21, 950, 1000)  # 向上滑动顶部
        # 点击公司详情
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.widget.Image').click()
        time.sleep(2)
        # 向下滑动，看某些职位信息是否显示出来
        self.driver.swipe(21, 930, 21, 100, 800)
        self.driver.swipe(21, 882, 21, 80, 800)
        self.driver.swipe(21, 882, 21, 30, 1500)
        # 选择一条职位信息，点击进行查看
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View[1]').click()
        # 从岗位描述进行下滑
        time.sleep(1)
        self.driver.swipe(21, 707, 21, 10, 1000)
        self.driver.swipe(46, 661, 46, 1, 1000)
        # 上滑 看到返回键 点击返回
        self.driver.swipe(21, 126, 21, 900, 1000)
        self.driver.swipe(21, 126, 21, 950, 1000)  # 向上滑动顶部
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.widget.Image').click()
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.widget.Image').click()
        # 切换一下地区  点击下三角
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View').click()
        # 选择上海
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("上海")').click()
        self.driver.swipe(180, 644, 180, 200, 1000)  # 向下滑动 看下面的地区信息
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[7]/android.view.View[3]/android.view.View[2]/android.view.View[10]').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[11]/android.view.View[3]/android.view.View[2]/android.view.View[10]').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View').click()
        # 点击全部 查看全部信息
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[7]/android.view.View[3]/android.view.View[1]/android.view.View[1]').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[7]/android.view.View[3]/android.view.View[2]/android.view.View').click()
        print('地区信息查看完毕')
        # 点击发布日期
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[5]/android.view.View').click()
        # 进行向上滑动选择全部
        time.sleep(0.5)
        self.driver.swipe(0, 524, 0, 822, 1000)
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[6]/android.view.View[1]/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]').click()
        # 点击确定
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
        print('发布日期查看完毕')
        # 点击筛选
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[6]/android.view.View').click()
        # 工作经验选择不限
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("不限")').click()
        time.sleep(1)
        self.driver.swipe(0, 704, 0, 500, 800)  # 让屏幕向下滑动
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("全部")').click()
        self.driver.swipe(0, 746, 0, 200, 1000)  # 让屏幕向下滑动
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("全职")').click()
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("确认")').click()
        # 让屏幕向下滑动 看职位信息
        self.driver.swipe(42, 728, 42, 200, 1000)
        self.driver.swipe(42, 797, 42, 10, 1000)
        self.driver.swipe(42, 839, 42, 1, 1000)
        self.driver.swipe(42, 839, 42, 0, 1000)
        print('社会招聘页执行完了~~')
        print('点击校园招聘')
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("校园招聘")').click()
        # 　进入页面　点击集团总部
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View/android.view.View').click()
        time.sleep(2)
        time.sleep(2)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[6]/android.view.View').click()
        self.driver.swipe(251, 796, 251, 300, 800)
        # 点击返回退出
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        # 省公司
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("北京公司")').click()
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("天津公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("河北公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("山西公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("内蒙古公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("辽宁公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("吉林公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("黑龙江公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("上海公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("江苏公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("浙江公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("安徽公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("福建公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("江西公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("山东公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        # 让屏幕下滑
        time.sleep(2)
        self.driver.swipe(58,840,58,300,1000)
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("河南公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("湖北公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("湖南公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("广东公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("广西公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("海南公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("重庆公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("四川公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("贵州公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("云南公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("西藏公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("陕西公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("甘肃公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("青海公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("宁夏公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("新疆公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()

        # ***********  专业公司  **********
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("铁通公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("设计院")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("国际公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("终端公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("政企事业部")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("财务公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("物联网公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("云能力中心")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        time.sleep(1)
        self.driver.swipe(48,802,48,300, 1000)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("杭州研发中心（智慧家庭运营中心）")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("在线服务公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("咪咕公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("互联网公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("投资公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("成都产业研究院")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("上海产业研究院")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("金融科技公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("中移系统集成（雄安产业研究院）")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        # ************** 直属单位 ***************
        time.sleep(1)
        self.driver.swipe(21, 640, 21, 1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("研究院")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("中国移动学院")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("信息港中心")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("采购共享中心")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("信息技术中心")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("信安中心")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("销售分公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        # ************** 境外及其他 **********
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("香港公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("辛姆巴科公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("香港机构")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("卓望公司")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("中移智行")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("位置服务中心")').click()
        time.sleep(1)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout').click()
        print('校园招聘查看完毕！')
        time.sleep(1)
        print('点击实习生招聘')
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("实习生招聘")').click()
        time.sleep(1)
        # 切换一下地区  点击下三角
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View').click()
        # 选择上海
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("北京")').click()
        time.sleep(1)
        self.driver.swipe(180, 644, 180, 200, 1000)  # 向下滑动 看下面的地区信息
        # 点击选择 区域
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[9]/android.view.View[3]/android.view.View[2]/android.view.View[10]').click()
        # 点击出现全部
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View').click()
        # 点击全部 查看全部信息
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[7]/android.view.View[3]/android.view.View[1]/android.view.View[1]').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[7]/android.view.View[3]/android.view.View[2]/android.view.View').click()
        print('地区信息查看完毕')
        time.sleep(2)
        # 点击发布日期
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[5]/android.view.View').click()
        # 进行向上滑动选择全部
        time.sleep(0.5)
        self.driver.swipe(0,524,0,822,1000)
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[6]/android.view.View[1]/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]').click()
        # 点击确定
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
        print('发布日期查看完毕')
        # 点击筛选
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[6]/android.view.View').click()
        # 点击全部
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("全部")').click()
        time.sleep(0.5)
        # 工作职位类别
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("技术类")').click()
        # 点击确定
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("确认")').click()
        # 点击职位 查看职位详细信息
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[7]/android.view.View[1]/android.view.View[1]').click()
        # 屏幕进行滑动，看下面详细信息
        time.sleep(1)
        self.driver.swipe(21,806,21,1,1000)
        self.driver.swipe(21,692,21,1,1000)
        time.sleep(0.5)
        # 点击分享职位
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout[2]').click()
        # 分享给***
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("田建朝")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("发送")').click()  # 点击发送
        # 点击投个简历
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("投个简历")').click()
        time.sleep(2)
        print('投递简历成功')
        # 向上滑  看到返回键，点击返回键
        time.sleep(1)
        self.driver.swipe(21,601,21,800,1000)
        time.sleep(1)
        self.driver.swipe(21,180,21,600,1000)
        self.driver.swipe(21,162,21,900,1000)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.widget.Image').click()
        print('实习生招聘页执行完毕~~~~')
        time.sleep(1)
        print('点击个人中心')
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
        # 点击我的简历，进入简历信息
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的简历")').click()
        time.sleep(2)
        # 点击实习生简历
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[6]').click()
        time.sleep(4)
        # 点击预览
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("预览")').click()
        # 进入简历基础信息   点击联系方式
        time.sleep(2)
        # # 点击修改
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("修改")').click()
        # # 选择年龄  清空
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[5]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[5]').clear()
        #



        self.driver.find_element_by_android_uiautomator('new UiSelector().text("联系方式")').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("教育经历")').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("在校活动奖励")').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("自我评价")').click()
        # 点击返回
        time.sleep(1)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.widget.Image').click()
        # 来到实习生简历页面  点击一个基础信息进行查看
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]').click()
        time.sleep(0.5)
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.widget.Image').click()
        # 在点击返回
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.widget.Image').click()
        # 在点击返回
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.widget.Image').click()
        # 点击我的收藏
        time.sleep(0.5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的收藏")').click()
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.widget.Image').click()
        # 点击我的申请
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的申请")').click()
        # 点击查看
        time.sleep(0.5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("查看")').click()
        # 让手机往下滑
        self.driver.swipe(21,457,21,10,800)
        # 点击查看公司详情
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]').click()
        # 点击返回
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.widget.Image').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.widget.Image').click()
        time.sleep(5)

        print('执行完毕，无报错~~~~')

        # 测试结束后执行的方法
        def tearDown(self) -> None:
            self.driver.quit()





if __name__ == '__main__':
    unittest.main()




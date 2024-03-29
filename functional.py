from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        #张三听说有一个在线待办事项的应用
        #他去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        #他注意到网页里包含“To-Do"这个词
        self.assertIn('To-Do' in browser.title), "browser title was:" + self.browser.title
        self.fail('Finish the test!')
        #应用有一个输入代办事项的文本输入框
        #他在文本输入框中输入了“buy flowers"
        # 她按了回车键后，页面更新了
        # 待办事项表格中显示了"1: Buy flowers"

        # 页面中又显示了一个文本框，可以输入其她待办事项
        # 她输入了"Send a gift to Chenzhuhao"

        # 页面再次更新，她的清单中显示了这两个待办事项

        # 韩烨想知道这个网站是否会记住她的清单
        # 她看到网站为她生成了一个唯一的URL

        # 她访问这个URL，发现她的待办事项列表还在
        # 她很满意地离开了
if __name__== '__main__':
    unittest.main()
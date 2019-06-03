from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
import time


USERNAME = '17761864285'
PASSWORD = '879662581'
BORDER = 6

class Login(object):
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.username = USERNAME
        self.password = PASSWORD
        self.wait = WebDriverWait(self.browser, 10)

    def __del__(self):
        self.browser.close()

    def open(self):
        self.browser.get('https://www.jianshu.com/')
        login = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="btn log-in"]')))
        login.click()
        time.sleep(10)

        username = self.wait.until(EC.presence_of_element_located((By.ID, 'session_email_or_mobile_number')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'session_password')))
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)

    def click_button(self):
        '''
        点击按钮呼出验证码图片
        '''

        # button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'sign-in-button')))

        button.click()


    def get_captcha(self,name='captcha.png'):
        '''
        截图并且按照验证码图片的位置进行抠图
        '''
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        print('验证码图片位置是：', location)
        print('验证码图片尺寸是：', size)
        top,bottom,left,right = location['y'], location['y']+size['height'], location['x'], location['x']+size['width']

        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)


    def get_slider(self):
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider


    def get_gap(self, captcha1, captcha2):
        '''
        左边部分一定存在差异，因此直接忽略
        '''
        left = 60
        for i in range(left,captcha1.size[0]):  # captcha1.size宽度和高度的元组
            for j in range(captcha1.size[1]):
                if not self.is_pixel_equal(captcha1, captcha2, i, j):
                    left = i
                    return left
        return left

    def is_pixel_equal(self, captcha1, captcha2, x, y):
        '''
        对每个像素的RGB值进行比较
        '''
        pixel1 = captcha1.load()[x, y]
        pixel2 = captcha2.load()[x, y]
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel2[1] - pixel2[1]) < threshold and \
           abs(pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def get_track(self, distance):
        track = []
        current = 0
        mid = distance*4/5
        t = 0.2
        v = 0
        while current < distance:
            if current < mid:
                a = 10
            else:
                a = -18
            v0 = v
            v = v0 + a * t
            move = v0 * t + 1 / 2 * a * t * t
            current += move
            track.append(round(move))
        return track

    def move_to_gap(self, slider, track):
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0)
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()

    def loginin(self):
        submit = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'commit')))
        submit.click()
        time.sleep(5)
        print('登陆成功')

    def crack(self):
        self.open()
        self.click_button()  # 点击按钮呼出验证码图片
        captcha1 = self.get_captcha('captcha1.png')  # 截图，获取原始验证码位置，抠图

        slider = self.get_slider()   # 获取验证码滑块位置
        slider.click()  # 点击位置
        captcha2 = self.get_captcha('captcha2.png')  # 截图，获取凹凸验证码位置，抠图

        gap = self.get_gap(captcha1, captcha2)       # 图片对比，距离
        gap -= BORDER                                # 减去左边的边框距离
        track = self.get_track(gap)                  # 获取移动轨迹

        print('滑动轨迹', track)

        self.move_to_gap(slider, track)
        success = self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_success_radar_tip_content'), '验证成功'))
        print(success)

        time.sleep(0.5)
        self.loginin()
        # if not success:
        #     self.crack()
        # else:
        #     self.login()

if __name__ == '__main__':
    crack = Login()
    crack.crack()

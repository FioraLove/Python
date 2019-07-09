import re,time,csv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from pymongo import MongoClient
import pymongo


MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_TABLE = 'product'

#SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']

KEYWORD = '美食'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

browser = webdriver.Chrome()
#browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
wait = WebDriverWait(browser, 20)

#browser.set_window_size(1400, 900)
headers={
            'Cookie':'cna=gPweE1BGd1ACAd/XieK1Ynjn; t=8b79d2c1559d044c0f700ed409d4817e; _m_h5_tk=a174fd9294c39b5e3be7fdfd11667ebd_1562643793321; _m_h5_tk_enc=49d2f732683fd0d9422d39217667e330; thw=cn; v=0; cookie2=1bfa81beaa141cba9c496d7cd81f7552; _tb_token_=75a3b5b7e7195; unb=2352423317; sg=07a; _l_g_=Ug%3D%3D; skt=82fb8b51968be0bf; cookie1=BxT7dJgxZCK1kJs8RPI6nj%2Fyx3wCLQvJPMz%2B93t6ynU%3D; csg=5560dadd; uc3=vt3=F8dBy3%2F6%2BQXKAbsdeKE%3D&id2=UUtO%2Bptqfajwdg%3D%3D&nk2=0PK8qIP%2BLRI%3D&lg2=URm48syIIVrSKA%3D%3D; existShop=MTU2MjYzNjYyMw%3D%3D; tracknick=%5Cu9648%5Cu6D69%5Cu4E1C80; lgc=%5Cu9648%5Cu6D69%5Cu4E1C80; _cc_=VFC%2FuZ9ajQ%3D%3D; dnk=%5Cu9648%5Cu6D69%5Cu4E1C80; _nk_=%5Cu9648%5Cu6D69%5Cu4E1C80; cookie17=UUtO%2Bptqfajwdg%3D%3D; tg=0; enc=hwY1K%2FjOT0%2F246f2VKVpwc0Uc2egItAL50O5YhujIqFs2ZdOmKULjsSGfc2SdvFDznEOvAtWPD9UcfALoxDdvg%3D%3D; _uab_collina=156263660733566676336021; x5sec=7b227365617263686170703b32223a226432306331373435636532336361646266353363316538653030623164343338434d2f696a2b6b46454f446f75595479774c6d4262426f4d4d6a4d314d6a51794d7a4d784e7a7378227d; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=URm48syIYB3rzvI4Dim4&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&pas=0&cookie14=UoTaGqtNSH9s%2BQ%3D%3D&tag=8&lng=zh_CN; mt=ci=24_1; swfstore=141038; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; JSESSIONID=6F0514F7075A208F93BF2C311B8C41C3; l=bBjFzqicv7CkB_yoBOfBqQKbYE_9qIRb8RFP2N-MFICP9DfHxuVcWZnD38LMC3hVZ1rJR3PGap0LBeV9qyCN.; isg=BJWVwjKKZPdyL0HDBpS2d1T7pJHjgkqyJYuR4xc6lIx3brdg3-HpdNdkOTL9t2Fc; whl=-1%260%260%261562636764179',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        }
def search():
    print('正在搜索')
    try:
        browser.get('https://www.taobao.com')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        input.send_keys(KEYWORD)
        submit.click()
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return total.text
    except TimeoutException:
        return search()


def next_page(page_number):
    print('正在翻页', page_number)
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
        get_products()
    except TimeoutException:
        next_page(page_number)


def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    # try:
    #     if db[MONGO_TABLE].insert(result):
    #         print('存储到MONGODB成功', result)
    # except Exception:
    #     print('存储到MONGODB失败', result)
    with open('taobao.csv','a+',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(result)



def main():
    try:
        total = search()
        total = int(re.compile('(\d+)').search(total).group(1))
        for i in range(2, total + 1):
            time.sleep(10)
            next_page(i)
    except Exception:
        print('出错啦')
    finally:
        browser.close()

if __name__ == '__main__':
    main()

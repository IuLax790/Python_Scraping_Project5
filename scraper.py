from selenium import webdriver
from lxml import html
from time import sleep
driver = webdriver.Chrome("C:/Program Files/Google/Chrome/chromedriver")

for page_nb in range(1,10):
    driver.get('https://www.aliexpress.com/w/wholesale-bike.html?catId=0&initiative_id=SB_20230110131150&SearchText=bike&spm=a2g0o.home.1000002.0&dida=y')
    sleep(1)
    tree = html.fromstring(driver.page_source)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(1)
    for product_tree in tree.xpath('//li[@class="list-item"]'):
        title = product_tree.xpath('.//a[@class="item-title"]/@title')
        price = product_tree.xpath('.//span[@class="price-current"]/text()')
        review = product_tree.xpath('.//span[@class="rating-value"]/text()')
        nb_sold = product_tree.xpath('.//a[@class="sale-value-link"]/text()')
        print(title,price,review,nb_sold)
    print("\n\n\n\n\n\n")

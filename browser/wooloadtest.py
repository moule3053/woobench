from locust import Locust, HttpLocust, TaskSet, task
import string
import random
import time
from locust.web import app

#from src import report

# For reporting
app.add_url_rule('/htmlreport', 'htmlreport')

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        #self.comment()

    @task(1)
    def comment(self):
        from splinter import Browser

        with Browser('phantomjs') as browser:
#            foo = ['70', '37', '53', '31', '56', '50' , '19', '73', '76', '93', '99', '47', '34', '79', '60', '15', '96', '90', '87', '83', '67']
            foo = ['26','27','99','96','93','90','87','83','79','117','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116']
            #foo = ['']
	# Visit URL
            url = WebsiteUser.host + "/shop/?add-to-cart=" + random.choice(foo)
            browser.visit(url)
            url = WebsiteUser.host + "/checkout/"
            #print(url)
            browser.visit(url)
            browser.fill('billing_first_name', 'Vanessa')
            browser.fill('billing_last_name', 'Michaels')
            browser.fill('billing_address_1', 'Storkower Strasse 223')
            browser.fill('billing_postcode', '10367')
            browser.fill('billing_city', 'Berlin')
            browser.fill('billing_email', 'hello@dfdf.dfdfdfdf')
#            browser.find_by_name('woocommerce_checkout_place_order').first.click()

    # Find and click the 'Place Order' button
            button = browser.find_by_name('woocommerce_checkout_place_order')
    # Interact with elements
            button.first.click()


	    browser.quit()
class WebsiteUser(HttpLocust):
    host = "http://35.198.133.209/"
    weight = 1
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000

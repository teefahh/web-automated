from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time




class AfbLogin:
    def __init__(self, username, password, SecurityQuestion):
        self.username = username
        self.password = password
        self.SecurityQuestion = SecurityQuestion

        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        self.driver.get('https://business.alat.ng/')
        self.driver.maximize_window()


    def login(self):

        username_element = self.driver.find_element_by_id('input_0')
        username_element.send_keys(self.username)

        password_element = self.driver.find_element_by_id('input_1')
        password_element.send_keys(self.password)

        continue_button = self.driver.find_element_by_xpath('// button[text() = "Continue"]')
        continue_button.click()

        page_title = self.driver.title
        assert page_title == "ALAT for Business"

        SecurityQuestion_element = WebDriverWait(self.driver, 300).until(ec.element_to_be_clickable((By.ID, 'input_2')))
        SecurityQuestion_element.send_keys(self.SecurityQuestion)

        login_button = self.driver.find_element_by_xpath('// button[text() = "Sign in"]')
        login_button.click()

        CompanyName = WebDriverWait(self.driver, 300).until(ec.presence_of_element_located((By.XPATH, '//h4[@ng-bind="overview.Dashboard.Profile.CompanyName"]'))).text

        if CompanyName != "":
            print(CompanyName)
            FundsTransfer_element = WebDriverWait(self.driver, 500).until(ec.presence_of_element_located((By.LINK_TEXT, 'Funds Transfer (Naira)')))
            FundsTransfer_element.click()

            dropdown = self.driver.find_element_by_id('select_4')
            optionn = dropdown.find_elements_by_tag_name('md-option')
            number_of_accounts = len(optionn) - 1
            position_of_acct_to_click = 35
            transfer_option = 35

            for option in optionn:
                print(number_of_accounts)
                account_dropdwn = WebDriverWait(self.driver, 500).until(ec.element_to_be_clickable((By.ID, "select_4")))
                account_dropdwn.click()

                account_dropdwn_a = WebDriverWait(self.driver, 500).until(ec.element_to_be_clickable((By.ID, "select_option_" + str(position_of_acct_to_click))))
                account_dropdwn_a.click()

                Available_amount = WebDriverWait(self.driver, 500).until(ec.presence_of_element_located(
                    (By.XPATH, '//span[@ng-bind="trans.AccountMandate.Account.AvailableBalance | number:2"]'))).text

                x = str(Available_amount)

                x = x.replace(',', '')

                def Transfer_tab():
                    print(number_of_accounts)
                    if number_of_accounts > 1:
                        print('method')
                        select_account = WebDriverWait(self.driver, 800).until(
                            ec.element_to_be_clickable((By.ID, "accNo")))
                        select_account.click()
                        destination_bank = WebDriverWait(self.driver, 800).until(
                            ec.element_to_be_clickable((By.ID, "select_option_" + str(transfer_option + number_of_accounts))))
                        destination_bank.click()

                        description_element = self.driver.find_element_by_id('input_179')
                        description_element.send_keys('Transfer 1 billion')

                        amount_element = self.driver.find_element_by_id('input_12')
                        amount_element.send_keys(str(10.00))
                        time.sleep(20)

                        proceed_button = self.driver.find_element_by_id('btnOwnStart')
                        proceed_button.click()
                        time.sleep(20)

                        confirm_element =  WebDriverWait(self.driver, 800).until(
                            ec.element_((By.ID, "select_option_" + str(transfer_option + number_of_accounts))))
                        destination_bank.click()







                if float(x) > 200.0:
                    print('iffff')
                    Transfer_tab()
                    position_of_acct_to_click+=1
                    print('Successful')







                number_of_accounts += 1




            Available_amount = WebDriverWait(self.driver, 500).until(ec.presence_of_element_located((By.XPATH, '//span[@ng-bind="trans.AccountMandate.Account.AvailableBalance | number:2"]'))).text

            x = str(Available_amount)

            x = x.replace(',', '')
            # float(x)

            print(x)

            def Transfer_tab():
                if number_of_accounts > 2:
                    select_account = WebDriverWait(self.driver, 500).until(ec.element_to_be_clickable((By.ID, "accNo")))
                    select_account.click()
                    destination_bank = WebDriverWait(self.driver, 500).until(ec.element_to_be_clickable((By.ID, "select_value_label_10")))
                    destination_bank.click()

            if float(x) > 200.0:
                Transfer_tab()
                print('Successful')

            # account_dropdwn = WebDriverWait(self.driver, 500).until(ec.element_to_be_clickable((By.ID, "select_4")))
            # account_dropdwn.click()

            # for index in range(0, len(options)):
            #     select.select_by_index(index)

            # account_dropdwn = WebDriverWait(self.driver, 500).until(ec.element_to_be_clickable((By.ID, "select_4")))
            # account_dropdwn.click()
            # account_dropdwn_a = WebDriverWait(self.driver, 500).until(ec.element_to_be_clickable((By.ID, "select_option_36")))
            # account_dropdwn_a.click()
            # account_dropdwn = WebDriverWait(self.driver, 500).until(ec.element_to_be_clickable((By.ID, "select_4")))
            # account_dropdwn.click()
            # account_dropdwn_b = WebDriverWait(self.driver, 500).until(ec.element_to_be_clickable((By.ID, "select_option_37")))
            # account_dropdwn_b.click()















if __name__ == '__main__':

    AFB_login = AfbLogin(username='admin', password='admin', SecurityQuestion='admin')
    AFB_login.login()






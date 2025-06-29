# import time
# import imaplib
# import email
# from bs4 import BeautifulSoup
# import re
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC


# def get_sagasoft_otp(since_time):
#     username = "abitha@sagasoft.io"
#     password = "Abitha@123"
#     imap_server = "mail.sagasoft.io"
#     sender_email = "support@sagasoft.io"

#     mail = imaplib.IMAP4_SSL(imap_server)
#     mail.login(username, password)
#     mail.select("inbox")

#     timeout = 120
#     interval = 5
#     end_time = time.time() + timeout

#     while time.time() < end_time:
#         since_date = time.strftime('%d-%b-%Y', time.localtime(since_time))
#         criteria = f'(FROM "{sender_email}" SINCE {since_date})'
#         result, data = mail.search(None, criteria)
#         mail_ids = data[0].split()

#         if mail_ids:
#             for email_id in reversed(mail_ids):
#                 result, msg_data = mail.fetch(email_id, "(RFC822)")
#                 raw_email = msg_data[0][1]
#                 msg = email.message_from_bytes(raw_email)

#                 email_date = msg.get('Date')
#                 email_timestamp = email.utils.mktime_tz(email.utils.parsedate_tz(email_date))
#                 if email_timestamp < since_time:
#                     continue

#                 for part in msg.walk():
#                     if part.get_content_type() == "text/html":
#                         body = part.get_payload(decode=True).decode()
#                         soup = BeautifulSoup(body, "html.parser")
#                         text = soup.get_text()

#                         match = re.search(r'\b\d{6}\b', text)
#                         if match:
#                             mail.logout()
#                             return match.group()
#         time.sleep(interval)

#     mail.logout()
#     return None


# def main():
#     driver = webdriver.Chrome()
#     driver.get("https://signup-qa1.sagasoft.xyz/")
#     driver.maximize_window()
#     time.sleep(1)

#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "company"))).send_keys("sagasoft")
#     time.sleep(1)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "site"))).send_keys("tech1")
#     time.sleep(1)

#     Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "employee")))).select_by_visible_text("1 - 10")
#     time.sleep(1)

#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys("abitha@sagasoft.io")
#     time.sleep(1)

#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input-group-dropdown-2"))).click()
#     time.sleep(1)

#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/form/div[5]/div/div[1]/div/a[1]"))).click()
#     time.sleep(1)

#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mobile"))).send_keys("8489716029")
#     time.sleep(1)

#     industry_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "industry")))
#     industry_dropdown.click()
#     Select(industry_dropdown).select_by_visible_text("Technology & Software")
#     time.sleep(2)

#     Signup_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "SignupButton")))
#     Signup_Button.click()
#     print("Signup successfully")

#     # Get current time after clicking signup
#     otp_start_time = time.time()
#     time.sleep(2)  # short wait

#     driver.execute_script("window.open('');")
#     driver.switch_to.window(driver.window_handles[1])
#     driver.get("https://signup-qa1.sagasoft.xyz/verify?method=email")
#     time.sleep(1)

#     Email_code = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "code")))



#     otp = get_sagasoft_otp(otp_start_time)
#     if otp:
#         Email_code.send_keys(otp)
#         print(f"OTP entered: {otp}")
#         time.sleep(1)

#         Submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Button")))
#         Submit_button.click()
#         print("OTP submitted successfully")
#         time.sleep(2)
#         driver.execute_script("window.open('');")
#         driver.switch_to.window(driver.window_handles[2])
#         driver.get("https://signup-qa1.sagasoft.xyz/verify?method=mobile")
#         time.sleep(3)
#     Mobile_code=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"code")))
#     otps = get_mobile_otp(otp_start_time)
#     print(f"Retrieved OTP: {otps}")
#     if otps:
#         Mobile_code.send_keys(otps)
#         print(f"Mobile OTP entered: {otps}")
#         time.sleep(1)

#         Submitt_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Button")))
#         Submitt_button.click()
#         print("Mobile OTP submitted successfully")
#     else:
#         print("Failed to retrieve mobile OTP.")
#     if otp:
#         print("OTP verification completed successfully.")
    
#     else:
#         print("Failed to retrieve OTP.")

#     driver.quit()


# if __name__ == "__main__":
#     main()


# import time
# import imaplib
# import email
# from bs4 import BeautifulSoup
# import re
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC


# def get_sagasoft_otp(since_time):
#     username = "abitha@sagasoft.io"
#     password = "Abitha@123"
#     imap_server = "mail.sagasoft.io"
#     sender_email = "support@sagasoft.io"

#     mail = imaplib.IMAP4_SSL(imap_server)
#     mail.login(username, password)
#     mail.select("inbox")

#     timeout = 120
#     interval = 5
#     end_time = time.time() + timeout

#     while time.time() < end_time:
#         since_date = time.strftime('%d-%b-%Y', time.localtime(since_time))
#         criteria = f'(FROM "{sender_email}" SINCE {since_date})'
#         result, data = mail.search(None, criteria)
#         mail_ids = data[0].split()

#         if mail_ids:
#             for email_id in reversed(mail_ids):
#                 result, msg_data = mail.fetch(email_id, "(RFC822)")
#                 raw_email = msg_data[0][1]
#                 msg = email.message_from_bytes(raw_email)

#                 email_date = msg.get('Date')
#                 email_timestamp = email.utils.mktime_tz(email.utils.parsedate_tz(email_date))
#                 if email_timestamp < since_time:
#                     continue

#                 for part in msg.walk():
#                     if part.get_content_type() == "text/html":
#                         body = part.get_payload(decode=True).decode()
#                         soup = BeautifulSoup(body, "html.parser")
#                         text = soup.get_text()

#                         match = re.search(r'\b\d{6}\b', text)
#                         if match:
#                             mail.logout()
#                             return match.group()
#         time.sleep(interval)

#     mail.logout()
#     return None


# def main():
#     driver = webdriver.Chrome()
#     driver.get("https://signup-qa1.sagasoft.xyz/")
#     driver.maximize_window()
#     time.sleep(1)

#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "company"))).send_keys("sagasoft")
#     time.sleep(1)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "site"))).send_keys("tech1")
#     time.sleep(1)

#     Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "employee")))).select_by_visible_text("1 - 10")
#     time.sleep(1)

#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys("abitha@sagasoft.io")
#     time.sleep(1)

#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input-group-dropdown-2"))).click()
#     time.sleep(1)

#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/form/div[5]/div/div[1]/div/a[1]"))).click()
#     time.sleep(1)

#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mobile"))).send_keys("8489716029")
#     time.sleep(1)

#     industry_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "industry")))
#     industry_dropdown.click()
#     Select(industry_dropdown).select_by_visible_text("Technology & Software")
#     time.sleep(2)

#     Signup_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "SignupButton")))
#     Signup_Button.click()
#     print("Signup successfully")

#     # Get current time after clicking signup
#     otp_start_time = time.time()
#     time.sleep(2)  # short wait

#     driver.execute_script("window.open('');")
#     driver.switch_to.window(driver.window_handles[1])
#     driver.get("https://signup-qa1.sagasoft.xyz/verify?method=email")
#     time.sleep(1)

#     Email_code = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "code")))



#     otp = get_sagasoft_otp(otp_start_time)
#     if otp:
#         Email_code.send_keys(otp)
#         print(f"OTP entered: {otp}")
#         time.sleep(1)

#         Submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Button")))
#         Submit_button.click()
#         print("OTP submitted successfully")
#         time.sleep(2)
#         driver.execute_script("window.open('');")
#         driver.switch_to.window(driver.window_handles[2])
#     driver.get("https://signup-qa1.sagasoft.xyz/verify?method=mobile")
#     time.sleep(3)

#     Mobile_code = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "code")))
#     time.sleep(3)

#     otps = input("Enter the mobile OTP received via call: ")

#     if otps:
#         Mobile_code.send_keys(otps)
#         time.sleep(1)

#         Submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Button")))
#         Submit_button.click()
#         print("Mobile OTP submitted successfully")
#     else:
#         print("Failed to retrieve mobile OTP.")

#     if otp:
#         print("OTP verification completed successfully.")
#     else:
#         print("Failed to retrieve OTP.")

#     driver.quit()
# if __name__ == "__main__":
#     main()
#         driver.switch_to.window(driver.window_handles[2])
#         driver.get("https://signup-qa1.sagasoft.xyz/verify?method=mobile")
#         time.sleep(3)
#         Mobile_code=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"code")))
#         time.sleep(3)

#     otps = input("Enter the mobile OTP received via call: ")

#         print("Mobile OTP submitted successfully")
#     else:
#         print("Failed to retrieve mobile OTP.")
#     if otp:
#         print("OTP verification completed successfully.")
    
#     else:
#         print("Failed to retrieve OTP.")

#     driver.quit()


# if __name__ == "__main__":
#     main()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# browser=webdriver.Chrome()
# browser.get("https://practicetestautomation.com/practice-test-login/")
# time.sleep(2)
# title=browser.title
# user=browser.find_element(By.ID,"username")
# user.send_keys("abitha")
# time.sleep(2)
# pas=browser.find_element(By.XPATH,'//*[@id="password"])')
# pas.send_keys("12345")
# time.sleep(2)
# login=browser.find_element(By.ID,"submit")
# login.click()
# time.sleep(2)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser=webdriver.Chrome()
browser.get("https://signup-qa1.sagasoft.xyz/")
print("Title:",browser.title)
browser.maximize_window()
time.sleep(3)
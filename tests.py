from selenium import webdriver

open_edge = webdriver.Edge('msedgedriver.exe')

open_edge.get('https://www.youtube.com/')

show_message_button = open_edge.find_element_by_css_selector('ytd-searchbox')
click_button = open_edge.find_element_by_id('search-icon-legacy')
show_message_button.send_keys('python tutorial')
click_button.click()



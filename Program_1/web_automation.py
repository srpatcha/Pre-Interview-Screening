  
# web_automation.py

from selenium import webdriver
def automate_web_interaction(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
    except Exception as e:
            return f"Failed web automation: {str(e)}"
    finally:
        driver.quit()
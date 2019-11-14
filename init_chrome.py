from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def init_chrome(headless = False, 
                mobile = False,
                no_images = False,
                datadir =  r'/home/matias/.config/google-chrome/default',
                chrome_path = os.getcwd() +'/chromedriver', 
                windowsize = None):
    
    chrome_options = Options()
    
    if mobile:
#        chrome_options.add_experimental_option("mobileEmulation", { "deviceName": "Nexus 5" })
        chrome_options.add_experimental_option("mobileEmulation", 
            {"deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0}, 
             "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) "
             "Chrome/18.0.1025.166 Mobile Safari/535.19" , 
            'touch':True})
        chrome_options.add_experimental_option('w3c', False)
        
        useragent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36"
    else:
        useragent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        chrome_options.add_argument(f"user-agent={useragent}") if useragent else None
    
    chrome_options.add_argument("--headless") if headless else None
    #chrome_options.add_argument("--auto-open-devtools-for-tabs")
    chrome_options.add_argument(f"user-data-dir={datadir}") if datadir else None
    chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) if no_images else None
    
    driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options, desired_capabilities=chrome_options.to_capabilities())
    driver.set_window_size(windowsize[0], windowsize[1]) if windowsize else None
    #print('Running Chrome.')
    #options.add_argument('start-maximized')
    return driver

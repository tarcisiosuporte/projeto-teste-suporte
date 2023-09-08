
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
arguments = ['--lang=pt-BR','--windows-size=1024,500','--incognito']
for arguments in arguments:
    chrome_options.add_argument(arguments)

chrome_options.add_experimental_option('prefs', {   
    'download.prompt_for_download': False,
    'profile.default_content_setting_values.notifications':2,
    'profile.default_content_setting_values.automatic_downloads':1,
})    


# inicializando o whebdrive
#drive= webdriver.Chrome(service=chromeService(ChromeDriverManager().install()),options=chrome_options)
chrome= webdriver.Chrome(service=chromeService(ChromeDriverManager().install()),options=chrome_options)

url_do_forms    = "https://conectividadesocialv2.caixa.gov.br"
#este funcionava chrome = webdriver.Chrome(executable_path='chromedriver.exe')

# Navegando.
#este funcionavachrome.get(url_do_forms)
chrome.get(url_do_forms)

input(90)
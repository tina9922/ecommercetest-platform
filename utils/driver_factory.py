from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import tempfile

def get_driver():
    # Needed for GitHub Actions 
    # Your tests may fail initially because GitHub Actions Linux runners often need:
    # Without headless mode:
    # ❌ GitHub Actions may fail launching browser
    # Chrome setup
    # Headless browser mode
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
    # 🚫 Disable password manager popup
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=options)
    return driver 

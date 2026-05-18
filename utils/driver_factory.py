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
    print("trigger CI")
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
'''
    Think of regression.yml as:

📋  Instructions for GitHub Actions telling GitHub:
    Whenever code changes happen, automatically run my automation tests.

    Artifacts =
👉 downloadable files after pipeline completes

  Example:

  HTML reports
  screenshots
  logs

  Your regression.yml is basically:

👉 “automation instructions for GitHub cloud machines.”

  The regression.yml file defines the CI/CD workflow for the automation framework using GitHub Actions. 
  It automatically triggers test execution whenever code is pushed or a pull request is created on the main branch. 
  The workflow provisions a Linux runner(UBUNTU VM), installs Python and project dependencies, downloads your repository code into the VM
  executes the pytest regression suite, and uploads the generated test reports as artifacts for analysis.

    End-to-End Flow

When you push code:

Developer Pushes Code
        ↓
GitHub Actions Triggered
        ↓
Ubuntu VM Created
        ↓
Repo Downloaded
        ↓
Python Installed
        ↓
Dependencies Installed
        ↓
Pytest Runs
        ↓
Reports Generated
        ↓
Artifacts Uploaded

Now you need to verify:
👉 “Does the pipeline actually run successfully in GitHub?”

As soon as push completes:

👉 GitHub detects:

.github/workflows/regression.yml

and automatically triggers pipeline.

“Queued” is actually a good sign—it means GitHub accepted your workflow and is about to run it, but it hasn’t started executing yet.
If you triggered multiple commits quickly:

GitHub queues them
Only a limited number run in parallel
'''
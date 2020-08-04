# Custom Google Form Autofill

Custom Google Form autofiller implementation using Selenium.

## Installation

### Step 1: Install the Webdriver

First we need to find our browser’s version number. This is to make sure we install the correct webdriver.

Click `Help` `>` `About Google Chrome`.

Then go to https://chromedriver.chromium.org/downloads and choose the download corresponding to the chrome version number and operating system.

### Step 2: Install Selenium

Create a directory, navigate to the directory and use a virtual environment, more on virtual environment : https://docs.python.org/3/tutorial/venv.html.

Install Selenium using the command `pip install selenium` on virtual environment.

### Step 4: Modify script parameters

Modify mandatory parameters inside `fill.py`

### Step 5: Run the script

```bash
$ python fill.py
```

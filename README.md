# Custom Google Form Autofill

Custom Google Form autofiller implementation using Selenium.

## Installation

### Step 1: Install the Webdriver

First we need to find our browser’s version number. This is to make sure we install the correct webdriver.

Click `Help` `>` `About Google Chrome`.

Then go to https://chromedriver.chromium.org/downloads and choose the download corresponding to the chrome version number and operating system.

Extract the `chromedriver` binary from the downloaded zip to current directory or any directory that you have decided.

### Step 2: Create Virtual Environment

Navigate to any directory where you want to place the virtual environment (using current directory is fine) and create the virtual environment : 

```bash
python3 -m venv fill-env
```

This will create the `fill-env` directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter, the standard library, and various supporting files.

Then we can activate the virtual environment by using the following command : 

```bash
fill-env\Scripts\activate.bat
```

More on virtual environment setup : https://docs.python.org/3/tutorial/venv.html.

### Step 3: Install Selenium

Install Selenium using the command `pip install selenium`.

### Step 4: Modify script parameters

Modify required parameters inside the `fill.py` script :

- name
- age
- position
- contact_history
- form_url

Also don't forget to modify the `executable_path` to include the directory path where we have extracted `chromedriver` earlier.

```python
browser = webdriver.Chrome(executable_path='chromedriver.exe', options=option)
```

## Running the script

Run the script from terminal :

```bash
python3 fill.py
```

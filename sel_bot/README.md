## 0: Working
This is a complete Python program that uses the Selenium module of Python. Selenium is a tool for controlling web browsers in performing browser automation. Selenium creates an instance of webdriver, which allows it to control and automate web-processes. You can read more about this at this [site](https://selenium-python.readthedocs.io/).


## 1: Installation

This program requires selenium and python. 
* Download the latest python version from [here](https://www.python.org/downloads/).
* You also should have pip installed to install the neccessary pacakages of python. To check if pip is installed in your system use the command "pip --version", this should display a message showing the current version of pip.

### 1.1: Cloning the repository
Move into the directory where you would like to clone this repository and using terminal in your code editor and paste the following lines.
```bash
git clone https://github.com/preetam-g/linkedin_connection_bot.git
cd linkedin_connection_bot
```

### 1.2: Installing required packages
Install the required python packages, as this program requires selenium, you can install it using this command.
```bash
pip install selenium
```

### 1.3: CSV file
Edit the "profiles.csv" file with a list of profiles you would like to send connection notes to. 

## 3: Usage

### 3.1: Update configuration file
```bash

[linkedin]
LINKEDIN_USERNAME = "your username"
LINKEDIN_PASSWORD = "your password"

```

### 3.2: Run the program
Move into the linkednin_connection_bot directory using a terminal of your choice. Copy the following commands.
```bash
cd sel_bot
python main.py
```
If the following chrom driver does not work you can install the driver matching your chrome brower's version from [here](https://sites.google.com/chromium.org/driver/).

## 4: Remember
* Try not to make any changes in the "main.py" if you don't completely understand how to code works. If you are well aware of python you can tweek the code according to your needs by refering to the selenium documentation.

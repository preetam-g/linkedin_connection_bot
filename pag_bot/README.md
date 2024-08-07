## 0: Working
This is a complete Python program that uses the PyAutoGUI module of Python. This module is used to control your mouse and keyboard commands. One of the applications of PyAutoGUI is to automate actions of the mouse and keyboard based on the content present on the screen, which is being done here. If you want to know more about PyAutoGUI, you can visit this [site](https://pyautogui.readthedocs.io/en/latest/).

## 1: Pre-requisites
* This code is designed to work on Windows computer systems.
* You should be logged in to your LinkedIn web in **_chrome_** browser. (It will not work if you have any browsers other than Chrome.)
* You should have a dark theme set on the LinkedIn webpage. On how to switch, visit this [site](https://www.linkedin.com/help/linkedin/answer/a524473/switch-between-dark-and-light-mode#:~:text=To%20switch%20to%20either%20dark,under%20Display%2C%20click%20Dark%20mode.).

## 2: Installs and Modifications

This program requires python, pyautogui and open-cv. 
* Download the latest python version from [here](https://www.python.org/downloads/).
* You also should have pip installed to install the neccessary pacakages of python. To check if pip is installed in your system use the command "pip --version", this should display a message showing the current version of pip.

### 2.1: Cloning the repository
Move into the directory where you would like to clone this repository and using terminal in your code editor and paste the following lines.
```bash
git clone https://github.com/preetam-g/linkedin_connection_bot.git
cd linkedin_connection_bot
```

### 2.2: Installing required packages
Install the required python packages. In case of other requirements, install them accordingly.
```bash
pip install -r requirements.txt
```

### 2.3: Google sheet
* Create a Google sheet and add all the links to LinkedIn profiles in one column. Make sure that there are no empty cells between two links in that column. Here is an example image.

<p align="center">
    <img src ="https://github.com/preetam-g/linkedin_connection_bot/assets/118665778/b3e1cdf5-0756-47ae-9335-4a6d2ea239a2" height = "280">
</p>

* Now go to the "images.py" file and you can find a variable named "excel_sheet_link". Update the link with the link of your excel sheet.  To avoid google account conflicts, make sure the sheet is public.

### 2.4: Connection Note
You can also add your personalized connection note. The default note set is 
<p align="center">
    Hi, <br />
    I would like to connect with you.
</p>
This has been kept optional due to multiple restrictions of LinkedIn on free accounts.
To add your note, open the "images.py" file and write the note within triple dobule-quotes ("""Like this"""). This ensures that we can add notes consisting of multiple lines in the python file.


## 3: Usage

### 3.1: Inputs
* You will be asked for cell number, give the cell number of cell from which you want to start sending requests from the excel sheet.
* Give the number of cells this code should run for.
* You can also choose whether to send the connection note or not. If you choose "y" make sure to edit the default connection note before starting the program.

### 3.2: Run the program
Move into the linkednin_connection_bot directory using a terminal of your choice. Copy the following commands.
```bash
cd pag_bot
python main.py
```

## 4: Remember
* Try not to make any changes in the "main.py" if you don't completely understand how to code works. If you are well aware of python you can tweek the code according to your needs by refering to the pyautogui documentation. 
* If you want to stop the program force your mouse cursor to the top left corner of the screen, this will trigger the fail-safe mechanism and the program will stop executing. You can continue again from the stopped cell by giving this cell num and input when you run the program again.
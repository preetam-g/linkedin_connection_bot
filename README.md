## LinkedIn Connections Automation Bot

This project is a LinkedIn auto connection bot which automates the process of connecting with professionals in linkedin. You just have to list the profiles and this can do the rest. 

#### Overview
As a Marketing Executive for Techniche, North-East India's largest annual techno-management fest conducted solely by the student body of the Indian Institute of Technology Guwahati, one of my initial tasks was to profile and list various companies from specific sectors that could potentially become our financial partners for the event.

This task required extensive research on LinkedIn, sending connection requests to marketing personnel at targeted companies. To streamline this tedious process, I decided to automate it using PyAutoGUI. As this lead to system specific configurations I decided to use Selenium for web-automation. These automation tools significantly aided me in efficiently managing the profiling and outreach efforts. 

This repository consists the python code that helped me in increasing my connections and reach multiple companies with minimal efforts.

#### Description

This repository contains two directories, each of them have their specific instructions inside.
* pag_bot: contains the PyAutoGUI code which uses data from a google sheet.
* sel_bot: contains the Selenium code which uses data from a csv file.

These two work in a similar manner, each of them requires a list of links to profiles of the people you would like to connect. They open your browser, go to the provided links and send connection requests.

#### Don't forget
This code only sends requests but does not keep track of your connections so make sure you actively check your linkedIn connections. If any of these professionals accept your connection request, using the contact info option obtain their phone_no. and email ids and update them in your database correspondingly along with their position. Once you feel like you have a robust database, group the database according to company name and start your cold callings.

HAND! (Have a nice Day :beaming face with similing eyes:)
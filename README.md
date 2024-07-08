## LinkedIn Connections Automation Bot

This project is a LinkedIn auto connection bot that automates connecting with professionals on LinkedIn. You have to list the profiles, and this can do the rest. 

### Overview
As a Marketing Executive for Techniche, North-East India's largest annual techno-management fest conducted solely by the student body of the Indian Institute of Technology Guwahati, one of my initial tasks was to profile and list various companies from specific sectors that could potentially become our financial partners for the event.

This task required extensive research on LinkedIn and sending connection requests to marketing personnel at targeted companies. To streamline this tedious process, I decided to automate it using PyAutoGUI. As this led to system-specific configurations, I used Selenium for web automation. These automation tools significantly aided me in efficiently managing the profiling and outreach efforts. 

This repository consists of the Python code that helped me increase my connections and reach multiple companies with minimal effort.

### Description

This repository contains two directories, each with specific instructions inside.
* pag_bot: contains the PyAutoGUI code, which uses data from a Google sheet.
* sel_bot: contains the Selenium code, which uses data from a CSV file.

These two work similarly; each requires a list of links to profiles of the people you would like to connect with. They open your browser, open the provided links, and send connection requests.

### Don't forget
This code only sends requests but does not keep track of your connections, so please ensure you actively check your LinkedIn connections. If any of these professionals accept your connection request, using the contact info option obtain their phone_no. and email IDs and update them in your database, along with their position. Once you feel like you have a robust database, group the database according to the company name and start your cold callings.

HAND! (Have a nice Day :grin:)

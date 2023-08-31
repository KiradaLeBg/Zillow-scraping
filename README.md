# **Stephanie Younger's Zillow Profile Reviews Web Scraper** 
# **Overview**
The Zillow Reviews Scraper is a Python script designed to extract review data from [Stephanie Younger's Zillow](https://www.zillow.com/profile/Stephanie-Younger-CA/) profile page using their public API. This tool allows you to collect review information and store it in a structured format for further analysis or processing.

# **Installation**
To use the Zillow Reviews Scraper:

Clone or download this repository to your local machine.
Install the required dependencies using the following command:
```bash
pip install requests
```
# **Usage**
Configure the script by adjusting variables such as fieldnames and max_pages in the scraper.py file.
Run the script in your terminal using the command:
```bash
python Reviews.py
```
The script will fetch review data from Stephanie Younger's Zillow profile page and save it in a CSV file named ```reviews.csv```.

# **Technologies Used**
- Python
- Requests library
  
# **Customization**
Modify the fieldnames variable to customize the columns in the CSV file.
Adjust the max_pages variable to control the number of pages you want to scrape.

# **Notes**
Be aware of Zillow's terms of use and API policies before using this script.
Be mindful of potential API rate limits or restrictions to avoid issues.

# **License**
This project is licensed under the [GNU General Public License v3.0](License). 

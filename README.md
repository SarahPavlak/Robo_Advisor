# Robo_Advisor

Ensure that your computer has: 
Pip
Python 3.7
Anaconda 3.7

Setup:
1. Clone or download this repository onto your computer:
    git clone https://github.com/SarahPavlak/Robo_Advisor
2. Utilizing Anaconda, create a new virtual environment.
3. Within the new environment, install the following: 
    pip install requests python-dotenv
 
Security Setup: 
1. Navigate to https://www.alphavantage.co/ and request an API Key
2. Create a .env file in your virtual code studio or other desired platform. Within the .env file, type "ALPHAVANTAGE_API_KEY='YOUR API KEY GOES HERE'
    This will create an environment variable for you which will ensure that your key remains secure. 

Running the program:
1. On your terminal type:
    1. cd desktop, 
    2. cd *name of your folder*, 
    3. conda activate *name of created environment*
    4. "python *name of your document*" for example, python robo.py
2. Type the name of the stock you would like to analyze, as well as your preferred risk level. Wait for results to generate.

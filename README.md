# symmetrical-spoon

###How to run tests:
Optional: Set up virtualenv of your choice 

1. Install dependencies with pip `pip install -r requirements.txt`
2. Export your login username as env variable to LOGIN_USERNAME
3. Export your login password as env variable to LOGIN_PASSWORD
4. Download Chrome and matching ChromeDriver version https://chromedriver.chromium.org/downloads
5. Put chromedriver of your choice to the /drivers directory under repo root
6. Append drivers directory to your PATH to allow chromedriver to execute 
7. Export the path to your chromedriver executable to CHROMEDRIVER_PATH 
8. Run `behave --tags=@login` from repository root to execute tests

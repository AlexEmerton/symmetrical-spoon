# symmetrical-spoon

###How to run tests:
Optional: Set up virtualenv of your choice 

1. Install dependencies with pip `pip install -r requirements.txt`
2. Export your login username as env variable to LOGIN_USERNAME
3. Export your login password as env variable to LOGIN_PASSWORD
4. Append drivers directory to your PATH to allow chromedriver to execute  (executables included for Win and Mac)
4. Run `behave --tags=@login` from repository root to execute tests

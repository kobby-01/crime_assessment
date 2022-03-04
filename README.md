# Crime Assessment

## Maintenance details are as follows

### Data source
I got the datasource from https://data.world/carlvlewis/u-s-metro-areas-violent-crime-rates-by-type-1970-2015 and added them to the project in a folder named datasets.

### Virtual Environment

#### Setup (Windows)
        pyenv local 3.10.0 # this sets the local version of python to 3.10.0
        python3 -m venv .venv # this creates the virtual environment for you
        .\.venv\Scripts\activate # this activates the virtual environment
        pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.

I used Flask (https://flask.palletsprojects.com/en/1.1.x/) as our web framework for the application. We install that with 
        
        pip install flask

And that will install flask with its associated dependencies.

I was be able to run the datasource to confirm the path is correct, I read the file with

        python3 parse_csv.py

#### Running Virtual Server
        export FLASK_APP=crimes.py
        export FLASK_ENV=development
        python3 -m flask run

### Error Handling
To handle errors in the flow, I added to the file "crimes.py" the function below and later added a 404.html file inside the templates folder to handle the error response

        @app.errorhandler(404)
        def page_not_found(e):
            return render_template("404.html")

### Testing

#### Setup
I used this command to install pytest and coverage to enable me test

        pip install pytest coverage

#### Running Test
I added a file named "setup.cfg" which is not required but makes running tests with coverage less verbose.
I executed the command below to run the test I have written
        pytest
* For running the coverage test, I executed the command below to acheive that and the results is as below
        coverage run -m pytest

        ================================================= test session starts =================================================
        platform win32 -- Python 3.10.0, pytest-7.0.1, pluggy-1.0.0
        rootdir: C:\Users\Kobby\Desktop\crime_assesment, configfile: setup.cfg, testpaths: tests
        collected 1 item
        
        tests\app_test.py .                                                                                              [100%]
        
        ================================================== 1 passed in 0.55s ==================================================

* To get a coverage report, I issued the command below and the result is as below
        coverage report

        Name                Stmts   Miss Branch BrPart  Cover
        -----------------------------------------------------
        crimes.py              12      0      0      0   100%
        tests\__init__.py       0      0      0      0   100%
        tests\app_test.py       7      0      0      0   100%
        -----------------------------------------------------
        TOTAL                  19      0      0      0   100%

## Heroku URL
        Kindly use this URL to access the web application https://crime-assessment.herokuapp.com/
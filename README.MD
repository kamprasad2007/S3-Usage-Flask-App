1) Installing virtualenv

    On macOS and Linux:
        python3 -m pip install --user virtualenv

    On Windows:
        py -m pip install --user virtualenv

2) Creating a virtual environment
    On macOS and Linux:
        python3 -m venv env

    On Windows:
        py -m venv env

3) Activating a virtual environment
    On macOS and Linux:
        source env/bin/activate

    On Windows:
        .\env\Scripts\activate

4) Install project dependency using requirements file
    On macOS and Linux:
        python3 -m pip install -r requirements.txt

    On Windows:
        py -m pip install -r requirements.txt

5). In dev.config file
    configure AWS_ACCESS_KEY and AWS_SECRET_KEY


6). Running Flask App in your local

    On macOS and Linux:
        python3 app.py

    On Windows:
        py app.py


7). Access web page
    http://localhost:8080


7). Leaving the virtual environment after done.

    On macOS, Linux and Windows:
        deactivate 
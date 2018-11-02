##  Setup Your Environment

###     First install python3

-   $ sudo apt-get update
-   $ sudo apt-get install python3.6

###     Install pip

-   $ wget https://bootstrap.pypa.io/get-pip.py
-   $ sudo python3 get-pip.py

###     Install OpenCV on Ubuntu into a virtual environment with pip

-   $ pip install virtualenv virtualenvwrapper

-   #### Before Continue Add some line
    -   $ sudo gedit ~/.bashrc
    -   Add these line to the end of ~/.bashrc file
        ```
        # virtualenv and virtualenvwrapper
        export WORKON_HOME=$HOME/.virtualenvs
        export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
        source /usr/local/bin/virtualenvwrapper.sh
        ```
    -   $ source ~/.bashrc

###     Commands of virtualenvwrapper

-   **Create** an environment with _mkvirtualenv_ .
-   **Activate** an environment (or __switch__ to a different one) with _workon_ .
-   **Deactivate** an environment with _deactivate_ .
-   **Remove** an environment with _rmvirtualenv_ .

###     Now Create an environment

-   $ mkvirtualenv cv -p python3
-   $ virtualenv cv -p python3

###     Now install open cv

-   $ pip install opencv-contrib-python
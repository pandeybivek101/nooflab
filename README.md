# nooflab

# Installation

1. make sure Python and Virtual environment is already installed on your computer. if not please follow this link (https://www.python.org/downloads/) for python installation and use command (pip install       virtualenv) for virtual environment installation.


2. create virtual environment using the command
    virtualenv <"name of virtual environment">

    based on my case.

    cd /home/bivek/Desktop
    virtualenv demo   


4. After creating demo virtual environment there should be a folder named demo. Go into that folder and clone the project from the github. make sure the the main project folder must be inside demo folder along
    with other two folders(lib and bin)

    cd <"path to virtual environment">

    based on my case.

    cd /home/bivek/Desktop/demo
    git clone https://github.com/pandeybivek101/nooflab.git


3. Activating the virtual environment
    
    Go into the demo that folder there should be 3 folders lib, bin and nooflab(project folder), you can activate the virtual environment inside demo folder. To do so use below mentioned code, below mentioned command is for linux devices if you are using window or mac OS please check the given link( https://linuxhint.com/activate-virtualenv-windows/ ,   https://mnzel.medium.com/how-to-activate-python-venv-on-a-mac-a8fa1c3cb511)

    cd <"path to demo">

    based on my case.

    cd /home/bivek/Desktop/demo
    
    source bin/activate

4. Installation of all dependencies and packages required for the project. All the requirements are included in requirements.txt file, you can find requirements.txt file inside the project folder
    
    cd <"path to demo">/<"project name">
    
    based on my case.

    cd /home/bivek/Desktop/demo/nooflab

    pip install -r requirements.txt

    also make sure your virtual environment is activated while installing dependencies and packages.


5. Making migrations

    create the database tables from the models folder to do so. use the given command

    cd /home/bivek/Desktop/demo/nooflab

    python manage.py makemigrations

    python manage.py migrate


6. Database configuration
    Hence all kind of databases can be configured, in this project I have used sqlite database which is also the default database of django. After executing the above command django will automatically generate the db.sqlite file inside the project folder.

7. Running the local server.

    you need to execute the below given command to run local serve

    python manage.py runserver

    you can see server started in the terminal.



8. Go to the the given url in the browser or you can send request using postman. The endpoints for fetching the data and storing into the database is 
    http://localhost:8000/postal_codes/fetch/companies

9. Endpoints for getting the stored data 
    http://localhost:8000/postal_codes/02100/companies












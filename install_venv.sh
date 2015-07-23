sudo apt-get install python-virtualenv
sudo apt-get install python-pip
virtualenv venv
source venv/bin/activate
pip install --upgrade Flask Flask-RESTful mock nose requests SQLAlchemy

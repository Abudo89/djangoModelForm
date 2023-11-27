# djangoModelForm
___________Run the following on terminal to install mysql_________
pip install pymysql

_____________on installed app in the setting app_________

add your app; 


___copy and paste the below into the __init__.py app______

import pymysql


pymysql.install_as_MySQLdb()



_______DATABASE__________

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hpclass',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306'
    }
}


________________________makemigrations____________________


py manage.py makemigrations djangoModelForm

then


py manage.py migrate

_____________create user_______________________


py manage.py createsuperuser




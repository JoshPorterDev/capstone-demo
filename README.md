# capstone-demo

# Install project on your local machine
Create folder names 'capstone' in your desktop directory
<br />
Open the capstone folder in your file explorer
<br />
Click where the red blob is in the picture below
![cursor](cmd.PNG)
<br />
type 'cmd' to open the command prompt in this directory
<br />
Inside the command prompt type the following line
```
git clone https://github.com/JoshPorterDev/capstone-demo.git
```
<br />
Navigate into the project folder using the command

```
cd capstone-demo
```

Install virtualenv
```
pip install virtualenv
```

Create and activate virtualenv
```
virtualenv env
env\Scripts\activate
```

Install requirements
```
pip install -r requirements.txt
```

Make initial database migrations
```
python manage.py migrate
```

Start local Dev server
```
python manage.py runserver
```

Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
<br />
If everything worked correctly, you should see this screen
![Home](home.PNG)

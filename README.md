# Contact List (MongoDB/CLI) 🌐

## Description 📑
this project is consist of 2 main parts; first we have the `models.py` file, where the collection's schema is. 
then, we have the `main.py` which has the responsibility to do the CRUD operations on the database.

*Notice: I have commented codes related to logger because It was more of a distraction due to the fact that it logs the
the information in the terminal where the output of the command also exists!
but you can uncomment it based on your desire :)*

***APOLOGY! I wanted to use `MongoDB-Atlas` to deploy the database... I did it but I couldn't insert any data :( now you need to run a MongoDB instanse on your `localhost` port `27017` (which is the default port of it). alternative way, you can modify the `connection_string` to connect to your own MongoDB database (it will create the database and collection automatically)***

## How to Run ❓
first you need to create a virtual environment, cd to the directory where this file is and then run the following command:

Create and Activate a Virtual Environment:<br>
 
- Linux/mac: 
```bash
$ pip install virtualenv
$ virtualenv [YourVenvName]
$ source [YourVenvName]/bin/activate
```

- Windows:
```cmd
pip install virtualenv
python -m venv [YourVenvName]
[YourVenvName]/Scripts/activate
```
<br>


install the required libraries and run the code:
```bash
$ pip install -r requirements.txt
```

execute ***READ*** operation:
```bash
$ python main.py list
```
or if you want to search for a specific contact:
```bash
$ python main.py search -f <first name> -l <last name>
```

execute ***CREATE*** operation:
```bash
$ python main.py create -f <first name> -l <last name> -d <country code> -n <phone number> [-C <country>] [-c <city>] [-a <address>]
```

execute ***UPDATE*** operation:
```bash
$ python main.py create -f <first name> -l <last name> [-d <new country code>] [-n <new phone number>] [-C <new country>] [-c <new city>] [-a <new address>] [-F <new first name>] [-L <new last name>]
```

execute ***DELETE*** operation:
```bash
$ python main.py delete -f <first name> -l <last name>
```

## Contribute! 🤝🏻
I'm more than happy to hear your feedbacks and collaborate with you guys!

if you had any problem contributing on the project, feel free to contact me:

- [Gmail](mailto:amirhosseinkhalili901@gmail.com "my gmail address")
- [LinkedIn](https://linkedin.com/in/amirhossein-khalili-a83250271 "my LinkedIn account")
- [Telegram](https://t.me/Amirkh_MoD "my Telegram account")
- [Github](https://github.com/amirkhgraphic "my Github account")
- [Quera](https://quera.org/profile/Amirkh1996 "my Quera profile/resume")


*- Amirhoseein Khalili*
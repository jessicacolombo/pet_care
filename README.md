<h1>pet_care</h1>

<p>Repository made to study Django and Django Rest Framework. The app is build on python 3.11.0.</p>
<br>

<h2> How to run de app locally: </h2>
<br>
<h3> Preparing the environment: <h3>
<br>
<li> Create a virtual environment: </li>

```shell
python -m venv venv
```

<br>
<li> Activate the virtual env:</li>

```shell
#on windows
source venv/Scripts/activate

#on linux or macOS
source venv/bin/activate
```

<br>
<li>Install the dependencies on the requirements.txt file:</li>

```shell
pip install -r requirements.txt
```

<h3> Running the app: <h3>
<br>
<li>Running the migrations and creating the database:</li>

```shell
python manage.py migrate
# will create automaticaly a SQLite database
```

<br>

<li>Starting the server:</li>

```shell
python manage.py runserver
```

<br>

<li>Access the endpoint -> http://127.0.0.1:8000/api/ </li>

<br>

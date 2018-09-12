# Setting up the python development
1. Create a new venv <br />
flmiron@MININT-5QD0CBB MINGW64 ~/source/tutorials/py-flask/py-words-service (master)
py -3 -m venv venv

2. Source the new env <br />
. venv/Scripts/activate <br />

3. Install requirements <br />
pip install -r requirements.txt <br />

4. Run flask <br />
cd src <br />
export FLASK_APP=hello.py <br />
python -m flask run <br />

5. You should see: <br />
    * Serving Flask app "hello.py"
    * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

# For changes to the mysql db:
Run a mysql instance called mysql1 with root password set to fun <br />

docker run --name=mysql1  -e MYSQL_ROOT_PASSWORD=fun -e MYSQL_ROOT_HOST=% -p 3306:3306 -d mysql/mysql-server:latest

docker logs mysql1

docker exec -it mysql1 mysql -uroot -p
From <https://hub.docker.com/r/mysql/mysql-server/> 
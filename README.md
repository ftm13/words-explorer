# For local development
<h3> Setup python venv and install deps. Steps 1 and 3 are on subsequent runs. </h3>
1. Create a new venv <br />
py -3 -m venv venv

2. Source the new env <br />
. venv/Scripts/activate <br />

3. Install requirements <br />
pip install -r requirements.txt <br />

4. Run flask <br />
cd src <br />
python hello.py <br />

5. You should see: <br />
    * Serving Flask app "hello.py"
    * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

<h3> Create a mysql db container:TODO explain how to do this locally</h3>
Run a mysql instance called mysql1 with root password set to fun <br />

docker run --name=mysql1  -e MYSQL_ROOT_PASSWORD=<insert-pswd> -e MYSQL_ROOT_HOST=% -p 3306:3306 -d mysql/mysql-server:8

docker logs mysql1

docker exec -it mysql1 mysql -uroot -p
From <https://hub.docker.com/r/mysql/mysql-server/> 

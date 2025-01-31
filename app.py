from flask import Flask, render_template , request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your-secret-key'

#MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'image-gallery'

mysql = MySQL(app)

@app.route('/register', methods=['GET','POST'])
def register():
    
    if request.method == 'POST':
        username = request.form.get('username')
        pwd = request.form.get('password')
        cur = mysql.connection.cursor()
        cur.execute(f"INSERT INTO gallery_tables (username, password) values ('{username}', '{pwd}')")
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute(f"select username, password from gallery_tables where username = '{username}'")
        user = cur.fetchone()
        cur.close()
        if user and pwd  == user[1]:
            session['username'] = user[0]
            return redirect(url_for('index'))
        else:
            return render_template('login.html', eror = 'Invalid Username or password')
    return render_template('login.html')



@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

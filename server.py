from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/users")

@app.route('/users')
def allUsers():
    users = User.get_all()
    return render_template("read.html", all_users = users)

@app.route('/users/new')
def newUsers():
    return render_template("create.html")

@app.route('/addUser', methods=['post'])
def add_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/oneUser')

@app.route('/users/<int:id>/edit')
def editUser(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html", editUser = User.get_selectedUser(data)) 

@app.route('/user/update',methods=['POST'])
def updateUser():
    User.update(request.form)
    return redirect('/oneUser')       

@app.route('/oneUser')
def userInfo():
    data ={ 
        "id":id
    }
    user = User.get_oneUser(data)
    return render_template("userInfo.html", user = user)    

@app.route('/users/delete/<int:id>')
def deleteUser(id):
    data ={
        'id': id
    }
    User.delete(data)
    return redirect('/users') 

if __name__ == "__main__":
    app.run(debug=True)


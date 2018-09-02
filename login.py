from bottle import run, get, post, request, route, static_file, error # or route


@route("<file:path>") 
def js_serve(file): 	
    return static_file(file, root="C:\Users\Vinay_2\Documents\RoomMe") 

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
        
def check_login(username, password):
    if username == "mark":
        return True;
        
@error(404)
def error404():
    return "woah shit"
        
run(host = 'localhost', port = 8080, debug = True)
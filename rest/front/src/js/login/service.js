function login(){
    username = document.getElementById('username').value
    password = document.getElementById('password').value
    
    const data = {
        "password": password,
        "username": username
    }

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "POST", "http://localhost:8000/auth/token/login/", false); // false for synchronous request
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    xmlHttp.send( JSON.stringify(data) );

    const token = JSON.parse(xmlHttp.responseText).auth_token
    if ( token ){
        save_token(token)
        window.location('../users/users.html')
    }
    else
        alert("incorrect data for login")
}

function save_token(token){
    localStorage.setItem('token', token);
}
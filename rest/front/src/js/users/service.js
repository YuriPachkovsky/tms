function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    token = getToken()

    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.setRequestHeader('Authorization','Token ' + token);

    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function generateUsers()
{
    var users = httpGet("http://localhost:8000/rest/")
    console.log(users)
    const objects = JSON.parse(users);
    console.log(objects)
    var html = "";
    for (let i = 0; i < objects.length; i++) {
        const elem  = objects[i]
        html += '<div class="card margin_top_50px" style="width: 18rem;" name="content">';
        html += '<div class="card-body">'
        html += '<h5 class="card-title">' + elem.id + '</h5>'
        html += '<p class="card-text">'+ elem.password+'</p>'
        html += '</div>';
        html += '</div>';
            
    }

    const main = document.getElementById('main');
    main.innerHTML = html + main.innerHTML
}

function getToken(){
    return localStorage.getItem('token')
}

function changeColor()
{
  const content = document.getElementsByName('content')
  console.log(content)
  content.forEach(element => {
    element.style.color = "green"
  });
}

window.onload = function() {
    generateUsers()
  };
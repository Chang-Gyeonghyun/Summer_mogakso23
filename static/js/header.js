const loginButton = document.querySelector("#etc button:last-child");
const postingButton = document.querySelector("#etc button:first-child");
const homebutton = document.querySelector("#logo img");

function movelogin(e){
    if (e.target.textContent == "LOGIN"){
        location.href = "/log-in";
    }
    
    else if (e.target.textContent == "LOG OUT"){
        location.href = "/logout";
    }
}
function moveposting(){
    location.href = "/posting";
}
function movehome(){
    location.href = "/";
}
function cursuron(event){
    event.target.style.cursor = "pointer";
}

loginButton.addEventListener("click",movelogin);
postingButton.addEventListener("click",moveposting);
homebutton.addEventListener("click", movehome);
homebutton.addEventListener("mouseenter",cursuron);
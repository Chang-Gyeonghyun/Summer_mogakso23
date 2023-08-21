const loginButton = document.querySelector("#etc button:last-child");
const postingButton = document.querySelector("#etc button:first-child");
const homebutton = document.querySelector("#logo img");
const searchForm = document.querySelector("#search form");


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
if (searchForm){
    searchForm.addEventListener("submit", function(e) {
        e.preventDefault(); // �⺻ ���� ���� (������ ��ȯ ��)
        
        const sort = "title"; // ���� ��� ("writer"�� �ϵ��ڵ��� ����)
        const subject = e.target.querySelector("input").value;
        
        const url = `/posting?sort=${sort}&subject=${encodeURIComponent(subject)}`;
        window.location.href = url; // ������ ���𷺼�
    });

}
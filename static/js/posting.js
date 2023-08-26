const chooselist = document.querySelector("main #choose")
const liElements = chooselist.querySelectorAll("li");
const Postlist = document.querySelector("#posthome")
const Post = Postlist.querySelectorAll("li");

liElements.forEach(li => {
    li.addEventListener("click", function(e) {
        console.log("click")
        const sort = "writer"; 
        const subject = li.textContent; 
        
        const url = `/posting?sort=${sort}&subject=${encodeURIComponent(subject)}`;
        window.location.href = url; 
    });
});


Post.forEach(li => {
    li.addEventListener("click", function(e) {
        console.log("click")
        const spanlist = li.querySelectorAll("span");
        const title = spanlist[1].textContent;
        const subject = spanlist[2].textContent;
        
        const url = `/reading?title=${title}&writer=${encodeURIComponent(subject)}`;
        window.location.href = url;
    });
});
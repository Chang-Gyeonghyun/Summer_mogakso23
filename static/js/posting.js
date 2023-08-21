const chooselist = document.querySelector("main #choose")
const liElements = chooselist.querySelectorAll("li");
const Postlist = document.querySelector("#posthome")
const Post = Postlist.querySelectorAll("li");

liElements.forEach(li => {
    li.addEventListener("click", function(e) {
        console.log("click")
        const sort = "writer"; // 정렬 방식 ("writer"로 하드코딩된 예시)
        const subject = li.textContent; // 클릭한 리스트 아이템의 내용
        
        const url = `/posting?sort=${sort}&subject=${encodeURIComponent(subject)}`;
        window.location.href = url; // 페이지 리디렉션
    });
});


Post.forEach(li => {
    li.addEventListener("click", function(e) {
        console.log("click")
        const spanlist = Postlist.querySelectorAll("span");
        const title = spanlist[1].textContent;
        const subject = spanlist[2].textContent;
        
        const url = `/reading?title=${title}&writer=${encodeURIComponent(subject)}`;
        window.location.href = url; // 페이지 리디렉션
    });
});
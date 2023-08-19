const chooselist = document.querySelector("main #choose")
const liElements = chooselist.querySelectorAll("li");

liElements.forEach(li => {
    li.addEventListener("click", function(e) {
        console.log("click")
        const sort = "writer"; // ���� ��� ("writer"�� �ϵ��ڵ��� ����)
        const subject = li.textContent; // Ŭ���� ����Ʈ �������� ����
        
        const url = `/posting?sort=${sort}&subject=${encodeURIComponent(subject)}`;
        window.location.href = url; // ������ ���𷺼�
    });
});
# Greeting.js

`document.querySelector()`를 통해서 해당 html태그, id, class를 가져올 수 있다. 이 함수는 한 개의 값만 불러오며, 같은 class를 쓰는 여러 태그들을 가져오기 위해선 All을 붙여 사용한다.

```jsx
const loginForm = document.querySelector("#login-form");
```

### 변수 설정

- `const` 초기화가 되어야 하며 수정이 불가능하다. 대게로 이 타입으로 선언한다.
- `let` 변수의 수정이 가능하다.

### Class관리

- `document.querySelector()` 통해 정보를 받아서 변수에 저장을 하였다. `.classList` 를 통해 객체가 가지고 있는 클래스들을 전부 살펴볼 수 있고, 클래스를 넣고 빼는 작업을 할 수 있다.

```css
.hidden{
    display: none;
}
```

예를 들어 `.hidden` 라는 클래스를 넣고 빼는 작업을 함으로써 페이지의 요소들을 관리할 수 있다.

- `객체.innerText` 를 통해 HTML내부의 텍스트를 바꿀 수 있다.

### formating

`“문자열”` 나 `‘문자열’` 가 아닌 ``${변수명}`` 를 이용하여 format을 할 수 있다. 

### localstroage

브라우저에는 localstorage가 존재한다. 브라우저 내에 작은 데이터베이스와 같다. `form` 태그를 통해 제출하게 되거나, 웹이 새로 고침 될 경우 브라우저 내 데이터는 초기화가 된다. 이를 방지하기 위해서 localstorage에 접근한다. `localstorage.setItem(key, value)` 로 설정할 수 있다. 이용 방법은 dictinary와 매우 유사하다. 

### EventListner

폼을 ‘제출’ 하거나 또는 버튼을 ‘클릭’ 그 외의 많은 이벤트가 발생한다. `document.querySelector()` 로 객체를 받아 저장하고, 해당 객체에 대해 `.addEventListener("이벤트", 함수)` 를 통해 해당 이벤트가 발생했을 때 함수를 작동할 수 있다. 함수를 인자로 사용할 때 ()를 넣지 않도록 한다.

- 작동 시킬 함수를 구현할 때, 함수의 파라미터로 event를 넣을 수 있다. `event.preventDefault()` 를 통해 해당 이벤트가 발생하는 것을 막을 뿐더러 다른 메소드를 활용하여 다양한 코드를 완성할 수 있다.

---

# clocks.js

### Date()

- `const date = new Date();` 코드를 통해 현재 시간을 불러올 수 있다. 객체에 매소드를 활용하여 시간, 날짜, 및 년도를 불러낼 수 있다.
- `setInterval(함수, 초)` 해당 함수가 지정한 초를 간격으로 실행되게 한다.
- `.padStart(숫자, "문자")` 해당 string 객체 앞을 지정한 숫자에 맞게 문자를 채워 넣는다.

---

# quotes.js

### Math

- `Math.floor` 숫자를 내림한다.
- `Math.random()` 0부터 1사이의 숫자를 랜덤하게 표출한다. 원하는 범위가 있다면, 그 숫자만큼 곱하면 된다.

---

# background.js

### HTML태그 만들기

- `document.createElement("태그")` 문서 내에 태그를 만들 수 있다.
    - 태그가 생성되면 해당 태그가 가지는 속성 또한 js내에서 수정 가능한다.
- `.appendChild(태그 변수)` 태그를 위치할 곳을 지정한다. 해당 객체의 자식 요소로 들어간다.

---

# weather.js

### 위치를 나타내는 함수

```jsx
navigator.geolocation.getCurrentPosition(onGeoOk,onGeoError);
```

js에 기본으로 깔려있는 모듈이다. 첫 번째 인자는 현재 위치를 이벤트로 받는다`. coords` 를 통해 위도와 경도를 구할 수 있다.

```jsx
fetch(url).then(response => response.json())
    .then((data) => {
        const weather = document.querySelector("#weather span:first-child");
        const city = document.querySelector("#weather span:last-child");
        city.innerText = data.name;
        weather.innerText = `${data.weather[0].main} / ${data.main.temp}`;
    })
```

- fetch로 url을 불러온다. 이 작업은 시간을 오래 잡아먹는데 컴퓨터는 pipeline 형태로 동시 다발적으로 작업을 진행한다. 따라서 해당 데이터를 얻기도 전에 관련 코드를 실행해버릴 수 있다는 것이다.
- `.then` 은 객체가 실행되어야 다음 코드가 실행될 수 있게 진행한다. `response` 로 데이터를 불러오고 `json` 언어로 변환시킨다. 또한 관련 데이터들을 저장하여 활용할 수 있다.

---

# toDo.js

앞서 언급한 개념들을 적극 활용한다. 

to do 목록을 만들고 지우는 작업을 한다. 하지만 지울 시 목록의 내용이 같으면 두 개의 목록이 동시에 지워지기 때문에 각 항목에 대한 ID를 만들기로 한다. → Date를 이용한 시간대 별로 다른 값 적용

- to do 리스트가 브라우저 내에 저장되게 하여금 log in 하였을 때 목록이 표시되도록 한다.
    - 리스트 내용을 localstorage에 저장한다. 하지만 이 DB는 string만 가능하기 때문에 타입 변환 시켜줘야 한다. → `JSON.stringify(객체)` 로 타입 변환 시킬 수 있다.
    - filter함수 내 lamda식을 활용하여 리스트를 조정할 수 있다.
    
    ```jsx
    	 toDos = toDos.filter((toDo) => toDo.id !== parseInt(li.id));
    ```
    

---
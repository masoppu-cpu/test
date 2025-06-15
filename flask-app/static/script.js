function sayHello() {
  alert("JavaScript 動いてるで！✨");
}

fetch('/static/test.json')
.then(response => {
  return response.json();
})
.then(data => {
   const p = document.createElement('p');
   p.textContent = data.name;
   document.getElementById('test').appendChild(p);
})
  .catch(error => {
    console.log("エラー発生:", error);
  });

function getHello(){
  fetch('/hello')
  .then(response => {
  return response.text();
})
.then(data => {
   alert("とってきた値・・" + data);
})
  .catch(error => {
    console.log("エラー発生:", error);
  });
}

function getPosts(){
  fetch('/get_posts')
  .then(response => {
  return response.json();
})
.then(data => {
   alert("OK"+ data);
})
  .catch(error => {
    console.log("エラー発生:", error);
  });
}
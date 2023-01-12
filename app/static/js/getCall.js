// function httpGet(theUrl="http://localhost:8000/media/video/slug.avi") {
//     console.log("theUrl yes get is called" );
//     let xmlHttpReq = new XMLHttpRequest();
//     xmlHttpReq.open("GET", theUrl, false); 
//     xmlHttpReq.send(null);
//     return xmlHttpReq.responseText;
//   }
// console.log("js file");
function create(value = "function"){
  console.log(value)
  console.log("yes bro its working function");
}

const fileInput = document.querySelector('#folder');
const loder = document.querySelector('.loder');
const toggleLoder = function() {
  loder.classList.add('active');
  setTimeout(() => {
    loder.classList.remove('active');
  }, 10000);
}
fileInput.addEventListener('change',toggleLoder);

function downloadFile(urlToSend) {
  var req = new XMLHttpRequest();
  req.open("GET", urlToSend, true);
  req.responseType = "blob";
  req.onload = function (event) {
      var blob = req.response;
      // var fileName = req.getResponseHeader("fileName") //if you have the fileName header available
      var link=document.createElement('a');
      link.href=window.URL.createObjectURL(blob);
      // link.download=fileName;
      link.click();
  };

  req.send();
}

const button = document.querySelector('button')

// function passAuthCode(){
//     const search_parameter = window.location.search
//     const code = search_parameter.split("=")[1]
//     const url = `http://127.0.0.1:5000/code/${code}`
//     fetch(url)
//       .then(response => response.json())
//       .then(data => console.log(data))
//     window.close()
// }

 const showCode = () =>{
   const codeInput = document.querySelector('.code')
   const search_parameter = window.location.search
   const code = search_parameter.split("=")[1]
   codeInput.value = code
   codeInput.select(); // select the text
   document.execCommand("copy"); // copy text
   window.close()
 }

button.addEventListener('click', showCode)
// button.addEventListener('click', passAuthCode)
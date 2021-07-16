import axios from "axios";
const button = document.querySelector("button");

async function passAuthCode() {
  const search_parameter = window.location.search;
  const code = search_parameter.split("=")[1];
  const url = "http://127.0.0.1:5000/code/";
  const res = await axios.post(url, { code });
  console.log(res)
  window.close();
}
button.addEventListener("click", passAuthCode);

//  const showCode = () =>{
//    const codeInput = document.querySelector('.code')
//    const search_parameter = window.location.search
//    const code = search_parameter.split("=")[1]
//    codeInput.value = code
//    codeInput.select(); // select the text
//    document.execCommand("copy"); // copy text
//    window.close()
//  }

// button.addEventListener('click', showCode)

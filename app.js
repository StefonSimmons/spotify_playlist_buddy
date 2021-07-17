const form = document.querySelector("form");

async function passAuthCode(e) {
  e.preventDefault()
  const search_parameter = window.location.search;
  const code = search_parameter.split("=")[1];
  const url = "http://127.0.0.1:5000/code/";
  try {
    const res = await axios.post(url, { code });
    console.log(res)
    // window.close();
  } catch (error) {
    console.error(error.message)
  }
}
form.addEventListener("submit", passAuthCode);

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

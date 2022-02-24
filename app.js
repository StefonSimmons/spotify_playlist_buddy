
const button = document.querySelector('button')


const codeInput = document.querySelector('.code')
const search_parameter = window.location.search
const code = search_parameter.split("=")[1]
codeInput.value = code

const showCode = () => {
  codeInput.select(); // select the text
  document.execCommand("copy"); // copy text
  window.close()
}

button.addEventListener('click', showCode)

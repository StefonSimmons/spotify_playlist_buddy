
const button = document.querySelector('button')


const codeInput = document.querySelector('.code')
const search_parameter = window.location.search
const code = search_parameter.split("=")[1]
codeInput.value = code

const showCode = async () => {
  codeInput.select(); // select the text
  await navigator.clipboard.writeText(codeInput.value) // copy text
  window.close()
}

button.addEventListener('click', showCode)

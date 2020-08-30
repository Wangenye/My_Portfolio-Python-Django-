let sHow = false

const element = document.getElementById('Menu-bar')
const el2 = document.getElementsByClassName('menu')

element.addEventListener('click', () => {
    element.classList.add('active')
    el2.classList.add('showMenu')
    sHow = true
})


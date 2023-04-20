var botao = document.getElementById("botao")
var limpar = document.getElementById("botao_limpar")

botao.addEventListener('click', function() {
    var paragrafo = document.getElementById('paragrafo');

    paragrafo.textContent = 'O texto deste parágrafo foi alterado!'
})

limpar.addEventListener('click', function() {
    var texto = document.getElementById('paragrafo');

    texto.textContent = ''
})
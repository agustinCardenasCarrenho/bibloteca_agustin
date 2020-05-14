var selects = document.getElementsByClassName('slc')
var formUpdateProgress = document.getElementById('form')
var iCantPages = document.getElementById('cantPages')
var btns = document.getElementsByClassName('btn btn-primary')
var currentPage = document.getElementById('currentPage')
var book_id , cantpages

//cambia el estado del libro

function changebookState(book_id , state){
    fetch('http://localhost:8000/book/update/'+book_id+'/'+state).then(function(res){
        window.location.replace(res.url)
    })
}

for (let index = 0; index < selects.length; index++) {
    selects[index].onchange = function () {
       book_id = this.attributes[1].value 
       changebookState(book_id,this.value)
    }
}


//actualiza el progreso del libro 
for (let index = 0; index < btns.length; index++) {
     btns[index].onclick = function(){
        book_id = parseInt(this.attributes[4].value)
        cantpages = parseInt(this.attributes[5].value)
        iCantPages.setAttribute('value' , cantpages)
     }
}

$("#modalUpdateProgress").on("hidden.bs.modal", function () {
    formUpdateProgress.reset()
});

formUpdateProgress.addEventListener('submit' , function(e){
    e.preventDefault()
    currentPage.value <= cantpages ? updateBookProgress(book_id, currentPage.value) : alert("La cantidad de paginas ingresadas en mayor a la cantidad de paginas del libro")
})

function updateBookProgress(book_id , currentPage){
    if(currentPage == cantpages)  changebookState(book_id , 1) 
    fetch('http://localhost:8000/book/update/bookprogress/'+book_id+'/'+currentPage).then(function(e){
        location.reload()
    })
}

var selects = document.getElementsByClassName('slc')
var formUpdateProgress = document.getElementById('form')
var iCantPages = document.getElementById('cantPages')
var btns = document.getElementsByClassName('btn btn-primary')
var currentPage = document.getElementById('currentPage')
var book_id , cantpages
var user_id = document.getElementsByName('user_id')[0].value

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
    currentPage.value <= cantpages ? updateBookProgress(book_id, user_id, currentPage.value) : alert("La cantidad de paginas ingresadas en mayor a la cantidad de paginas del libro")
})




function updateBookProgress(book_id ,user_id , currentPage){
    let data = new FormData();
    data.append('book_id', book_id)
    data.append('user_id', user_id)
    data.append('current_page', currentPage)
    data.append('csrfmiddlewaretoken' , document.getElementsByName('csrfmiddlewaretoken')[0].value)
    fetch('http://localhost:8000/book/update/bookprogress',{
        method : 'POST',
        body : data,
        credentials: 'same-origin',
    }).then(function(e){
        location.reload() 
    })
}


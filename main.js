let btnAdd = document.getElementById('btn');
let userMess = document.getElementById('userMess');
let mess = document.getElementById('enterMsg');
let btnSubmit = document.getElementById('btn');

btnSubmit.onclick = async function(){
    let resMess ;
    try{
        await fetch('http://127.0.0.1:5000/res',{
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body : JSON.stringify({"mess": mess.value})
        })
        .then(response => response.json())
        .then(data => resMess = data.res)
        .catch(error => console.log(error));
    }catch(err){
        console.log(err);
    }
        userMess.innerHTML += `<div class="container" id="IdFirst">
            <p id="firstMsg">${mess.value}</p>
        </div>` + `<div class="container" id="IdSec">
            <p id="secondMsg"> ${resMess}</p>
        </div>`;
        mess.value = "";
    
    
}




import loadRateUP from "./character_randomizer.js"


const rolling = document.getElementById("rollDiv")
const inventory = document.getElementById("invDiv")
const characters = document.getElementById("charDiv")
const battle = document.getElementById("battleDiv")
const content = document.getElementById("contentDiv")




function renderRolling(){
    content.innerHTML=''
    let html = 
    `
        <div class="container text-center">
            <div><h3>ROLL U NIGG</h3></div>
            <div class="mt-2">
              <img src="" alt="" class="img1">
              <img src="" alt="" class="img1">
              <img src="" alt="" class="img1">
              <img src="" alt="" class="img1">
              
            </div>
            <div><button>ROLL</button></div>
        </div>
    `


    let newServ = document.createElement('div');
    newServ.classList.add('productcard');
    newServ.innerHTML = html;
    content.append(newServ);
    loadRateUP()
}


function renderCharacters(){
    content.innerHTML=''
    let html = 
    `
        <div>
            <div class="container">
                
              <div class="row">
                <div class="col-2">
                  <img src="./image/base/characters/alice.png" alt="" srcset="">
                </div>
                <div class="col-10">
                  <div><h3>Alice</h3></div>
                  <div>
                    <h4>HP:100</h4>
                    <h4>ATK:100</h4>
                    <h4>MAGI:100</h4>
                    <h4>DEF:100</h4>
                  </div>
                </div>
              </div>
              <hr>
              <div class="row">
                <div class="col-2">
                  <img src="./image/base/characters/alice.png" alt="" srcset="">
                </div>
                <div class="col-10">
                  <div><h3>Alice</h3></div>
                  <div>
                    <h4>HP:100</h4>
                    <h4>ATK:100</h4>
                    <h4>MAGI:100</h4>
                    <h4>DEF:100</h4>
                  </div>
                </div>
              </div>
              <hr>

            </div>
          </div>
    `


    let newServ = document.createElement('div');
    newServ.classList.add('productcard');
    newServ.innerHTML = html;
    content.append(newServ);
    loadRateUP()
}


function renderInventory(){
    content.innerHTML=''
    let html = 
    `
        <div class="text-center pe-3">
            <h3>INVENTORY</h3>
            <div class="row">
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
            </div>
            <div class="row">
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3">a</div>
            </div>
            <div class="row">
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3 ">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3 ">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3 ">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3 ">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3 ">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3 ">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3 ">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3 ">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3 ">a</div>
              <div class="col border border-1 pt-3 pb-3 ms-1 mt-1 rounded rounded-3 border border-3 ">a</div>
            </div>
          </div>
       
    `


    let newServ = document.createElement('div');
    newServ.classList.add('productcard');
    newServ.innerHTML = html;
    content.append(newServ);
    loadRateUP()
}



rolling.addEventListener('click',renderRolling)
inventory.addEventListener('click',renderInventory)
characters.addEventListener('click',renderCharacters)

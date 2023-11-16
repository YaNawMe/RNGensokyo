import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.6.0/firebase-app.js';
import { getDatabase, ref, get, set, child } from 'https://www.gstatic.com/firebasejs/10.6.0/firebase-database.js';

// --- GLOBAL VARIABLES ---
const firebaseConfig = {
    apiKey: "AIzaSyCo-Hj5cdVvLJfrSJpT7zQEvnL3KK_NCDU",
    authDomain: "rngensokyo.firebaseapp.com",
    databaseURL: "https://rngensokyo-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "rngensokyo",
    storageBucket: "rngensokyo.appspot.com",
    messagingSenderId: "62753174974",
    appId: "1:62753174974:web:9414b07e3baeed0901b5ef"
};
const app = initializeApp(firebaseConfig);
const database = getDatabase(app)

// --- GAME VARIABLES ---
var char_chances = {
    "Rumia": {"chance": 0.75, "stats": {"attack": 5, "defense": 7}},
    "Poi": {"chance": 0.5, "stats": {"attack": 10, "defense": 14}},
    "Fumog": {"chance": 0.05, "stats": {"attack": 50, "defense": 35}}
}

// --- CLASS ---//
function Enum(values) {
    const enumObject = {};

    for (const val of values) {
        enumObject[val] = val;
    }

    return Object.freeze(enumObject);
}

class FireBase {
    constructor() {
        this.ID_List = [];
    }
    
    addData(character){
        var json = this.getData()
        console.log(json)
        json.forEach(element => {
            this.ID_List.push(element);
        });
        
        try {
            set(ref(database, 'GameDatabase/' + (this.ID_List.length + 1)),
            {
                character_name: character 
            })
        }
    
        catch(error) {
            alert("boom sumabog")
        }
    }

    getData(){
        this.ID_List = []
        get(child(ref(database),`GameDatabase/`)).then((snapshot)=>{
            if (snapshot.exists()){
                console.log(snapshot)
                return snapshot;
            }
        })
    }
}
//peenis 8======D
class Gacha {
    constructor() {
        this.chance_list = "";
    }

    roll()
    {
        const current_roll = Math.random();
        
        this.chance_list = Object.keys(char_chances);
        this.chance_list = this.chance_list.filter(
            function(key){
                return current_roll <= char_chances[key]["chance"];
            }
        );
    
        change_text.innerHTML = "Roll Value: " + current_roll.toString() + "\nCharacter Got: " + this.chance_list.toString();
    }
}


// --- CLASS INIT ---//
const gacha = new Gacha();
const firebase = new FireBase();

// --- HTML ELEMENTS ---
// window.addEventListener("load", Test.print_statement);
const change_text = document.getElementById("change_text");
const roll_button = document.getElementById("roll_button");
const get_button = document.getElementById("get_button");

// --- HTML FUNCTIONS ===
roll_button.addEventListener("click", function(){
    gacha.roll();
    firebase.addData(gacha.chance_list);
})

get_button.addEventListener("click", function(){
    firebase.getData();
})

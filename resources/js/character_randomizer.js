const rateup_characters = "";
var img_holders = document.getElementsByClassName("img1")

const images_list = [
    "alice.png",
    "aya.png",
    "byakuren.png",
    "chen.png",
    "cirno.png",
    "daiyousei.png",
    "eiki.png",
    "eirin.png",
    "flandre.png",
    "hieda.png",
    "hina.png",
    "hong.png",
    "ichirin.png",
    "iku.png",
    "kaguya.png",
    "kanako.png",
    "keine.png",
    "keineyoukai.png",
    "kisume.png",
    "koakuma.png",
    "kogasa.png",
    "koishi.png",
    "komachi.png",
    "letty.png",

]

function loadRateUP(){
    console.log(img_holders.length)
    for (var i = 0; i!=img_holders.length;i++){
        
        var random = Math.floor(Math.random() * images_list.length);
        img_holders[i].src = "./image/base/characters/"+images_list[random]
    }
}

export default loadRateUP


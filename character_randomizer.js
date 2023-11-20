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
    "eirin.png"     
]

for (var i in img_holders){
    var random = Math.floor(Math.random() * 7);
    img_holders[i].src = "./img/"+images_list[random]
}


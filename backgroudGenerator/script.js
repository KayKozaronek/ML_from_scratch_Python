var css = document.querySelector("h3");
var color1 = document.querySelector(".color1");
var color2 = document.querySelector(".color2");
var body = document.getElementById("gradient");
var randomBtn = document.getElementById("randomBtn");

console.log(randomBtn);

function setGradient(){
    body.style.background = 
        "linear-gradient(to right,"
        + color1.value + "," + color2.value + ")";
    
    css.textContent = body.style.background + ";";
}

function randomColor(){
    return "rgba(" 
        + Math.floor(Math.random()*255) + "," 
        + Math.floor(Math.random()*255) + "," 
        + Math.floor(Math.random()*255) + ","
        + Math.random().toFixed(2) + ")";

    /*return "#" + Math.floor(Math.random()*99) +  
        + Math.floor(Math.random()*99) +  
        + Math.floor(Math.random()*99); 
    */
}

function setRandomGradient(){
    let colorA = randomColor();
    let colorB = randomColor();

    body.style.background = 
        "linear-gradient(to right,"
        + colorA + "," + colorB + ")";

    css.textContent = body.style.background + ";"; 
}

window.addEventListener("load", setGradient)

color1.addEventListener("input", setGradient)

color2.addEventListener("input", setGradient)

randomBtn.addEventListener("click", setRandomGradient)

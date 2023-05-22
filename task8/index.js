"use strict";
//this is a mode in js where it helps in finding common coding mistakes and helps in writing good code
var audio1 = new Audio();
//this(var is variable declaration in js) creates audio object and assigns it to the variable audio1
audio1.src = "sounds/crash.mp3";
//this provide the path to the audio file and locates to this file.
const btnw = document.querySelector(".w");
//This selects the HTML element with class 'w' using document.querySelector(), and assigns it to the variable btnw.
btnw.addEventListener("click", function (e) {
  e.preventDefault();
  audio1.play();
});
/*An event listener is added to btnw that listens for a click event.
When the button is clicked, the function is executed. It prevents the default behavior
of the click event using e.preventDefault().Finally it calls 'audio.play()' to play the audio file associated with
'audio'
*/
const handleKeyPressW = function (e) {
  if (e.key === "w") {
    btnw.click();
  }
};
document.addEventListener("keydown", handleKeyPressW);

var audio2 = new Audio();
audio2.src = "sounds/tom-1.mp3";
const btna = document.querySelector(".a");
btna.addEventListener("click", function (e) {
  e.preventDefault();
  audio2.play();
});

const handleKeyPressA = function (e) {
  if (e.key === "a") {
    btna.click();
  }
};
document.addEventListener("keydown", handleKeyPressA);

var audio3 = new Audio();
audio3.src = "sounds/snare.mp3";
const btns = document.querySelector(".s");
btns.addEventListener("click", function (e) {
  e.preventDefault();
  audio3.play();
});

const handleKeyPressS = function (e) {
  if (e.key === "s") {
    btns.click();
  }
};
document.addEventListener("keydown", handleKeyPressS);

var audio4 = new Audio();
audio4.src = "sounds/kick-bass.mp3";
const btnd = document.querySelector(".d");
btnd.addEventListener("click", function (e) {
  e.preventDefault();
  audio4.play();
});

const handleKeyPressD = function (e) {
  if (e.key === "d") {
    btnd.click();
  }
};
document.addEventListener("keydown", handleKeyPressD);

var audio5 = new Audio();
audio5.src = "sounds/tom-2.mp3";
const btnj = document.querySelector(".j");
btnj.addEventListener("click", function (e) {
  e.preventDefault();
  audio5.play();
});

const handleKeyPressJ = function (e) {
  if (e.key === "j") {
    btnj.click();
  }
};
document.addEventListener("keydown", handleKeyPressJ);

var audio6 = new Audio();
audio6.src = "sounds/tom-3.mp3";
const btnk = document.querySelector(".k");
btnk.addEventListener("click", function (e) {
  e.preventDefault();
  audio6.play();
});

const handleKeyPressK = function (e) {
  if (e.key === "k") {
    btnk.click();
  }
};
document.addEventListener("keydown", handleKeyPressK);

var audio7 = new Audio();
audio7.src = "sounds/tom-4.mp3";
const btnl = document.querySelector(".l");
btnl.addEventListener("click", function (e) {
  e.preventDefault();
  audio7.play();
});

const handleKeyPressL = function (e) {
  if (e.key === "l") {
    btnl.click();
  }
};
document.addEventListener("keydown", handleKeyPressL);

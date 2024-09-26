"use strict";

const form1 = document.getElementById("form1")
const form2 = document.getElementById("form2")
const form3 = document.getElementById("form3")

const progressEL = document.getElementById('progress')
const circles = document.getElementById('.circle')


let currentActive = 1;
//==============Next Form============
function nextOne(){
    form1.style.left = "-500px";
    form2.style.left = "25px";
}

//==============Second Form============
function nextTwo(){
    form2.style.left = "-500px";
    form3.style.left = "25px";
}   

// =================btn Events=================

const btnsEvent = () => {
    const next1 = document.getElementById('next1')
    const next2 = document.getElementById('next2')
    const back1 = document.getElementById('back1')
    const back2 = document.getElementById('back2')

    //=====next1=======
    next1.addEventListener('click', nextOne)

    //=====next2=======
    next2.addEventListener('click',nextTwo)

};

document.addEventListener("DOMContentLoaded", btnsEvent);
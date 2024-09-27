"use strict";

const form1 = document.getElementById("form1")
const form2 = document.getElementById("form2")
const form3 = document.getElementById("form3")
const form4 = document.getElementById("form4")

const progressEL = document.getElementById('progress')
const circle = document.getElementById('.circle')


let currentActive = 1;
//==============Second Form============
function nextOne(){
    form1.style.left = "-500px";
    form2.style.left = "25px";

    // next progress number
    currentActive++;
    if(currentActive> circle.length){
        currentActive = circle.length;
    }

    // update 
    update();
}


// ==========Back One=================
function backOne(){
    form1.style.left = "25px";
    form2.style.left = "500px";
}

//==============Third Form============
function nextTwo(){
    form2.style.left = "-500px";
    form3.style.left = "25px";
}   
// ==========Back Two=============
function backTwo(){
    form2.style.left = "25px";
    form3.style.left = "500px";
}
// ==========Fourth Form================
function nextThree(){
    form3.style.left = "-500px";
    form4.style.left = "25px";
}
// ==========Back Three=============
function backThree(){
    form3.style.left = "25px";
    form4.style.left = "500px";
}


// =================progress Update=================
function update(){
    circle.forEach((circle,indx) =>{
    
        if(indx < currentActive){
            circle.classList.add('active');
        }
        else{
            circle.classList.remove('active');
        }

    })

}


// =================btn Events=================

const btnsEvent = () => {
    const next1 = document.getElementById('next1')
    const next2 = document.getElementById('next2')
    const next3 = document.getElementById('next3')
    const Back1 = document.getElementById('Back1')
    const Back2 = document.getElementById('Back2')
    const Back3 = document.getElementById('Back3')

    //=====next1=======
    next1.addEventListener('click', nextOne);

    // ====Back 1======
    Back1.addEventListener('click',backOne);

    //=====next2=======
    next2.addEventListener('click',nextTwo);

    //=====Back2======== 
    Back2.addEventListener('click',backTwo);

    //=====next3=======
    next3.addEventListener('click',nextThree);

    //=====Back3======== 
    Back3.addEventListener('click',backThree);

    

};

document.addEventListener("DOMContentLoaded", btnsEvent);

document.getElementById("form4").addEventListener("submit", function(e) {
    e.preventDefault(); // Prevent the default form submission action

    // Hide the form
    document.querySelector(".container").style.display = "none";

    // Show the thank you message
    document.getElementById("thankyouMessage").style.display = "block";
});

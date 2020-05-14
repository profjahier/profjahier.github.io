"use strict";

function toggleAffichage(elt, suivant){
    let selection = elt.parentElement.nextElementSibling;
    if(suivant == 2){
        selection = selection.nextElementSibling;
    }
    console.log(selection.style.display);
    console.log(getComputedStyle(selection).display);
    if (getComputedStyle(selection).display == "none"){
        selection.style.display = "block";
    }else{
        selection.style.display = "none";
    }

}
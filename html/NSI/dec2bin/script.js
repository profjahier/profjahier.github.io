"use strict";

function convertir(){
    let n = document.getElementById("n").value;
    n = Number(n);
    let reste;
    let binaire = '';
    let signe = '';
    if (isNaN(n)){
        alert("Entre un nombre !");
    } else if (!(Number.isInteger(n)) || n < 0){
        alert("Entre un entier positif !");
    } else if (n === 0){
        document.getElementById("reponse").textContent = '0';
    } else{
        while (n !== 0){
            reste = n % 2;
            binaire = reste.toString() + binaire;
            n = Math.trunc(n/2);
            console.log(n, reste, binaire);
        }
        document.getElementById("reponse").textContent = signe + binaire;
    }
}
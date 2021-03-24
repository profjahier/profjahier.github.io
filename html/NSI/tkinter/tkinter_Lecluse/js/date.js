"use strict";

let mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "décembre"];
let jours = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"];
let d = new Date();
let j = d.getDay();
let jj = d.getDate();
let m = d.getMonth();

let date = document.getElementById("date");
date.textContent = jours[j] + ' ' + jj + ' ' + mois[m];

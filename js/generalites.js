/*
// Le snippet ci-dessous devrait transformer tous les liens qui ne correspondant pas à ce nom  de domaine avec un attribut target à la valeur _blank.

let liens = document.getElementsByTagName('a');
for (let a of liens){
  if (a.href != location.hostname){ // Attention ça ne marche plur l'instant !!!!
    a.setAttribute("target", "_blank")
  }
}
*/  
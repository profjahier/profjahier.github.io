/*
// Le snippet ci-dessous devrait transformer tous les liens qui ne correspondant pas à ce nom  de domaine avec un attribut target à la valeur _blank.

let liens = document.getElementsByTagName('a');
for (let a of liens){
  if (a.href != location.hostname){ // Attention ça ne marche plur l'instant !!!!
    a.setAttribute("target", "_blank")
  }
}
*/  

function menu_page(){
  let titres = document.getElementsByTagName('h2');
  let menu = document.getElementById('menu_page');
  liste = document.createElement('ol');
  menu.appendChild(liste);
  for (let i in titres){
    let titre = titres[i].textContent;
    titres[i].setAttribute('id', titre+i);
    item = document.createElement('li');
    lien = document.createElement('a');
    lien.setAttribute('href', '#'+titre+i);
    lien.setAttribute('onclick', 'efface_menu()');
    lien.textContent = titre;
    item.appendChild(lien);
    liste.appendChild(item);
  }
}

function efface_menu(){
  let menu = document.getElementById('menu_page');
  menu.innerHTML = "";
}


function fleche_up(){
  let titres = document.getElementsByTagName('h2');
  for (let i in titres){
    let titre = titres[i].textContent;
    titres[i].innerHTML = "<a href='#'><img src='../../img/up.png' alt='retour haut de page' height='20'/></a> " + titre;
  }
}

fleche_up();

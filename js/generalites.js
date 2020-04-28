// *******************************************************************************************************************
// Transforme tous les liens qui ne correspondant pas à ce nom  de domaine avec un attribut target à la valeur _blank.
let liens = document.getElementsByTagName('a');
for (let lien of liens){
  let url = new URL(lien.href);
  if (url.hostname != location.hostname){ 
  lien.setAttribute("target", "_blank");
  } 
}

// ********************************************************************************************************************
// Crée un menu de navigation automatique qui est inséré parès le titre h1 de chaque page automatiquement 
let domaine = "https://"+location.hostname;
let navHTML = ' <nav><a href="#" onclick="creer_menu_page()"><img src="'+domaine+'/img/sommaire.png" alt="- Sommaire -" height="30"></a><a href="index.html"><img src="'+domaine+'/img/racine.png" alt="- Home -" height="30"></a><a href="../index.html"><img src="'+domaine+'/img/sortie.png" alt="- Quitter -" height="30"></a><div id="menu_page"></div></nav>';
document.querySelector('h1').insertAdjacentHTML('afterend', navHTML);

// ********************************************************************************************************************
// Crée un menu de la page en cours (liste des titres h2) si clic sur icone de menu
let menu_on = false;

function creer_menu_page(){
  if (!menu_on){
    let titres = document.getElementsByTagName('h2');
    let menu = document.getElementById('menu_page');
    liste = document.createElement('ol');
    menu.appendChild(liste);
    for (let i=0; i<titres.length; i++){
      let titre = titres[i].textContent;
      titres[i].setAttribute('id', titre+i);
      item = document.createElement('li');
      lien = document.createElement('a');
      lien.setAttribute('href', '#'+titre+i);
      lien.setAttribute('onclick', 'effacer_menu()');
      lien.textContent = titre;
      item.appendChild(lien);
      liste.appendChild(item);
    }
    menu_on = true;
  }
}

function effacer_menu(){ // Efface le menu dès qu'on clique sur un lien
  let menu = document.getElementById('menu_page');
  menu.innerHTML = "";
  menu_on = false;
}

// ********************************************************************************************************************
// Ajoute une fleche de retour en haut de page devant chaque titre h2
function fleche_up(){
  let titres = document.getElementsByTagName('h2');
  for (let i in titres){
    let titre = titres[i].textContent;
    titres[i].innerHTML = "<a href='#'><img src='"+domaine+"/img/up.png' alt='&#8593;' height='20'/></a> " + titre;
  }
}

fleche_up();

// ********************************************************************************************************************
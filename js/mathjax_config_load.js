// Définir ci-dessous la configuration spécifique désirée
window.MathJax = {
  loader: {load: ['[tex]/mhchem', '[tex]/physics', '[tex]/ams']},
  tex: {packages: {'[+]': ['mhchem', 'physics', 'ams']}, }
};

// fonction qui charge la librairie MathJax automatiquement
(function () {
  var script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js'; // choisir ici la configuration par défaut à charger
  script.async = true;
  document.head.appendChild(script);
})();
var Cookie = {
  set: function(name, value, daysToExpire) {
    var expire = '';
    if (daysToExpire != undefined) {
      var d = new Date();
      d.setTime(d.getTime() + (86400000 * parseFloat(daysToExpire)));
      expire = '; expires=' + d.toGMTString();
    }
//    return (document.cookie = escape(name) + '=' + escape(value || '') + expire);
    return (document.cookie = escape(name) + '=' + (value || '') + expire + '; path=/');
  },
  get: function(name) {
    var cookie = document.cookie.match(new RegExp('(^|;)\\s*' + escape(name) + '=([^;\\s]*)'));
    return (cookie ? unescape(cookie[2]) : null);
  },
  erase: function(name) {
    var cookie = Cookie.get(name) || true;
    Cookie.set(name, '', -1);
    return cookie;
  },
  accept: function() {
    if (typeof navigator.cookieEnabled == 'boolean') {
      return navigator.cookieEnabled;
    }
    Cookie.set('_test', '1');
    return (Cookie.erase('_test') === '1');
  }
};

function adjustView(which) {
    if (which=='tcl') {
        $('.tcl').addClass('tclplain').removeClass('tcl')
        $('.tclhidden').addClass('tclplain').removeClass('tclhidden')
        $('.ruby').addClass('rubyhidden').removeClass('ruby')
        $('.rubyplain').addClass('rubyhidden').removeClass('rubyplain')
        $('.perl').addClass('perlhidden').removeClass('perl')
        $('.perlplain').addClass('perlhidden').removeClass('perlplain')
        $('.python').addClass('pythonhidden').removeClass('python')
        $('.pythonplain').addClass('pythonhidden').removeClass('pythonplain')
        Cookie.set('tlang', 'tcl');
    } else if (which=='ruby') {
        $('.ruby').addClass('rubyplain').removeClass('ruby')
        $('.rubyhidden').addClass('rubyplain').removeClass('rubyhidden')
        $('.tcl').addClass('tclhidden').removeClass('tcl')
        $('.tclplain').addClass('tclhidden').removeClass('tclplain')
        $('.perl').addClass('perlhidden').removeClass('perl')
        $('.perlplain').addClass('perlhidden').removeClass('perlplain')
        $('.python').addClass('pythonhidden').removeClass('python')
        $('.pythonplain').addClass('pythonhidden').removeClass('pythonplain')
        Cookie.set('tlang', 'ruby');
    } else if (which=='perl') {
        $('.perl').addClass('perlplain').removeClass('perl')
        $('.perlhidden').addClass('perlplain').removeClass('perlhidden')
        $('.tcl').addClass('tclhidden').removeClass('tcl')
        $('.tclplain').addClass('tclhidden').removeClass('tclplain')
        $('.ruby').addClass('rubyhidden').removeClass('ruby')
        $('.rubyplain').addClass('rubyhidden').removeClass('rubyplain')
        $('.python').addClass('pythonhidden').removeClass('python')
        $('.pythonplain').addClass('pythonhidden').removeClass('pythonplain')
        Cookie.set('tlang', 'perl');
    } else if (which=='python') {
        $('.python').addClass('pythonplain').removeClass('python')
        $('.pythonhidden').addClass('pythonplain').removeClass('pythonhidden')
        $('.tcl').addClass('tclhidden').removeClass('tcl')
        $('.tclplain').addClass('tclhidden').removeClass('tclplain')
        $('.ruby').addClass('rubyhidden').removeClass('ruby')
        $('.rubyplain').addClass('rubyhidden').removeClass('rubyplain')
        $('.perl').addClass('perlhidden').removeClass('perl')
        $('.perlplain').addClass('perlhidden').removeClass('perlplain')
        Cookie.set('tlang', 'python');
    } else {
        $('.tclplain').addClass('tcl').removeClass('tclplain')
        $('.tclhidden').addClass('tcl').removeClass('tclhidden')
        $('.rubyplain').addClass('ruby').removeClass('rubyplain')
        $('.rubyhidden').addClass('ruby').removeClass('rubyhidden')
        $('.perlplain').addClass('perl').removeClass('perlplain')
        $('.perlhidden').addClass('perl').removeClass('perlhidden')
        $('.pythonplain').addClass('python').removeClass('pythonplain')
        $('.pythonhidden').addClass('python').removeClass('pythonhidden')
        Cookie.erase('tlang');
    }
}

function setDefaultLang() {
    var l = Cookie.get('tlang')
    if (l!=null) {
        $('#languageselect').val(l)
        adjustView(l)
    }
}

function getPlatform() {
    if (navigator.platform.startsWith("Mac")) {return "mac";}
    if (navigator.platform.startsWith("Linux")) {return "x11";}
    return "win";
}

function installpicker_setup() {
    var l = Cookie.get('tlang')
    if (l==null) {l = 'python';}
    $("#lang"+l).click();
    var p = getPlatform();
    $("#plat"+p).click();
    $("#plat"+p).blur();
}

function installpicker_navigate() {
    var l = Cookie.get('tlang')
    var lang = $("input[name='lang']:checked").val();
    var plat = $("input[name='plat']:checked").val();
    if (l!=null && l!=lang) {
        $('#languageselect').val("all")
        adjustView("")
    }
    gtag('event', plat+'/'+lang, {'event_category': 'install'});
    var target = "#install-" + plat + "-" + lang
    location.hash = target;
}

$(document).ready(function(){
    $("#bookAdModal").on("show.bs.modal", function(event){
        $(this).find(".modal-body").load("https://tkdocs.com/bookad.html");
    });
});





setDefaultLang()

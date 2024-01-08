$(document).on('show.bs.collapse hide.bs.collapse', '.collapse', function(e) {
    e.stopPropagation();
    console.log('event triggered');
});


function navbarMotion() {
    var element = $("#listaNav");
    var toogle = $("#menuToogle");
  
      element.toggleClass("hideNav");
      element.toggleClass("showNav");
      toogle.toggleClass("menuShow");
      toogle.toggleClass("menuHide");
  
  }
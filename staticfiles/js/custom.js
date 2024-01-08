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

// When the user scrolls down 20px from the top of the document, slide down the navbar
window.onscroll = function() {smoothNav()};

function smoothNav(){
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById('navSmooth').style.backgroundColor = 'rgba(0,0,0,0.1)';
        document.getElementById('navSmooth').style.transition = '0.5s';     
    }else{
        document.getElementById('navSmooth').style.backgroundColor = 'rgba(0,0,0,1)';;
        document.getElementById('navSmooth').style.transition = '0.5s';
    } 
}
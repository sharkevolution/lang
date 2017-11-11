
// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
var navbar = document.getElementById("navbar");
// var sticky = navbar.offsetTop;
var sticky = 100;

window.onload = function() {
  window.onscroll = pagesticky;
  window.onresize = resize_menu;
  resize_menu();
}

function openNav() {
  document.getElementById("navbar").style.width = "250px";
}

function closeNav() {
  document.getElementById("navbar").style.width = "0";
}

function pagesticky(){
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky");
  } else {
    navbar.classList.remove("sticky");
  }
}

function resize_menu() {
  var navbar = document.getElementById("navbar");
  var scrollWidth = window.innerWidth;

  if (scrollWidth > 767){

    var el = document.getElementById("divmenu");
    if (typeof(el) != 'undefined' && el != null){
      el.remove();
      var el = document.getElementById("navclose");
      el.parentNode.removeChild(el);
      var el = document.getElementById("navbar");
      el.style.width = null;
    }
    pagesticky();

  } else {
    var element = document.getElementById('divmenu');

    if (typeof(element) != 'undefined' && element != null){
      // alert("Element does not exist");
    } else {

      var new_href = document.createElement('a');
      new_href.setAttribute("class", "closebtn");
      new_href.setAttribute("id", "navclose");
      new_href.setAttribute("href", "javascript:void(0)");
      new_href.setAttribute("onclick", "closeNav()");
      new_href.innerHTML = "&times;";
      navbar.insertBefore(new_href, navbar.children[0]);

      var new_btn = document.createElement('span');
      new_btn.setAttribute("style", "font-size:25px;cursor:pointer");
      new_btn.setAttribute("onclick", "openNav()");
      new_btn.setAttribute("id", "menu_click");
      new_btn.innerHTML = "&#9776;";

      var new_div = document.createElement('div');
      new_div.setAttribute("id", "divmenu");

      new_div.insertBefore(new_btn, null);
      header.insertBefore(new_div, header.children[0]);
    }
  }
}

$(document).scroll(function() { 
   if($(window).scrollTop() === 0) {
        $("header").css("height", "5em");
        $("main").css("padding-top", "5em");
        $(".logo-text").css("letter-spacing", "10px");
        $("#logo-img").css("transform", "scaleX(1)");
        $("nav a").css("padding", "10px");
       $("#join").css("padding", "10px 30px");
   }
   else {
        $("nav a").css("padding", "0px 10px");
        $("header").css("height", "3em");
        $("main").css("padding-top", "3em");
        $(".logo-text").css("letter-spacing", "3px");
        $("#logo-img").css("transform", "scaleX(-1)")
        $("#join").css("padding", "0px 30px");
   }
});

const btn = document.querySelector('#mode-toggle');
var mode = false;

btn.addEventListener('click', function() {
  document.body.classList.toggle('dark-theme')
  mode = !mode;
  if (mode) {
    document.querySelector('#mode-toggle').innerText = 'Light Mode';
  } else {
    document.querySelector('#mode-toggle').innerText = 'Dark Mode';
  }
})

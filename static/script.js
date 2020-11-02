var owl = $('.owl-carousel');

$(document).ready(function(){
    owl.owlCarousel({
        loop: true,
        margin: 15,
        stagePadding: 50,
        nav: true,
        lazyLoad: true,
        dots: false,
        animateOut: 'slideOutDown',
        animateIn: 'flipInX',
        responsive:{
            0:{
                items:1,
                stagePadding: 0,
            },
            1000:{
                items:3,
            }
        },
    })
});

var scrolledTop = 10;

$(document).scroll(function() { 
   if($(window).scrollTop() === 0) {
        $("header").css("height", "5em");
        $(".logo-text").css("letter-spacing", scrolledTop + "px");
        $(".logo-img").css("transform", "scaleX(1)");
        if (scrolledTop < 70) {
            scrolledTop += 3;
        } else {
            scrolledTop = 10
        }
   }
   else {
        $("header").css("height", "3em");
        $(".logo-text").css("letter-spacing", "3px");
        $(".logo-img").css("transform", "scaleX(-1)")
   }
});

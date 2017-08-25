// $(document).ready(function(){
//   $(window).bind('scroll', function() {
//   var navHeight = $(window).height() -70;
//     if ($(window).scrollTop() > navHeight) {
//       $('nav').addClass('fixed');
//     }
//     else {
//       $('nav').removeClass('fixed');
//     }
//  });
// });

//$(document).ready(function() {
//    //change the integers below to match the height of your upper dive, which I called
//    //banner.  Just add a 1 to the last number.  console.log($(window).scrollTop())
//    //to figure out what the scroll position is when exactly you want to fix the nav
//    //bar or div or whatever.  I stuck in the console.log for you.  Just remove when
//    //you know the position.
//    $(window).scroll(function () {
//        var topnav = $(".topnav");
//        if ($(window).scrollTop() >= 45) {
//            topnav.addClass("fixed");
//        }
//
//        else {
//            topnav.removeClass("fixed");
//        }
//    });
//});

$(document).ready(function() {
    // cache the element
    var $navBar = $('.topnav');

    // find original navigation bar position
    var navPos = $navBar.offset().top;

    // on scroll
    $(window).scroll(function() {

        // get scroll position from top of the page
        var scrollPos = $(this).scrollTop();

        // check if scroll position is >= the nav position
        if (scrollPos >= navPos) {
            $navBar.addClass('fixed');
        } else {
            $navBar.removeClass('fixed');
        }

    });
});
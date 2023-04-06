        $(document).ready(function () {
            $(window).scroll(function () {
                //Method 1: Using addClass and removeClass
                //if ($(document).scrollTop() > 50) {
                //    $('.navbar-default').addClass('navbar-shrink');
                //} else {
                //    $('.navbar-default').removeClass('navbar-shrink');
                //}
                //Method 2: Using toggleClass
                $(".navbar-default").toggleClass("navbar-shrink", $(this).scrollTop() > 50)
            });
        });
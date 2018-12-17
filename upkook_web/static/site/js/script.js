(function ($) {
    $(document).ready(function () {
        $(window).scroll(function () {
            if ($(this).scrollTop() > 50) {
                $('#back_to_top').fadeIn();
            } else {
                $('#back_to_top').fadeOut();
            }
        });
        // scroll body to 0px on click
        $("#back_to_top").on('click', function () {
            $("body,html").animate({scrollTop: 0}, 800);
            return false;
        });

    });
})(jQuery);
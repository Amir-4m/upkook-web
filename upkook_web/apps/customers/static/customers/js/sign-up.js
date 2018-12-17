(function ($) {
    $(document).ready(function () {
        $(".sign-up .btn-radio").on("click", function () {
            $(this).find("input[type=radio]").prop("checked", true);
            var intro_id = $(this).find("input[type=radio]").attr('id') + "_intro";
            $(".sign-up-intro .intro").hide();
            $("#" + intro_id).show();
        });

        $("#sign-up").submit(function (event) {
            event.preventDefault();
            var url = $(this).attr('action');
            var method = $(this).attr('method');
            var data = $(this).serialize();

            $.ajax({url: url, type: method, data: data}).done(function (response) {
                console.log(response);
            });
        });

        $("#customer_entrepreneur").trigger('click');
    });
})(jQuery);
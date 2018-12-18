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
            var data = {
                email: $(this).find("input[name=email]").val(),
                password: $(this).find("input[name=password]").val(),
                customer_type: $(this).find("input[name=customer_type]").val(),
            };

            var code = $(this).find("input[name=coupon_code]").val();
            if (code !== "") {
                data['coupon_code'] = {campaign: $(this).find("input[name=campaign]").val(), code: code}
            }

            $.ajax({
                url: url, type: method, data: JSON.stringify(data),
                cache: false, contentType: "application/json", dataType: "json"
            }).complete(function (response) {
                console.log(response.responseText);
            });
        });

        $("#customer_entrepreneur").trigger('click');
    });
})(jQuery);
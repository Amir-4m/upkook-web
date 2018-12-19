(function ($) {
    function sign_up(form) {
        var url = $(form).attr('action');
        var method = $(form).attr('method');
        var data = {
            email: $(form).find("input[name=email]").val(),
            password: $(form).find("input[name=password]").val(),
            customer_type: $(form).find("input[name=customer_type]").val()
        };

        var code = $(form).find("input[name=coupon_code]").val();
        if (code !== "") {
            data['coupon_code'] = {campaign: $(form).find("input[name=campaign]").val(), code: code}
        }

        var alert = $(form).find("#sign-up-alert");
        alert.html("");
        alert.attr("class", "alert");
        $(form).find(".has-error").removeClass("has-error");
        $(form).find(".input-alert").html("");

        $.ajax({
            url: url, type: method, data: JSON.stringify(data),
            cache: false, contentType: "application/json", dataType: "json",
            statusCode: {
                201: function () {
                    alert.html("پیش ثبت نام شما با موفقیت انجام شد.");
                    alert.addClass("alert-success");
                },
                400: function (response) {
                    alert.html("پیش ثبت نام شما با خطا مواجه شد.");
                    alert.addClass("alert-warning");
                    if (response.status === 400) {
                        $.each(response.responseJSON, function (key, value) {
                            var input_alert = $(form).find("#" + key + "_alert");
                            input_alert.parent(".form-group").addClass("has-error");
                            input_alert.html(value);
                        })

                    }
                    // else {
                    //     // TODO
                    // }
                }
            }

        }).complete(function () {
            $("body,html").animate({scrollTop: 0}, 800);
            $(form).find("[type=submit]").removeAttr("disabled");
        }).error(function (response) {
            if (response.status !== 201) {
                alert.html("پیش ثبت نام شما با خطا مواجه شد.");
                alert.addClass("alert-warning");
            }
        });
    }

    $(document).ready(function () {
        $(".sign-up .btn-radio").on("click", function () {
            $(this).find("input[type=radio]").prop("checked", true);
            var intro_id = $(this).find("input[type=radio]").attr('id') + "_intro";
            $(".sign-up-intro .intro").hide();
            $("#" + intro_id).show();
        });

        $("#sign-up").submit(function (event) {
            event.preventDefault();
            $(this).find("[type=submit]").attr("disabled", "disabled");
            sign_up(this);
        });

        $("#customer_entrepreneur").trigger('click');
    });
})(jQuery);
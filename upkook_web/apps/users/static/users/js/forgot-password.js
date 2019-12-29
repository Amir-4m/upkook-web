(function ($) {
  const ForgotPasswordForm = function (form) {
    this.form = form;
  };

  ForgotPasswordForm.handleSuccess = function () {
    $("#fg-email").css("animation", '0.7s ease 0s normal forwards 1 fadeOut');
    setTimeout(function () {
      $("#fg-email").css('display', "none");
    }, 1000);
    $("#email-submit").css("animation", '0.7s ease 0s normal forwards 1 fadeOut');
    setTimeout(function () {
      $("#email-submit").css('display', "none");
    }, 1000);
    setTimeout(function () {
      $("#sentMessage").css('display', "block");
    }, 880);
    $('#sentMessage').css("animation", '0.7s ease 0s normal forwards 1 fadein');
    $('#homePage').css("animation", '2s ease 0s normal forwards 1 moveUp');
  };

  ForgotPasswordForm.handleError = function (jqXHR) {
    if (jqXHR.status === 400) {
      const message = django.gettext('No active account found with the given Email');
      snackbar.error(message, 5000);
      $("#signUpButton").css('display', "block");
      $('#signUpButton').css("animation", '0.7s ease 0s normal forwards 1 fadein');
    } else {
      handleAPIError(jqXHR);
    }
  };

  Object.defineProperty(ForgotPasswordForm.prototype, 'email', {
    get: function () {
      return $(this.form).find("input[name=email]").val().trim();

    }
  });

  Object.defineProperty(ForgotPasswordForm.prototype, 'action', {
    get: function () {
      return $(this.form).attr('data-action');
    }
  });

  Object.defineProperty(ForgotPasswordForm.prototype, 'method', {
    get: function () {
      return $(this.form).attr('method');
    }
  });

  ForgotPasswordForm.prototype.isValid = function () {
    return Boolean(this.email);
  };

  ForgotPasswordForm.prototype.handleComplete = function () {
    $(this.form).find("button").removeAttr("disabled");
  };

  ForgotPasswordForm.prototype.submit = function () {
    grecaptcha.execute();
  };

  ForgotPasswordForm.prototype.ajax = function (recaptchaToken) {
    const data = {
      recaptcha_token: recaptchaToken,
      email: this.email,
    };

    $.ajax({
      url: this.action, type: this.method, data: JSON.stringify(data),
      cache: false, contentType: "application/json", dataType: "json",
      success: ForgotPasswordForm.handleSuccess, error: ForgotPasswordForm.handleError,
      complete: this.handleComplete.bind(this),
    });
  };

  $(document).ready(function () {
    $("#email").val(getURLParameter(window.location.search, 'email'));
    $("#forgot-password").submit(function (event) {
      event.preventDefault();
      const form = new ForgotPasswordForm(this);
      window.forgotPasswordForm = form;

      if (form.isValid()) {
        snackbar.cleanup();
        $(this).find("button").attr("disabled", "disabled");
        form.submit();
      }
    });
  });
})(jQuery);

function recaptchaCallback(recaptchaToken) {
  window.forgotPasswordForm.ajax(recaptchaToken);
}




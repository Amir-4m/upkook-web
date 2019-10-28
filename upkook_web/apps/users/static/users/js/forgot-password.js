(function ($) {
  const ForgotPasswordForm = function (form) {
    this.form = form;
  };

  ForgotPasswordForm.handleSuccess = function () {
    document.getElementById("fg-email").style.animation = '0.7s ease 0s normal forwards 1 fadeOut';
    setTimeout(function () {
      document.getElementById("fg-email").style.display = "none";
    }, 1000);
    document.getElementById("email-submit").style.animation = '0.7s ease 0s normal forwards 1 fadeOut';
    setTimeout(function () {
      document.getElementById("email-submit").style.display = "none";
    }, 1000);
    setTimeout(function () {
      document.getElementById("sentMessage").style.display = "block";
    }, 880);
    document.getElementById('sentMessage').style.animation = '0.7s ease 0s normal forwards 1 fadein';
    document.getElementById('homePage').style.animation = '2s ease 0s normal forwards 1 moveUp';
  };

  ForgotPasswordForm.handleError = function (jqXHR) {
    if (jqXHR.status === 400) {
      const message = django.gettext('No active account found with the given Email');
      snackbar.error(message, 5000);
      document.getElementById("signUpButton").style.display = 'block';
      document.getElementById('signUpButton').style.animation = '0.7s ease 0s normal forwards 1 fadein';
    } else {
      handleAPIError(jqXHR);
      const message = django.gettext('Connection has been interrupted! try again later please.');
      snackbar.error(message, 10000);
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
    const data = { email: this.email };

    $.ajax({
      url: this.action, type: this.method, data: JSON.stringify(data),
      cache: false, contentType: "application/json", dataType: "json",
      success: ForgotPasswordForm.handleSuccess, error: ForgotPasswordForm.handleError,
      complete: this.handleComplete.bind(this),
    });
  };

  $(document).ready(function () {
    $("#forgot-password").submit(function (event) {
      event.preventDefault();
      const form = new ForgotPasswordForm(this);
      if (form.isValid()) {
        snackbar.cleanup();
        $(this).find("button").attr("disabled", "disabled");
        form.submit();
      }
    });
  });
})(jQuery);





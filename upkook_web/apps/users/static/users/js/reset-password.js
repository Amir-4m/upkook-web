(function ($) {
  const TokenVerification = function (token) {
    this.token = token;
  };

  TokenVerification.handleSuccess = function () {
    $("#resetForm").css("display", "block");
  };

  TokenVerification.handleError = function (jqXHR) {
    $("#notFound").css("display", "block");
    if (jqXHR.status === 404) {
      const message = gettext('Link has been expired !');
      snackbar.error(message, 5000);

    } else {
      handleAPIError(jqXHR);
    }
  };
  Object.defineProperty(TokenVerification.prototype, 'action', {
    get: function () {
      return $(this.form).attr('data-action');
    }
  });
  TokenVerification.prototype.isValid = function () {
    return Boolean(this.token) && Boolean(this.password);
  };

  TokenVerification.prototype.submit = function () {
    const data = {token: this.token};
    $.ajax({
      url: apiURL + 'users/password/reset/verification/', type: 'post', data: JSON.stringify(data),
      cache: false, contentType: "application/json", dataType: "json",
      success: TokenVerification.handleSuccess, error: TokenVerification.handleError,
    });
  };

  function getToken() {
    const url = window.location.href;
    return url.match(/^(http[s]?:\/\/)([^\/\s]+\/)users\/password\/reset\/([^\/\s]+)\/$/);
  }

  const ResetPasswordForm = function (form, token) {
    this.form = form;
    this.token = token;
  };

  ResetPasswordForm.handleSuccess = function () {
    window.location.replace(signInURL);
  };

  ResetPasswordForm.handleError = function (jqXHR) {
    if (jqXHR.status === 400) {
      const message = gettext('Link has been expired !');
      snackbar.error(message, 5000);
    } else {
      handleAPIError(jqXHR);
    }
  };

  Object.defineProperty(ResetPasswordForm.prototype, 'password', {
    get: function () {
      return $(this.form).find("input[name=password]").val().trim();
    }
  });


  Object.defineProperty(ResetPasswordForm.prototype, 'action', {
    get: function () {
      return $(this.form).attr('data-action');
    }
  });

  ResetPasswordForm.prototype.isValid = function () {
    return Boolean(this.token) && Boolean(this.password);
  };

  ResetPasswordForm.prototype.handleComplete = function () {
    $(this.form).find("button").removeAttr("disabled");
  };

  ResetPasswordForm.prototype.submit = function () {
    const data = {
      new_password: this.password,
      token: this.token
    };

    $.ajax({
      url: this.action, type: 'put', data: JSON.stringify(data),
      cache: false, contentType: "application/json", dataType: "json",
      success: ResetPasswordForm.handleSuccess, error: ResetPasswordForm.handleError,
      complete: this.handleComplete.bind(this),
    });
  };

  window.onload = function () {
    const tokenVerification = new TokenVerification(getToken());
    tokenVerification.submit();
  };


  $(document).ready(function () {
    $("#reset-password").submit(function (event) {
      event.preventDefault();
      const form = new ResetPasswordForm(this, getToken());
      if (form.isValid()) {
        snackbar.cleanup();
        $(this).find("button").attr("disabled", "disabled");
        form.submit();
      }
    });
  });
})(jQuery);
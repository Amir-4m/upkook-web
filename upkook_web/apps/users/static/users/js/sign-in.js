(function ($) {
  const SignInForm = function (form) {
    this.form = form;
  };

  SignInForm.handleSuccess = function (data) {
    token.update(data);
    const path = getURLParameter(window.location.search, 'ret');
    window.location.assign(path != null ? dashboardURL + path : dashboardURL);
  };

  SignInForm.handleError = function (jqXHR) {
    if (jqXHR.status === 400 || jqXHR.status === 401) {
      const message = gettext('No active account found with the given credentials');
      snackbar.error(message, 5000);
    } else {
      handleAPIError(jqXHR);
    }
  };

  Object.defineProperty(SignInForm.prototype, 'email', {
    get: function () {
      return $(this.form).find("input[name=email]").val().trim();

    }
  });

  Object.defineProperty(SignInForm.prototype, 'password', {
    get: function () {
      return $(this.form).find("input[name=password]").val();
    }
  });

  Object.defineProperty(SignInForm.prototype, 'action', {
    get: function () {
      return $(this.form).attr('data-action');
    }
  });

  Object.defineProperty(SignInForm.prototype, 'method', {
    get: function () {
      return $(this.form).attr('method');
    }
  });

  SignInForm.prototype.isValid = function () {
    return Boolean(this.email) && Boolean(this.password);
  };

  SignInForm.prototype.handleComplete = function () {
    $(this.form).find("button").removeAttr("disabled");
  };

  SignInForm.prototype.submit = function () {
    const data = {
      email: this.email,
      password: this.password,
      business: null,
    };

    $.ajax({
      url: this.action, type: this.method, data: JSON.stringify(data),
      cache: false, contentType: "application/json", dataType: "json",
      success: SignInForm.handleSuccess, error: SignInForm.handleError,
      complete: this.handleComplete.bind(this),
    });
  };

  $(document).ready(function () {
    $("#sign-in").submit(function (event) {
      event.preventDefault();
      const form = new SignInForm(this);
      if (form.isValid()) {
        snackbar.cleanup();
        $(this).find("button").attr("disabled", "disabled");
        form.submit();
      }
    });
  });
})(jQuery);
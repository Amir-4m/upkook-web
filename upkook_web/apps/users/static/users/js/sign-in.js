(function ($) {
  const SignInForm = function (form) {
    this.form = form;
    this.retries = 0;
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
      this.retries += 1;
      this.showForgotDialog()

    } else {
      handleAPIError(jqXHR);
    }
  };
  Object.defineProperty(SignInForm.prototype, 'email', {
    get: function () {
      return $(this.form).find("input[name=email]").val().trim().toLowerCase();

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

  SignInForm.prototype.showForgotDialog = function () {
    const dialog = document.querySelector('dialog');
    if (!dialog.showModal) {
      dialogPolyfill.registerDialog(dialog);
    }
    if (this.retries >= 3) {
      dialog.showModal();
    }
    dialog.querySelector('.close').addEventListener('click', function () {
      dialog.close();
    });
  };

  SignInForm.prototype.isValid = function () {
    return Boolean(this.email) && Boolean(this.password);
  };

  SignInForm.prototype.handleComplete = function () {
    $(this.form).find("button").removeAttr("disabled");
  };

  SignInForm.prototype.submit = function () {
    grecaptcha.execute();
  };
  SignInForm.prototype.ajax = function (recaptchaToken) {
    const data = {
      recaptcha_token: recaptchaToken,
      email: this.email,
      password: this.password,
      business: null,
    };

    $.ajax({
      url: this.action, type: this.method, data: JSON.stringify(data),
      cache: false, contentType: "application/json", dataType: "json",
      success: SignInForm.handleSuccess, error: SignInForm.handleError.bind(this),
      complete: this.handleComplete.bind(this),
    });
  };

  $(document).ready(function () {
    const signIn = $("#sign-in");
    const form = new SignInForm(signIn);
    window.signInForm = form;

    signIn.submit(function (event) {
      event.preventDefault();
      if (form.isValid()) {
        snackbar.cleanup();
        $(this).find("button").attr("disabled", "disabled");
        form.submit();
      }
    });
  });
})(jQuery);

function recaptchaCallback(recaptchaToken) {
  window.signInForm.ajax(recaptchaToken);
}

function recaptchaErrorCallback() {
  const message = gettext('Limited or No Connectivity. Please check your internet connection.');
  snackbar.error(message, 5000);
  window.signInForm.handleComplete();
}

document.getElementById('forget-password-button').addEventListener('click', forgetPassword);
document.getElementById('dialog-forget-button').addEventListener('click', forgetPassword);

function forgetPassword(event) {
  event.preventDefault();
  const forgotButton = document.getElementById('forget-password-button');
  const email = document.getElementById('email').value;
  window.location.assign(forgotButton.getAttribute('href') + '?email=' + email);
}
(function ($) {
  class SignInForm {
    constructor(form) {
      this.form = form;
    }

    get email() {
      return $(this.form).find("input[name=email]").val().trim();
    }

    get password() {
      return $(this.form).find("input[name=password]").val();
    }

    get action() {
      return $(this.form).attr('data-action');
    }

    get method() {
      return $(this.form).attr('method');
    }

    is_valid() {
      return Boolean(this.email) && Boolean(this.password);
    }

    static handleSuccess(data) {
      cookie.setItem(
        Auth.accessKey,
        data.access,
        Auth.age,
        Auth.path,
        Auth.domain,
        Auth.secure,
      );
      cookie.setItem(
        Auth.refreshKey,
        data.refresh,
        Auth.age,
        Auth.path,
        Auth.domain,
        Auth.secure,
      );

      const path = getURLParameter(window.location.search, 'ret');
      window.location.assign(`${dashboardURL}${path}`);
    }

    static handleError(jqXHR) {
      if (jqXHR.status === 400) {
        const message = gettext('No active account found with the given credentials');
        snackbar.error(message, 5000);
      } else {
        handleAPIError(jqXHR);
      }
    }

    handleComplete() {
      $(this.form).find("button").removeAttr("disabled");
    }

    submit() {
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
    }
  }

  $(document).ready(function () {
    $("#sign-in").submit(function (event) {
      event.preventDefault();
      const form = new SignInForm(this);
      if (form.is_valid()) {
        snackbar.cleanup();
        $(this).find("button").attr("disabled", "disabled");
        form.submit();
      }
    });
  });
})(jQuery);
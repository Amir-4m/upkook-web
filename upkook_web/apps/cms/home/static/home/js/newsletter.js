(function ($) {
  const NewsletterForm = function (form) {
    this.form = form;
  };

  NewsletterForm.handleError = function (jqXHR) {
    if (jqXHR.status === 400) {
      const message = gettext('Email is invalid');
      snackbar.error(message, 5000);
    } else {
      handleAPIError(jqXHR);
    }
  };

  Object.defineProperty(NewsletterForm.prototype, 'email', {
    get: function () {
      return $(this.form).find("input[name=email]").val().trim();
    }
  });

  Object.defineProperty(NewsletterForm.prototype, 'action', {
    get: function () {
      return $(this.form).attr('data-action');
    }
  });

  Object.defineProperty(NewsletterForm.prototype, 'method', {
    get: function () {
      return $(this.form).attr('method');
    }
  });

  NewsletterForm.prototype.isValid = function () {
    return Boolean(this.email);
  };

  NewsletterForm.handleSuccess = function () {
    const message = gettext('Successfully subscribed in newsletter');
    snackbar.success(message, 5000);
  };

  NewsletterForm.prototype.handleComplete = function () {
    $(this.form).find("button").removeAttr("disabled");
  };

  NewsletterForm.prototype.submit = function () {
    grecaptcha.execute();
  };

  NewsletterForm.prototype.ajax = function (recaptchaToken) {
    const data = {
      recaptcha_token: recaptchaToken,
      email: this.email,
    };

    $.ajax({
      url: this.action, type: this.method, data: JSON.stringify(data),
      cache: false, contentType: "application/json", dataType: "json",
      success: NewsletterForm.handleSuccess, error: NewsletterForm.handleError.bind(this),
      complete: this.handleComplete.bind(this),
    });
  };

  $(document).ready(function () {
    const newsletter = $("#newsletter");
    const form = new NewsletterForm(newsletter);
    window.newsletterForm = form;

    newsletter.submit(function (event) {
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
  window.newsletterForm.ajax(recaptchaToken);
}

function recaptchaErrorCallback() {
  const message = gettext('Limited or No Connectivity. Please check your internet connection.');
  snackbar.error(message, 5000);
  window.newsletterForm.handleComplete();
}

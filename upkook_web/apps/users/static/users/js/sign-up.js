(function ($) {
  const IndustryService = function () {
  };

  IndustryService.options = function (industries) {
    return industries.map(function (industry) {
      return '<li class="mdl-menu__item" data-val="' + industry.id + '">' + industry.name + '</li>';
    });
  };

  IndustryService.isLoaded = function () {
    return $('ul[for="industry"]').html().trim() !== "";
  };

  IndustryService.load = function () {
    $.ajax({
      tryCount: 0, retryLimit: 3, retryInterval: 300,
      url: apiURL + 'industries/', type: 'GET',
      cache: true, contentType: "application/json", dataType: "json",
      success: function (data) {
        $('ul[for=industry]').html(IndustryService.options(data));
        $('ul[for=industry] > li').click(function () {
          document.getElementById('sign-up-step2').scrollIntoView();
        });
        $('#fg-industry').addClass('getmdl-select');
        getmdlSelect.init("#fg-industry.getmdl-select");
      },
      error: function (jqXHR) {
        this.tryCount++;
        if (this.tryCount <= this.retryLimit) {
          setTimeout(
            function () {
              $.ajax(this);
            },
            this.retryInterval * this.tryCount
          );
        } else {
          handleAPIError(jqXHR);
        }
      },
    })
  };

  const StepOne = function (form) {
    this.fields = ['email', 'password', 'first_name', 'last_name'];
    this.form = form;
  };

  Object.defineProperty(StepOne.prototype, 'data', {
    get: function () {
      return {
        email: $(this.form).find("input[name=email]").val().trim(),
        password: $(this.form).find("input[name=password]").val(),
        first_name: $(this.form).find("input[name=first_name]").val().trim(),
        last_name: $(this.form).find("input[name=last_name]").val().trim(),
      };
    }
  });

  const StepTwo = function (form) {
    this.fields = ['domain', 'name', 'industry', 'size'];
    this.form = form;
  };

  Object.defineProperty(StepTwo.prototype, 'data', {
    get: function () {
      return {
        domain: $(this.form).find("input[name=domain]").val().trim(),
        name: $(this.form).find("input[name=name]").val().trim(),
        industry: $(this.form).find("input[name=industry]").val(),
        size: $(this.form).find("input[name=size]").val(),
      };
    }
  });

  const SignupForm = function (step) {
    this.step = step || 1;
  };

  Object.defineProperty(SignupForm.prototype, 'form', {
    get: function () {
      return $('#sign-up-step' + this.step);
    }
  });

  Object.defineProperty(SignupForm.prototype, 'stepForm', {
    get: function () {
      if (this.step === 2) {
        return new StepTwo(this.form);
      }
      return new StepOne(this.form);
    }
  });

  Object.defineProperty(SignupForm.prototype, 'action', {
    get: function () {
      return $(this.form).attr('data-action');
    }
  });

  Object.defineProperty(SignupForm.prototype, 'method', {
    get: function () {
      return $(this.form).attr('method');
    }
  });

  SignupForm.prototype.init = function () {
    IndustryService.load();
    const forms = $('form');
    forms.submit(this.submit.bind(this));
    forms.find('.mdl-textfield__error').each(function () {
      const element = $(this);
      const handleText = function () {
        element.text(element.attr('data-text'));
      };

      $(this).siblings('input').keyup(handleText);
      $(this).siblings('select').change(handleText);
    });
  };

  SignupForm.prototype.changeStep = function (step) {
    $('#sign-up-step' + this.step + '-wrapper').hide();
    this.step = step;
    if (step === 2 && !IndustryService.isLoaded()) {
      IndustryService.load();
    }
    $('#sign-up-step' + step + '-wrapper').show();

  };

  SignupForm.prototype.isValid = function () {
    const currentStep = this.stepForm;
    for (let i = 0; i < currentStep.fields; i += 1) {
      const name = currentStep.fields[i];
      if (this.form.find('#fg-' + name).hasClass('is-invalid')) {
        return false;
      }
    }
    return true;
  };

  SignupForm.prototype.handleFieldError = function (name, errors) {
    if (errors !== undefined) {
      const group = this.form.find('#fg-' + name);
      group.find('.mdl-textfield__error').html(errors.join('<br />'));
      group.addClass('is-invalid');
    }
  };

  SignupForm.prototype.handleError = function (jqXHR) {
    if (jqXHR.status === 400) {
      const data = jqXHR.responseJSON;
      const currentStep = this.stepForm;
      for (let i = 0; i < currentStep.fields.length; i += 1) {
        const name = currentStep.fields[i];
        this.handleFieldError(name, data[name]);
      }

      let message = gettext('Please fix form errors.');
      if (data.non_field_errors !== undefined) {
        message = data.non_field_errors.join('<br />');
      }
      snackbar.error(message, 5000);

    } else {
      handleAPIError(jqXHR);
    }
  };

  SignupForm.prototype.track = function (jqXHR) {
    dataLayer.push({
      event: 'signUp',
      signUpAction: this.step === 1 ? 'create-user' : 'create-business',
      signUpStatus: jqXHR.status,
    });
  };

  SignupForm.prototype.fail = function (jqXHR) {
    this.form.find("button").removeAttr("disabled");
    this.track(jqXHR);
  };

  SignupForm.prototype.done = function (data, textStatus, jqXHR) {
    this.form.find("button").removeAttr("disabled");
    token.update(data);
    this.track(jqXHR);

    if (this.step === 1) {
      this.changeStep(2);
    } else {
      const path = getURLParameter(window.location.search, 'ret');
      window.location.assign(path != null ? dashboardURL + path : dashboardURL);
    }
  };

  SignupForm.prototype.submit = function (event) {
    event.preventDefault();
    if (this.isValid()) {
      snackbar.cleanup();
      this.form.find("button").attr("disabled", "disabled");

      let headers = {};
      if (this.step === 2) {
        headers = {Authorization: 'Bearer ' + token.access};
      }

      $.ajax({
        url: this.action,
        type: this.method,
        headers: headers,
        data: JSON.stringify(this.stepForm.data),
        cache: false,
        contentType: "application/json",
        dataType: "json",
        error: this.handleError.bind(this)
      }).fail(
        this.fail.bind(this)
      ).done(
        this.done.bind(this)
      );
    }
  };

  $(document).ready(function () {
    const form = new SignupForm();
    form.init();
  });
})
(jQuery);
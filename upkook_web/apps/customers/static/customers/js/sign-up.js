(function ($) {
  class IndustryService {
    static options(industries) {
      return industries.map(function (industry) {
        return `<li class="mdl-menu__item" data-val="${industry.id}">${industry.name}</li>`;
      });
    }

    static load() {
      $.ajax({
        tryCount: 0, retryLimit: 3, retryInterval: 300,
        url: `${apiURL}industries/`, type: 'GET',
        cache: true, contentType: "application/json", dataType: "json",
        success: function (data) {
          $('ul[for=industry]').html(IndustryService.options(data));
        },
        error: function (jqXHR) {
          this.tryCount++;
          if (this.tryCount <= this.retryLimit) {
            setTimeout(
              () => {
                $.ajax(this);
              },
              this.retryInterval * this.tryCount,
            );
          } else {
            handleAPIError(jqXHR);
          }
        },
      })
    }
  }

  class StepOne {
    constructor(form) {
      this.fields = ['email', 'password', 'first_name', 'last_name'];
      this.form = form;
    }

    get data() {
      return {
        email: $(this.form).find("input[name=email]").val().trim(),
        password: $(this.form).find("input[name=password]").val(),
        first_name: $(this.form).find("input[name=first_name]").val().trim(),
        last_name: $(this.form).find("input[name=last_name]").val().trim(),
      };
    }
  }

  class StepTwo {
    constructor(form) {
      this.fields = ['domain', 'name', 'industry', 'size'];
      this.form = form;
    }

    get data() {
      return {
        domain: $(this.form).find("input[name=domain]").val().trim(),
        name: $(this.form).find("input[name=name]").val().trim(),
        industry: $(this.form).find("input[name=industry]").val(),
        size: $(this.form).find("input[name=size]").val(),
      };
    }
  }

  class SignupForm {
    constructor(step = 1) {
      this.step = step;
    }

    get form() {
      return $(`#sign-up-step${this.step}`);
    }

    get stepForm() {
      if (this.step === 2) {
        return new StepTwo(this.form);
      }
      return new StepOne(this.form);
    }

    get action() {
      return $(this.form).attr('data-action');
    }

    get method() {
      return $(this.form).attr('method');
    }

    init() {
      IndustryService.load();
      const forms = $('form');
      forms.submit(this.submit.bind(this));
      forms.find('.mdl-textfield__error').each(function () {
        const element = $(this);
        const handleText = () => {
          element.text(element.attr('data-text'));
        };

        $(this).siblings('input').keyup(handleText);
        $(this).siblings('select').change(handleText);
      });
    }

    changeStep(step) {
      $(`#sign-up-step${this.step}-wrapper`).hide();
      this.step = step;
      $(`#sign-up-step${step}-wrapper`).show();

    }

    isValid() {
      const currentStep = this.stepForm;
      for (let i = 0; i < currentStep.fields; i += 1) {
        const name = currentStep.fields[i];
        if (this.form.find(`#fg-${name}`).hasClass('is-invalid')) {
          return false;
        }
      }
      return true;
    }

    handleFieldError(name, errors) {
      if (errors !== undefined) {
        const group = this.form.find(`#fg-${name}`);
        group.find('.mdl-textfield__error').html(errors.join('<br />'));
        group.addClass('is-invalid');
      }
    }

    handleError(jqXHR) {
      if (jqXHR.status === 400) {
        const {responseJSON: data} = jqXHR;
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
    }

    fail() {
      this.form.find("button").removeAttr("disabled");
    }

    done() {
      this.form.find("button").removeAttr("disabled");
      if (this.step === 1) {
        // TODO store jwt token in cookie
        this.changeStep(2);
      } else {
        const path = getURLParameter(window.location.search, 'ret');
        window.location.assign(`${dashboardURL}${path != null ? path : ''}`);
      }
    }

    submit(event) {
      event.preventDefault();
      if (this.isValid()) {
        snackbar.cleanup();
        this.form.find("button").attr("disabled", "disabled");

        // TODO include Bearer authentication headers when requesting in step 2
        $.ajax({
          url: this.action, type: this.method, data: JSON.stringify(this.stepForm.data),
          cache: false, contentType: "application/json", dataType: "json",
          error: this.handleError.bind(this),
        }).fail(
          this.fail.bind(this),
        ).done(
          this.done.bind(this),
        );
      }
    }
  }

  $(document).ready(function () {
    const form = new SignupForm();
    form.init();
  });
})(jQuery);
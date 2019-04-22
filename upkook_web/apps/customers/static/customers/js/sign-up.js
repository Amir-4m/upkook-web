(function ($) {
  class StepOne {
    constructor(form) {
      this.form = form;
    }

    get email() {
      return $(this.form).find("input[name=email]").val().trim();
    }

    get password() {
      return $(this.form).find("input[name=password]").val();
    }

    get firstName() {
      return $(this.form).find("input[name=first_name]").val().trim();
    }

    get lastName() {
      return $(this.form).find("input[name=last_name]").val().trim();
    }

    get action() {
      return $(this.form).attr('data-action');
    }

    get method() {
      return $(this.form).attr('method');
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
        const fields = ['email', 'password', 'first_name', 'last_name'];
        for (let i = 0; i < fields.length; i += 1) {
          const name = fields[i];
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

    isValid() {
      return Boolean(this.email) && Boolean(this.password) && Boolean(this.firstName) && Boolean(this.lastName);
    }

    submit() {
      const data = {
        email: this.email,
        password: this.password,
        first_name: this.firstName,
        last_name: this.lastName,
      };

      return $.ajax({
        url: this.action, type: this.method, data: JSON.stringify(data),
        cache: false, contentType: "application/json", dataType: "json",
        error: this.handleError.bind(this),
      });
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
      return new StepOne(this.form);
    }

    init() {
      const forms = $('form');
      forms.submit(this.submit.bind(this));
      forms.find('.mdl-textfield__error').each(function () {
        const element = $(this);
        $(this).siblings('input').keyup(function (element) {
          return function () {
            element.text(element.attr('data-text'));
          }
        }(element));
      });
    }

    isValid() {
      return this.stepForm.isValid();
    }

    fail() {
      this.form.find("button").removeAttr("disabled");
    }

    done() {
      this.form.find("button").removeAttr("disabled");
      if (this.step === 1) {
        this.changeStep(2);
      }
    }

    submit(event) {
      event.preventDefault();
      if (this.isValid()) {
        snackbar.cleanup();
        this.form.find("button").attr("disabled", "disabled");

        this.stepForm.submit().fail(
          this.fail.bind(this),
        ).done(
          this.done.bind(this),
        );
      }
    }

    changeStep(step) {
      this.form.hide();
      this.step = step;
      this.form.show();
    }
  }

  $(document).ready(function () {
    const form = new SignupForm();
    form.init();
  });
})(jQuery);
(function ($) {
  window.addEventListener('load', function () {
    $('[data-required=true]').attr('required', true);
  });
})(jQuery);

const Snackbar = function () {
  this.notification = document.querySelector('.mdl-js-snackbar');
};

Snackbar.prototype.setClass = function (klass) {
  let className = this.notification.className;
  className = className.replace(/\bmdl-snackbar--(success|info|warning|error)\b/g, ``);
  this.notification.className = `${className.trim()} mdl-snackbar--${klass}`;
};

Snackbar.prototype.error = function (message, timeout = 3750) {
  this.setClass('error');
  this.notification.MaterialSnackbar.showSnackbar({message, timeout});
};

Snackbar.prototype.cleanup = function () {
  const mSnackbar = this.notification.MaterialSnackbar;
  mSnackbar.element_.classList.remove(mSnackbar.cssClasses_.ACTIVE);
  mSnackbar.element_.setAttribute('aria-hidden', 'true');
  mSnackbar.textElement_.textContent = '';
  if (!Boolean(mSnackbar.actionElement_.getAttribute('aria-hidden'))) {
    mSnackbar.setActionHidden_(true);
    mSnackbar.actionElement_.textContent = '';
    mSnackbar.actionElement_.removeEventListener('click', mSnackbar.actionHandler_);
  }
  mSnackbar.actionHandler_ = undefined;
  mSnackbar.message_ = undefined;
  mSnackbar.actionText_ = undefined;
  mSnackbar.active = false;
  mSnackbar.checkQueue_();
};

const snackbar = new Snackbar();
const Cookie = function cookie() {
};

Cookie.prototype.setItem = function (key, value, seconds, path, domain, secure) {
  path = path || '/';
  domain = domain || null;
  secure = secure || false;

  const d = new Date();
  d.setTime(d.getTime() + (seconds * 1000));
  const domainStr = domain != null ? ';domain=' + domain : '';
  const secureStr = secure ? ';secure' : '';
  document.cookie = key + '=' + value + domainStr + ';path=' + path + ';expires=' + d.toUTCString() + secureStr;
};

Cookie.prototype.getItem = function (key) {
  const match = document.cookie.match('(^|;) ?' + key + '=([^;]*)(;|$)');
  return match ? match[2] : null;
};

Cookie.prototype.removeItem = function (key, path, domain, secure) {
  this.setItem(key, '', -1, path, domain, secure);
};

const cookie = new Cookie();

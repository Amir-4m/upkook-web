function getURLParameter(url, name) {
  if (typeof url === 'string') {
    const matched = url.match(`[?&]${name}=(?<${name}>[^&#]*)`);
    return matched != null ? matched.groups[name] || null : null;
  }
  return null;
}

const Cookie = function cookie() {
};

Cookie.prototype.setItem = function (key, value, seconds, path = '/', domain = null, secure = false) {
  const d = new Date();
  d.setTime(d.getTime() + (seconds * 1000));
  const domainStr = domain != null ? `;domain=${domain}` : '';
  const secureStr = secure ? ';secure' : '';
  document.cookie = `${key}=${value}${domainStr};path=${path};expires=${d.toUTCString()}${secureStr}`;
};

Cookie.prototype.getItem = function (key) {
  const match = document.cookie.match(`(^|;) ?${key}=([^;]*)(;|$)`);
  return match ? match[2] : null;
};

Cookie.prototype.removeItem = function (key) {
  this.setItem(key, '', -1);
};

const cookie = new Cookie();
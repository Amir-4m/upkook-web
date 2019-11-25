function getURLParameter(url, name) {
  if (typeof url === 'string') {
    const matched = url.match('[?&]' + name + '=([^&#]*)');
    return matched != null ? matched[1] || null : null;
  }
  return null;
}

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

Cookie.prototype.removeItem = function (key) {
  this.setItem(key, '', -1);
};

const cookie = new Cookie();

if (typeof NodeList !== "undefined" && NodeList.prototype && !NodeList.prototype.forEach) {
  // Yes, there's really no need for `Object.defineProperty` here
  NodeList.prototype.forEach = Array.prototype.forEach;
}

// For IE Compatibility
// source: https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent/CustomEvent
(function () {
  if (typeof window.CustomEvent === "function") return false;

  function CustomEvent(event, params) {
    params = params || {bubbles: false, cancelable: false, detail: undefined};
    const evt = document.createEvent('CustomEvent');
    evt.initCustomEvent(event, params.bubbles, params.cancelable, params.detail);
    return evt;
  }

  CustomEvent.prototype = window.Event.prototype;

  window.CustomEvent = CustomEvent;
})();

// Function to make IE9+ support forEach:
if (!Array.prototype.forEach) {
  Array.prototype.forEach = function forEach(callback, thisArg) {
    if (typeof callback !== 'function') {
      throw new TypeError(callback + ' is not a function');
    }
    var array = this;
    thisArg = thisArg || this;
    for (var i = 0, l = array.length; i !== l; ++i) {
      callback.call(thisArg, array[i], i, array);
    }
  };
}

if (window.NodeList && !NodeList.prototype.forEach) {
  NodeList.prototype.forEach = Array.prototype.forEach;
}
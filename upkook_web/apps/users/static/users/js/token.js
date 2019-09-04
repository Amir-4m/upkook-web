const Token = function (data) {
  this.ak = data.ak;
  this.rk = data.rk;
  this.uk = data.uk;
  this.age = data.age;
  this.path = data.path;
  this.d = data.d;
  this.secure = data.secure;
};

Token.prototype.setCookie = function (key, value) {
  cookie.setItem(
    key,
    value,
    this.age,
    this.path,
    this.d,
    this.secure
  );
};

Object.defineProperty(Token.prototype, 'access', {
  get: function () {
    return cookie.getItem(this.ak);
  },
  set: function (value) {
    this.setCookie(this.ak, value);
  },
});

Object.defineProperty(Token.prototype, 'refresh', {
  get: function () {
    return cookie.getItem(this.rk)
  },
  set: function (value) {
    this.setCookie(this.rk, value);
  },
});

Object.defineProperty(Token.prototype, 'trackId', {
  get: function () {
    return cookie.getItem(this.uk);
  },
  set: function (value) {
    this.setCookie(this.uk, value);
  },
});

Token.prototype.update = function (data) {
  this.access = data.access;
  this.refresh = data.refresh;
  this.trackId = data[this.uk];
};
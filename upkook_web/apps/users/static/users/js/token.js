class Token {
  constructor({ak, rk, uk, age, path, d, secure}) {
    this.ak = ak;
    this.rk = rk;
    this.uk = uk;
    this.age = age;
    this.path = path;
    this.d = d;
    this.secure = secure;
  }

  setCookie(key, value) {
    cookie.setItem(
      key,
      value,
      this.age,
      this.path,
      this.d,
      this.secure,
    );
  }

  get access() {
    return cookie.getItem(this.ak);
  }

  set access(value) {
    this.setCookie(this.ak, value);
  }

  get refresh() {
    return cookie.getItem(this.rk)
  }
  
  set refresh(value) {
    this.setCookie(this.rk, value);
  }

  get trackId() {
    return cookie.getItem(this.uk);
  }

  set trackId(value) {
    this.setCookie(this.uk, value);
  }

  update = (data) => {
      this.access = data.access;
      this.refresh = data.refresh;
      this.trackId = data[this.uk];
  };
}
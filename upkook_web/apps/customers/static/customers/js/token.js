class Token {
  constructor({ak, rk, age, path, d, secure}) {
    this.ak = ak;
    this.rk = rk;
    this.age = age;
    this.path = path;
    this.d = d;
    this.secure = secure;
  }

  get access() {
    return cookie.getItem(this.ak);
  }

  set access(value) {
    cookie.setItem(
      this.ak,
      value,
      this.age,
      this.path,
      this.d,
      this.secure,
    );
  }

  get refresh() {
    return cookie.getItem(this.rk)
  }
  
  set refresh(value) {
    cookie.setItem(
      this.rk,
      value,
      this.age,
      this.path,
      this.d,
      this.secure,
    );
  }
}
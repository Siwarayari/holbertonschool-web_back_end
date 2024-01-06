export default class Airport {
  constructor(name, code) {
    this._code = code;
    this._name = name;
  }

  get [Symbol.toStringTag]() {
    return this._code;
  }
}

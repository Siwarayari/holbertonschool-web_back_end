export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building) {
      if (!this.evacuationWarningMessage) { throw TypeError('Class extending Building must override evacuationWarningMessage'); }
    }
    if (typeof (sqft) !== 'number') throw TypeError('must be a number');
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}

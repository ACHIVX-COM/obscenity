module.exports = {
  get ["en"]() {
    return new RegExp(require("./en.json"), "gi");
  },
  get ["ru"]() {
    return new RegExp(require("./ru.json"), "gi");
  },
  get ["de"]() {
    return new RegExp(require("./de.json"), "gi");
  },
  get ["fr"]() {
    return new RegExp(require("./fr.json"), "gi");
  },
  get ["es"]() {
    return new RegExp(require("./es.json"), "gi");
  },
  get ["ja"]() {
    return new RegExp(require("./ja.json"), "gi");
  },
  get ["ko"]() {
    return new RegExp(require("./ko.json"), "gi");
  },
  get ["all"]() {
    return new RegExp(require("./all.json"), "gi");
  },
};

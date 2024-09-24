const expressions = require("./regex");

/**
 * Run a global regex for given text, returning array of all matches.
 *
 * @param {string} text
 * @param {RegExp} re
 * @returns {string[]}
 */
function testText(text, re) {
  let matches = undefined;
  let match = null;

  while ((match = re.exec(text))) {
    matches = matches ?? [];
    matches.push(match[0].trim());
  }

  return matches;
}

const exprCache = new Map();

/**
 * Return a regex for the given language.
 *
 * @param {string} language
 * @returns {RegExp}
 */
function getExpression(language) {
  if (exprCache.has(language)) {
    return exprCache.get(language);
  }

  let expr = expressions[language];

  if (!expr) {
    if (language) {
      console.warn(
        "No obscenity expression defined for",
        language,
        "language, using generic expression",
      );
    }

    expr = getExpression("all");
  }

  if (language) {
    exprCache.set(language, expr);
  }

  return expr;
}

/**
 * Detects obscenity in given text.
 *
 * If language of a text is provided (second parameter) and is supported, this
 * function will more carefully check for words and phrases specific for this
 * language.
 * It will check for words and phrases that are obscene in this language but may
 * be safe in other languages.
 *
 * @param {string} text
 * @param {string?} language language code, e.g. "en"
 * @returns {string[]?} array of found obscene words
 */
module.exports.detect = function detect(text, language = null) {
  return testText(text, getExpression(language));
};

/**
 * Check if the `detect` function has special rules for given language.
 *
 * @param {string} language language code, e.g. "en"
 * @returns {bool}
 */
module.exports.supportsLanguage = function supportsLanguage(language) {
  return getExpression(language) !== getExpression("all");
};

const obscenity = require("@achivx/obscenity");

describe("obscenity.detect()", () => {
  it("should detect obscene words", () => {
    expect(obscenity.detect("fuck this shit")).toEqual(["fuck", "shit"]);
    expect(obscenity.detect("fUcK")).toEqual(["fUcK"]);
  });

  it("should handle obfuscated obscenity", () => {
    expect(obscenity.detect("$h1t p00p 1nc31 vvhore")).toHaveLength(4);
  });

  it("should not cause the Scunthorpe problem", () => {
    expect(
      obscenity.detect(
        `The Scunthorpe problem is the unintentional blocking of online content
         by a spam filter or search engine because their text contains a string
         (or substring) of letters that appear to have an obscene or otherwise
         unacceptable meaning.`,
      ),
    ).toBeFalsy();
  });

  it("should handle мент-case", () => {
    expect(obscenity.detect("this is a comment")).toBeFalsy();
    expect(obscenity.detect("this is a comment", "ru")).toBeFalsy();
    expect(obscenity.detect("это коммент, комментарий")).toBeFalsy();
    expect(obscenity.detect("это коммент, комментарий", "ru")).toBeFalsy();
    expect(obscenity.detect("ment")).toBeFalsy();
    expect(obscenity.detect("ment", "ru")).toHaveLength(1);
    expect(obscenity.detect("мент")).toHaveLength(1);
    expect(obscenity.detect("мент", "ru")).toHaveLength(1);
  });
});

describe("obscenity.supportsLanguage()", () => {
  it("should return true for supported language codes", () => {
    expect(obscenity.supportsLanguage("en")).toBe(true);
    expect(obscenity.supportsLanguage("de")).toBe(true);
    expect(obscenity.supportsLanguage("es")).toBe(true);
    expect(obscenity.supportsLanguage("fr")).toBe(true);
    expect(obscenity.supportsLanguage("ja")).toBe(true);
    expect(obscenity.supportsLanguage("ko")).toBe(true);
    expect(obscenity.supportsLanguage("ru")).toBe(true);
  });

  it("should return false for unsupported languages", () => {
    expect(obscenity.supportsLanguage("en-US")).toBe(false);
    expect(obscenity.supportsLanguage("kz")).toBe(false);
  });
});

# Obscenity

An obscene language/profanity detector.

> ⚠️ **WARNING:** This repository contains materials that some may find offensive. That's intentional.

This package uses the [List of Dirty, Naughty, Obscene, and Otherwise Bad Words](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words) along with few custom dictionaries.
It also takes some ways of profanity obfuscation (such as leetspeak) into account.
It's all done to build [the worst regular expression publicly available](./packages/obscenity/src/regex/all.json).

## How to use

The package is [available on npmjs.com](https://www.npmjs.com/package/@achivx/obscenity) and can be installed using `npm`:

```sh
npm i @achivx/obscenity
```

Then it can be used as follows:

```JavaScript
const obscenity = require("@achivx/obscenity");

obscenity.detect("Scunthorpe (/ˈskʌnθɔːrp/) is an industrial town in the North Lincolnshire district of Lincolnshire, England.")
// -> undefined

obscenity.detect('The town\'s name contains the substring "cunt".')
// -> ["cunt"]
```

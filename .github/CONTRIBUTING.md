# How to Contribute
Issues & Pull requests are welcome!

## 0. Be nice - [about](//gist.github.com/search?&q=Contributor+Code+of+Conduct)
This repo handles letting anonymous people reach compromises. Unfortunately the 
codebase doesn't extend to github comments. Don't be any form of oppressive or slandarous towards another person or group.

## 1. Documentation
Explaining an endpoint allows other people to use it correctly. If the
docs won't match the code anymore, change them too. Use markdown code
blocks for snippets, when in doubt run `mkdocs serve` to try them out.

## 2. Testing - [about](//congredi.readthedocs.io/en/latest/building/testing)

Before submitting your changes, run `setup.py test` &/|| `docker-compose build`,
just to see that everything superficially checks out. If you'd made changes
outside the scope of the tests, it might not register as failing, but it's
a good, basic step. The testing system currently uses `nose2` & `jasmine`.

## (3.) Code style - [about](//congredi.readthedocs.io/en/latest/building/style)
Insofar as the editor you use can format, and the test suite used can lint it.
Currently, that's `eslint` & `pylint` (`python setup.py lint`).
In other words, if the machines can both catch and help you, style it that way.

### Commits (from Atom/Contributing)
* Present Tense, Imperative mood `run` ***not*** `ran/runs`
* prefixes (use emojis! :sunglasses:)
    * tests :100:
        * :bug: `:bug:` Fixed bug (travis)
        * :green_heart: `:green_heart:` CI configuration
        * :white_check_mark: `:white_check_mark:` Added Tests (nose2/jasmine)
    * documentation :heart:
        * :octocat: `:octocat:` Changed .gitignore / .github / hooks
        * :memo: `:memo:` Updated docs (mkdocs)
        * :books: `:books:` Updated tutorials
        * :art: `:art:` format/structure (eslint/pylint)
    * builds :pray:
        * :droplet:/:whale:/:rocket: `:droplet:/:whale:/:rocket:` Updated Docker code
        * :snake: `:snake:` Updated python
    * methodology :pencil2:
        * :lock: `:lock:` Security
        * :fire: `:fire:` Deleted Code
        * :arrow_up: `:arrow_up:` Dependency management

# (finally) Submitting Changes

1. Create (or finish creating) an issue referencing what needs to change.
2. Start your pull request (on your honor it's your own code).
3. If the build, documentation, or testing need changes, alert us to them.

> want to change these `.github` docs?

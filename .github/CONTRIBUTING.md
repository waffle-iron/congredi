# How to Contribute
Hello! Welcome to Congredi/Delegito/Komento's repository!

> still looking through `.github` [style docs](https://github.com/atom/atom/blob/master/CONTRIBUTING.md)

# Rules for contributing
If you'd like to make a difference, we'd be happy to have you!
Doing the following helps everyone:

## Behavior (Be nice?)
This repo handles letting anonymous people reach compromises. Unfortunately the 
codebase doesn't extend to github comments.

Don't be any form of oppressive or slandarous towards another person or group.

## Documentation
Explaining an endpoint allows other people to use it correctly. If the
docs won't match the code anymore, change them too.

## Code style (automated)
Insofar as the editor you use can format, and the test suite used can lint it.

Currently, that's `eslint` & `pylint` (`python setup.py lint`).

In other words, if the machines can both catch and help you, style it that way.

## Testing

Before submitting your changes, run `setup.py test` &/|| `docker-compose build`,
just to see that everything superficially checks out. If you'd made changes
outside the scope of the tests, it might not register as failing, but it's
a good, basic step.

The testing system currently uses `nose2` & `jasmine`.

# Submitting Changes

1. Create (or finish creating) an issue referencing what needs to change.
2. Start your pull request (on your honor it's your own code).
3. If the build, documentation, or testing need changes, alert us to them.
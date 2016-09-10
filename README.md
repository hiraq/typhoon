# Typhoon (IS NOT A FRAMEWORK)

### Description

You can call _Typhoon_ as a bootstrapper and application manager for web application based on [Python Tornado Web Framework](http://www.tornadoweb.org).

### Versions

Latest release branch always at `master` branch.  Development branch always at `dev`.

```
Alpha: 0.6.1
```
Supported Python versions : `2.7.x`.

For current version, _Typhoon_ still on active development, the structure and API still on active
improvement.

### Abstract

Tornado is a great python framework for web application or server applications.  The problem come if we want to start to work for a new project, the problem is we just start it from scratch.  _Typhoon_ **is not a framework** on top of Tornado.

### Rationale

The purpose of _Typhoon_ is to make our structures between projects more consistent, and give you (and maybe your team) an idea how to start and manage a new project using Tornado.

And for the bonus, i tried to add some utilities that maybe we need it every time we start a new project such as for :


- Environment variables
- Session management
- Unit & integration tests
- Use Motor as main database driver for Mongo
- CLI Tools: routes, builder
- Custom cli commands from each app
- Dockerized

### Applications

The structure of _Typhoon_ is web application that consists of many apps.  Each app should `contain` three important informations :

- Application name
- Application routes
- Application custom commands

We register each app via `Registry` class to parse application name and their routes.  These routes will be used in `main.py` for `tornado.web.Application`.

### Flows 

_Typhoon_ designed to be easy to learn and also to modify.  You can modify current _Typhoon_ flows and create
your own flow.  I'm not enforce you to do this or that.

### Documentations

[Wiki](https://github.com/hiraq/typhoon/wiki).

### Contributions

Open for any contributions.  Just sent me your PR.  PR conditions:

```
[?] Make sure there are no conflict
[?] Give me detail explanation about your PR
[?] Make sure your changes not breaking core unit tests
```

For any ideas of improvement, bug / errors, we can use [github issues](https://github.com/hiraq/typhoon/issues), and follow these rules :

```
[PROPOSAL] <YOUR TITLE>
[BUG] <YOUR TITLE>
[ERROR] <YOUR TITLE>
```

### Current And Next Features

```
[x] Environment management
[x] Application container
[x] Registry management
[x] Routes command line
[x] Application skeleton builder
[x] Unit tests
[x] Dockerized
```

### License

See [BSD-3 LICENSE](https://github.com/hiraq/typhoon/blob/master/LICENSE)

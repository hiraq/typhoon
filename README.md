# Typhoon

### Description

You can call _Typhoon_ as a bootstrapper and application manager for web application based on [Python Tornado Web Framework](http://www.tornadoweb.org).

### Versions

Latest stable branch always at `master` branch.  Development branch always at `dev`.

```
Stable: 0.1.1
```

### Rationale

Tornado is a great python framework for web application or server applications.  But if we want to start to work in a new project, we just start it from scratch.  _Typhoon_ is not a framework on top of other framework (Tornado), the purpose of _Typhoon_ is to make our structures between projects more consistent.  

And for the bonus, i tried to add some utilities that maybe we need it every time we start a new project such as for :

- Application Container
- Environment variables
- Registry management

### Logic

The structure of _Typhoon_ is web application that consists of many apps.  Each app should `contain` two important informations :

- Application name
- Application routes

We register each app via `Registry` class to parse application name and their routes.  These routes will be used in `main.py` for `tornado.web.Application`.

### How To Use

Just clone this repo :

```
git clone https://github.com/hiraq/typhoon
```

Dont forget to use your [VirtualEnv](https://github.com/pypa/virtualenv) :

Create your first `env`:

```
virtualenv env
```
Activate your env:

```
source env/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

After you have done, just look at the structure.  I'll try to create the structure as simple as possible.

Put your apps in `apps` folder or just follow the `HelloApp` or `PingApp` as your guidance....and dont forget to use your imagination too :) .

Register your routes inside your application container.  You must create your own container class that inherit from
`Container` abstract class, and define your routes and name there.
Register your app into `Registry`  in `apps/registry.py`.

Please remember, that _Typhoon_ is about skeleton or bootstrapper. Feel free to modify the _main.py_ , _container.py_ , or _registry.py_ and use them to fullfill your needs.

### Environment Variables

Please look at more detail at `env.yml`.  Just use this file and add more environments such as:

- PRODUCTION
- TESTING
- STAGING

And set your configuration key and values based on environment.  Example:

```
DEV:
  DEBUG: true
  XSRF: false
  STATIC_HASH_CACHE: false
  COMPRESS_RESPONSE: false

PRODUCTION:
  DEBUG: false
  XSRF: true
  STATIC_HASH_CACHE: true
  COMPRESS_RESPONSE: true
```

Thanks for [MotherNature](https://github.com/femmerling/mothernature) for simple and usefull library ;) .

### Application Dependencies

Just put your required dependencies in `requirements.txt` and use :

```
pip install -r requirements.txt
```

Please dont expect any `magic` , and be simple, okay? :)

### Unit Tests

I'm a fan of unit test, but i'm not fanatic.  I just try to figure out how to manage our tests properly.  For now, i'm not decide yet any structures, for the library i'm using `unittest2`.

### How To Run Your Application

```
python main.py --port=8080 --env=PRODUCTION
```

This command will run your application on port `8080` (default: `8000`) and use `PRODUCTION` environment variables (default: `DEV`).

### Contributions

Open for any contributions.  Just sent me your PR.  PR conditions:

```
[?] Make sure there are no conflict for any PR
[?] Give me your detail explanation about your PR
```

For any ideas of improvement, bug / errors can use [github issues](https://github.com/hiraq/typhoon/issues), and use :

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
[?] Unit tests
[?] Routes command line
[?] Application skeleton builder
[?] Hooks
[?] Dockerized
```

### License

See [BSD-3 LICENSE](https://github.com/hiraq/typhoon/blob/master/LICENSE)

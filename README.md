# Typhoon (IS NOT A FRAMEWORK)

### Description

You can call _Typhoon_ as a bootstrapper and application manager for web application based on [Python Tornado Web Framework](http://www.tornadoweb.org).

### Versions

Latest stable branch always at `master` branch.  Development branch always at `dev`.

```
Stable: 0.2.0
```

### Rationale

Tornado is a great python framework for web application or server applications.  The problem come if we want to start to work for a new project, the problem is we just start it from scratch.  _Typhoon_ **is not a framework** on top of Tornado, the purpose of _Typhoon_ is to make our structures between projects more consistent, and give you (and maybe your team) an idea how to start and manage a new project using Tornado.
 
And for the bonus, i tried to add some utilities that maybe we need it every time we start a new project such as for :

- Environment variables
- Application Container
- Registry management
- CLI Tools: routes, builder

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

Current _Typhoon_ folder structures:

```
.
├── apps
├── assets
├── builder.py
├── env
├── env.yml
├── helpers
├── images
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
└── routes.py
```

Put your apps in `apps` folder or just follow the `HelloApp` or `PingApp` as your guidance....and dont forget to use your imagination too :) .

Current `apps` folder:

```
apps
├── hello
│   ├── __init__.py
│   ├── routes.py
├── ping
│   ├── __init__.py
│   ├── routes.py
├── registry.py
├── container.py
├── __init__.py
```

Register your routes inside your application container.  You must create your own container class that inherit from
`Container` abstract class, and define your routes and name there.
Register your application container into `Registry`  in `apps/registry.py`.

There are no rules how to manage your `app`, but for basic idea i just provide two files inside your `app` folder, and these two files *must be* exists inside your `app` folder:
- `__init__.py`
- `routes.py`

You can create your own structures inside your `app` folder.

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

### Routes CLI

Used to list of all registered routes from all apps.

Command line :

```
python routes.py list
```

example result :

```
| APPLICATION NAME   | PATH   | HANDLER     | METHOD   |
|--------------------+--------+-------------+----------|
| HelloApp           | /hello | MainHandler | GET      |
| PingApp            | /ping  | PingHandler | GET      |
| PingApp            | /pong  | PongHandler | GET      |
```

### Application Builder CLI

Used to build your `app` skeleton structures.

Command line :

```
python builder.py --app <YOURAPP>
```

example result :

```
=============================================================
INFO: Current Directory: /vagrant/typhoon
INFO: Application Directory: /vagrant/typhoon/apps/
=============================================================
INFO: Requested App Name: testing
=============================================================
INFO: Your application has been created.
```

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
[x] Routes command line
[x] Application skeleton builder
[?] Unit tests
[?] Hooks
[?] Dockerized
```

### License

See [BSD-3 LICENSE](https://github.com/hiraq/typhoon/blob/master/LICENSE)

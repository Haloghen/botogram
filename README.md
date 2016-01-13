## botogram [![Build Status](https://img.shields.io/travis/pietroalbini/botogram/master.svg)](https://travis-ci.org/pietroalbini/botogram) [![News channel](https://img.shields.io/badge/telegram_channel-@botogram__framework-0d86d7.svg?style=flat)][channel]

_A microframework for Telegram bots_

botogram is a MIT-licensed microframework, which aims to simplify the creation
of [Telegram bots][1]. It offers a concise, simple API, which allows you to
spend all your creativity in the bot, without worrying about anything else.

It also provides a robust, fully scalable bot runner process, which will be
able to process fastly high workloads. And as if this isn't enough, it has
builtin support for commands, with an automatically-generated ``/help``
command.

```python
import botogram
bot = botogram.create("YOUR-API-KEY")

@bot.command("hello")
def hello_command(chat, message, args):
    """Say hello to the world!"""
    chat.send("Hello world")

if __name__ == "__main__":
    bot.run()
```

You can find the documentation at [botogram.pietroalbini.io][2]. Also, you can
get all the news about botogram in its [Telegram channel][channel].

**Supported Python versions**: 3.4, 3.5

### Installation

botogram is currently in development, so a release doesn't exist yet.  
But if you want to install it anyway, you can clone the repository and install
it with setuptools. Be sure to have Python 3.4 (or a newer version), pip,
virtualenv, setuptools and [invoke][3] installed:

    $ git clone https://github.com/pietroalbini/botogram.git
    $ cd botogram
    $ invoke install

On some Linux systems you might need to wrap the ``make install`` command with
``sudo``, if you don't have root privileges.

[1]: https://core.telegram.org/bots
[2]: http://botogram.pietroalbini.io/docs
[3]: http://www.pyinvoke.org
[channel]: https://telegram.me/botogram_framework

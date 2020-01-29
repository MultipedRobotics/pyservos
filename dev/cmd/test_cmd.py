#!/usr/bin/env python
import cmd
import os
from colorama import Fore, Back

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    prompt = ">> "
    intro = "<<<< Intro banner >>>"

    def do_angle(self, arg):
        """angle [ID] [degrees]"""
        i, a = arg.split()
        a = float(a)
        i = int(i)
        if a and i:
            print(f"servo[{i}]: {a}")
        else:
            print("invalid args")

    def do_reset(self, arg):
        """reset [ID] [level]
    1 = all
    2 = all but ID
    3 = all but ID and datarate
        """
        i, l = arg.split()
        i = int(i)
        l = int(l)
        print(f"reset[{i}] to {l}")

    def do_q(self, line):
        """[q]uit"""
        # exit(1)
        return True

    def do_greet(self, person):
        """greet [person] Greet the named person"""
        if person:
            print("hi,", person)
        else:
            print('hi')

    def do_EOF(self, line):
        """Hit ctrl-D exits program"""
        print("ctrl-D detected ... stopping")
        return True

    def postloop(self):
        """run at exit"""
        print("bye ...")

    def preloop(self):
        print("welcome")
        print("to exit, press ctrl-D")
        print(dir(self))

    # def do_prompt(self, line):
    #     self.prompt = line + ">>"

    # last_output = ''

    def do_shell(self, line):
        "Run a shell command"
        print(Fore.GREEN + "running shell command:" + Fore.YELLOW + line)
        output = os.popen(line).read()
        print(Fore.CYAN + output + Fore.RESET)
        # self.last_output = output

    # def parseline(self, line):
    #     print('parseline({!r}) =>'.format(line), end='')
    #     ret = cmd.Cmd.parseline(self, line)
    #     print(ret)
    #     return ret

    def onecmd(self, line):
        # print('onecmd({})'.format(s))
        # return cmd.Cmd.onecmd(self, s)
        try:
            return super().onecmd(line)
        except Exception as e:
            print(e)
            print(line)
            if line is not None:
                # print(self['go_'+line.split()[0]].__doc__)
                func = line.split()[0]
                print(getattr(self, 'do_' + func).__doc__)
            # print(super().onecmd.__doc__)
            self.last_line = " "
            return False

    # def cmdloop(self, intro=None):
    #     print('cmdloop({})'.format(intro))
    #     return cmd.Cmd.cmdloop(self, intro)

if __name__ == '__main__':
    HelloWorld().cmdloop()

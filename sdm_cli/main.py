import fire
from sdm_cli.constants import SDK


class Command:
    def calendar_update(self, sdk: SDK):
        print('calendar_update')

def main():
    print('hello sdm-cli')
    fire.Fire(Command)
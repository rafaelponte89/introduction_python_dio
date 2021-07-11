




class Television:
    def __init__(self):
        self.on = False
        self.channel = 5

    def power(self):
        if self.on:
            self.on = False
        else:
            self.on = True

    def increase_channel(self):
        if self.on:
            self.channel +=1
    def decrease_channel(self):
        if self.on:
            self.channel -=1

print(__name__)
if __name__ == '__main__':
    television = Television()

    print('Television is on : {}'.format(television.on))
    television.power()
    print('Television is on: {}'.format(television.on))
    television.power()
    print('Television is on: {}'.format(television.on))
    television.power()
    print('Television is on: {}'.format(television.on))
    print('Channel: {}'.format(television.channel))
    television.increase_channel()
    television.increase_channel()
    print('Channel: {}'.format(television.channel))
    television.decrease_channel()
    print('Channel: {}'.format(television.channel))
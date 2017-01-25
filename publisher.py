from params import r
import sys

if __name__ == '__main__':
    name = sys.argv[1]
    channel = sys.argv[2]

    print 'Bienvenue {channel}'.format(**locals())

    while True:
        message = raw_imput('Entrez un message: ')
        if message.lower() == 'exit':
            break

        message = '{name} dit: {message}'.format(**locals())

        r.publish(channel, message)

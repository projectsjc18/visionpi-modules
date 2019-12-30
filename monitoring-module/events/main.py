# Services
from monitoring import Monitoring


def main():
    while True:
        print('Init Monitoring')
        mevents = Monitoring()
        mevents.monitoring_events()


main()

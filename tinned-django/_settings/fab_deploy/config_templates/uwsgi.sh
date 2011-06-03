#!/bin/sh

PYTHONPATH={{ PROJECT_DIR }}
MODULE=wsgi

### BEGIN INIT INFO
# Provides:          uwsgi
# Required-Start:    $all
# Required-Stop:     $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts the uwsgi app server
# Description:       starts uwsgi app server using start-stop-daemon
### END INIT INFO

PATH=/opt/uwsgi:/sbin:/bin:/usr/sbin:/usr/bin
DAEMON={{ ENV_DIR }}/bin/uwsgi

OWNER=uwsgi

NAME=uwsgi
DESC=uwsgi

test -x $DAEMON || exit 0

set -e

DAEMON_OPTS="-s 127.0.0.1:4000 -M 4 -t 30 -A 4 -p 4 -d /var/log/uwsgi/uwsgi.log --pythonpath $PYTHONPATH --module $MODULE --home {{ ENV_DIR }}/"

case "$1" in
  start)
        echo -n "Starting $DESC: "
        start-stop-daemon --start --chuid $OWNER:$OWNER --user $OWNER \
                --exec $DAEMON -- $DAEMON_OPTS
        echo "$NAME."
        ;;
  stop)
        echo -n "Stopping $DESC: "
        start-stop-daemon --signal 3 --user $OWNER --quiet --retry 2 --stop \
                --exec $DAEMON
        echo "$NAME."
        ;;
  reload)
        killall -1 $DAEMON
        ;;
  force-reload)
        killall -15 $DAEMON
       ;;
  restart)
        echo -n "Restarting $DESC: "
        start-stop-daemon --signal 3 --user $OWNER --quiet --retry 2 --stop \
                --exec $DAEMON
        sleep 1
        start-stop-daemon --user $OWNER --start --quiet --chuid $OWNER:$OWNER \
               --exec $DAEMON -- $DAEMON_OPTS
        echo "$NAME."
        ;;
  status)
        killall -10 $DAEMON
        ;;
      *)
            N=/etc/init.d/$NAME
            echo "Usage: $N {start|stop|restart|reload|force-reload|status}" >&2
            exit 1
            ;;
    esac
    exit 0
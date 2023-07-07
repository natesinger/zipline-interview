#!/bin/bash
python3 -m gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker server:app -w 4 -b 0.0.0.0:80 --log-level=info

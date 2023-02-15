# 🍌 Banana Demo on making a streaming API

This template to show how you can stream text (or any other data) from your model on Banana.
We use a few tricks to do this:
- a small hack to the transformers module to make the FlanT5 model output tokens as soon as they are ready, [repo here](https://github.com/ErikKaum/transformers-stream-hack).
- using FastAPI server-sent-events to send the chunks to a client as a stream. [This blog](https://devdojo.com/bobbyiliev/how-to-use-server-sent-events-sse-with-fastapi) is a useful intro.

## Note
Since the response comes as a stream of server-sent-events, the example output is not fully representative of how to handle it. `test.py` contains a more comlete example.
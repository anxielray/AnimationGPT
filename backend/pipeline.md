# AnimationGPT Pipeline

## Send Request

- First, after the server is up and running, the application will receive a request from the frontend.

- Below is a curl request to test the endpoint;

```sh
curl -X POST "http://127.0.0.1:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{"topic": "Black Holes"}'
```

## Topic Detection

The request is run into a system that detects what is is being said in the request. Try to relate the request unique words to the topic in STEM.

To test the topic detection, I added an endpoint, and below is a way to test it:

```sh
curl -X POST "http://127.0.0.1:8000/detect_topic" \
     -H "Content-Type: application/json" \
     -d '{"text": "How does gravity affect falling objects and motion?"}'
```


The NLP system generates a request to the animation creator.

The animation is generated with modifications based on what is being learned. The user should be able to adjust parameters to experience learning.

The response is returned back to the frontend and displayed to the user.

Moreover, before the animation is returned to the user in the frontend, the application calls on a system, to generate the script of the learning, in text{pdf, or show a snippet of the top.}

Additionally, the app adds a section wiht some questions based on the animationa generated to foster understanding of the topic in disussion.

If the user takes a step further and needs clarification about the questions presented, then the animation generation is disabled (the explanation is done without animation generation).
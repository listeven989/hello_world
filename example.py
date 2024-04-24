import runloop


@runloop.function
def hello_world(name: str) -> str:
    return f"Hello from the runloop cloud {name}!"

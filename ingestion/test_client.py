import asyncio
import websockets
import time

# The WebSocket endpoint we created in FastAPI
WS_URL = "ws://localhost:8000/stream"

# Some mock streaming data mimicking real-world feedback
MOCK_STREAM = [
    "I absolutely love this new update! The performance is lightning fast.",
    "This app keeps crashing every time I try to upload an image. Terrible experience.",
    "The interface is okay, but it lacks dark mode support. Please add it soon.",
    "Wow, the semantic search feature is completely changing how I find my documents!",
    "Extremely frustrated with the customer support response time. It has been 3 days."
]

async def stream_data():
    logger_prefix = "[MockClient]"
    print(f"{logger_prefix} Connecting to {WS_URL}...")
    
    try:
        async with websockets.connect(WS_URL) as websocket:
            print(f"{logger_prefix} Connected successfully! Starting live stream...")
            
            for msg in MOCK_STREAM:
                print(f"{logger_prefix} Sending event: '{msg}'")
                await websocket.send(msg)
                
                # Sleep for 1 second between messages to simulate real-time intervals
                await asyncio.sleep(1)
                
            print(f"{logger_prefix} Finished streaming mock data batches.")
            
    except Exception as e:
        print(f"{logger_prefix} Connection error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(stream_data())
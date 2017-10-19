"""
Send sample query to prediction engine
"""

import predictionio
engine_client = predictionio.EngineClient(url="http://localhost:8000")
print(engine_client.send_query({"userEntityId": "u1", "number": 4}))

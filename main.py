from datadog import initialize, api
import time

options = {
    'api_key': '<YOUR_API_KEY>',
    'app_key': '<YOUR_APP_KEY>'
}

initialize(**options)

now = time.time()
future_10s = now + 10

# Submit multiple metrics
api.Metric.send([{
    'metric': 'minecraft.server.memoryused',
    'points': 15
},
{
    'metric': 'minecraft.server.chunksloaded',
    'points': 15
},
{
    'metric': 'minecraft.server.tickspersecond',
    'points': 15
},
{
    'metric': 'minecraft.server.playercount',
    'points': 16
}])

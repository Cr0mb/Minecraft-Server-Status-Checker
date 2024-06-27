# Minecraft-Server-Status-Checker
This Python script allows you to check the status of Minecraft servers (both Java Edition and Bedrock Edition) using the MCSrvStatus API. 

It provides information such as server version, player count, MOTD (Message of the Day), plugins, and mods if available. 

The script also supports an option to exit gracefully.

## Features

> Check Minecraft server status (online/offline).

> Display server version, player count, MOTD, plugins, and mods (if available).

## Requirements
- Python 3.x
```
pip install colorama requests
```

## MCSrvStatus API

- API responses are cached for 1 minute to reduce load on the server and improve performance.

- Cached responses include metadata like cache hit status, cache time, and expiration time.

```
More info: https://api.mcsrvstat.us
```


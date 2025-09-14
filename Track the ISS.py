"""
Install the following libraries: `requests`, `matplotlib`.
    in terminal: pip install requests matplotlib 
Use `requests` to track the location of the International Space Station. Generate at least 100 data points with the latitude, longitude, and timestamp of the data point. You may do this by pinging this API once every 10 seconds for 17 or so minutes.
    https://api.wheretheiss.at/v1/satellites/25544
Use `matplotlib` to illustrate the path of the ISS. Use any visualization you feel is appropriate.
"""

import requests
import time
import pandas as pd
import matplotlib.pyplot as plt

data = []

for i in range(100):
    response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
    iss_data = response.json()

    timestamp = iss_data['timestamp']
    lat = iss_data['latitude']
    lon = iss_data['longitude']

    data.append({
        "timestamp": timestamp,
        "latitude": lat,
        "longitude": lon
    })

    print(f"Point {i+1}: {lat}, {lon}, {timestamp}")
    
    time.sleep(10)

df = pd.DataFrame(data)
df.to_csv("iss_data.csv", index=False)

plt.figure(figsize=(12,6))
plt.plot(df['longitude'], df['latitude'], marker='o', markersize=3, linestyle='-', color='pink')
plt.title('Path of the International Space Station (ISS)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()
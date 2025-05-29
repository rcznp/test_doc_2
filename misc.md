
# 📥 Download InfluxDB Data as Excel-Compatible CSV

gets the accelerometer data (`x`, `y`, `z`) from InfluxDB for a specific time range and saves it as a CSV file that can be opened with Excel.

```bash
influx query "from(bucket: \"w03SensorData\") |> range(start: 2025-04-23T02:00:58Z, stop: 2025-04-23T04:00:00Z) |> filter(fn: (r) => r._measurement == \"accelerometer\") |> filter(fn: (r) => r._field == \"x\" or r._field == \"y\" or r._field == \"z\") |> yield(name: \"raw\")" --raw --org "thingworx" --host http://10.107.107.180:8086 --token "oBJrTD0fITennbPQgiDCxojgE0Zn_BwCQ9-fTlY3JuqBg7sM1rayD5Ba4Lo5p6_IpHZKADAIObydKp_wE9Nf4w==" > test_data_apr23.csv
```

💡 Open `test_data_apr23.csv` with Excel to view and analyze the downloaded accelerometer data.

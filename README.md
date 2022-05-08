# Surfs_Up

### Purpose
To analyze temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.
##### Results:

- December temperatures average approximately 4 degrees cooler than June.
- December shows a greater fluctuation in temperatures with a standard deviation of 3.75 vs a standard deviation of 3.26 in June.
- December minimum temperature is 8 degrees cooler than June, while the max temperature is only 2 degrees cooler.

![June temps](https://github.com/lindseyasterman/surfs_up/blob/main/June_temps_statistics.png)

![Dec temps](https://github.com/lindseyasterman/surfs_up/blob/main/Dec_temps_statistics.png)


##### Summary:

While June is certainly warmer and more conducive to a profitable surf and ice cream shop business, December remains relatively temperate.  This weather would still be enjoyable to tourists year-round. For additional information, it would be important to look at rain fall amounts for June and December. This could be accomplished with the following code for precipitation in June and then refactored for December:
```
results = session.query(Measurement.date, Measurement.prcp).filter(func.strftime("%m", Measurement.date) == "06").all()

```
It might also be helpful to compare rainfall amounts from around the island using results from various stations.  This could be accomplished by adding a filter statement to the query as follows:
```
filter(Measurement.station == 'station_name').
```


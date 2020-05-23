SELECT today.Id
FROM Weather today, Weather yesterday
WHERE DATE_ADD(yesterday.RecordDate, INTERVAL 1 DAY) = today.RecordDate AND today.Temperature > yesterday.Temperature;

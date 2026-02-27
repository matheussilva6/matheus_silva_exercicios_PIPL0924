import requests as rex

request=rex.get("https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId=14526&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1771804800&end=1772409600&_=1771939774069%22%22")

print(request.text)
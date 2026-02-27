import requests as rex
 
for i in range(7000,7194):
    request=rex.get("https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId=i2&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1771804800&end=1772409600&_=1771937905632%22%22")
 
    print(i,"request : ",request.request)
   
    if "Pedro Carlos Mestre dos Santos" in request.text:
        print("Eencontrado no ID:", i)
    else:
        print(f"ID : {i} Pedro Carlos Mestre dos Santos nao existe")
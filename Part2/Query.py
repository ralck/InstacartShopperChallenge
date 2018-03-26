import sqlite3
import dateutil.parser
import datetime
import sys

def ValidateArgs():
    if len(sys.argv) is not 3:
        print("Usage: Python query.py start_date end_date")

    startDate = ''
    endDate = ''

    try:
        startDate = dateutil.parser.parse(sys.argv[1])
        endDate = dateutil.parser.parse(sys.argv[2])
    except:
        print("One ore more invalid date strings.")
        return (False, startDate, endDate)

    return (True, startDate, endDate)

def GetStartDate(theDate):
    # Helper function to get the monday before a given date
    return theDate - datetime.timedelta(days=theDate.weekday())

def RunQuery(sDate, eDate):
    print("count,week,workflow_state")

    # Validate sDate starts a week and eDate ends a week
    if not sDate.weekday() == 0:
        sDate += datetime.timedelta(days=(7-sDate.weekday()))
    if not eDate.weekday() == 0:
        eDate -= datetime.timedelta(days=eDate.weekday())

    # one query per week
    currentDate = sDate

    conn = sqlite3.connect('applicants.sqlite3')
    curs = conn.cursor()

    while(currentDate < eDate):
        endOfWeek = currentDate + datetime.timedelta(days=7)
        dates = (currentDate, endOfWeek)

        curs.execute('''SELECT COUNT(created_at), workflow_state FROM applicants WHERE created_at >= ? AND created_at < ? GROUP BY workflow_state''', dates)
        sqlResults = curs.fetchall()
        for result in sqlResults:
            print('{0},{1},{2}'.format(result[0], currentDate.date(), result[1]))

        currentDate = endOfWeek
    conn.close()

    # One query, post processing in Python
    # dates = (sDate,eDate)
    #
    # conn = sqlite3.connect('applicants.sqlite3')
    # curs = conn.cursor()
    # curs.execute('''SELECT workflow_state, created_at FROM applicants WHERE created_at >= ? AND created_at <= ?''', dates)
    # sqlResults = curs.fetchall()
    # conn.close()
    #
    # dateSets={}
    # for result in sqlResults:
    #     try:
    #         dateGroup = GetStartDate(dateutil.parser.parse(result[1])).date()
    #         if(not dateGroup in dateSets):
    #             dateSets[dateGroup] = {}
    #         if(not result[0] in dateSets[dateGroup]):
    #             dateSets[dateGroup][result[0]] = 0
    #         dateSets[dateGroup][result[0]] += 1
    # for weeksKey, weeksValue in dateSets.items():
    #     for workflowKey, workflowValue in weeksValue.items():
    #         print('{0}.{1}.{2}'.format(workflowValue, weeksKey, workflowKey))




if(__name__=='__main__'):
    result = ValidateArgs()
    if(result[0]):
        RunQuery(result[1], result[2])

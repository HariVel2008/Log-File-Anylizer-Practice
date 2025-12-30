
from AnalyzerModule import Analyzer
from ReportModule import Report

logLines = []

with open("server.log") as file:
    for line in file:
        logLines.append(line.strip())

a = Analyzer(logLines)

infos, warnings, errors, totalEntries = a.analyzeCount()
comError, count = a.getComErr()

report = Report(infos, warnings, errors, totalEntries, comError, count)

print(report.createReport())


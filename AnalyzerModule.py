
class Analyzer:
    def __init__(self, logLines):
        self.logLines = logLines

    def analyzeCount(self):

        info = 0
        warning = 0
        error = 0
        totalEntries = len(self.logLines)

        for log in self.logLines:
            if "INFO" in log:
                info += 1
            elif "WARNING" in log:
                warning += 1
            elif "ERROR" in log:
                error += 1

        return info, warning, error, totalEntries
    
    def getComErr(self):
        highestCount = 0
        highestLog = ""

        errLogs = []

        for log in self.logLines:
            errLogs.append(log[26:])

        for log in errLogs:
            tempLog = log
            tempCount = 0
            for l in errLogs:
                if tempLog == l:
                    tempCount += 1
            
            if tempCount > highestCount:
                highestCount = tempCount
                highestLog = tempLog

        return highestLog, highestCount

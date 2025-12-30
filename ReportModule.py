class Report:
    def __init__(self, infos, warnings, errors, totalEntries, comErr, count):
        self.infos = infos
        self.warnings = warnings
        self.errors = errors
        self.comErr = comErr
        self.count = count
        self.totalEntries = totalEntries

    def createReport(self):
        report = "==== LOG SUMMARY ====\nTotal Entries: " + str(self.totalEntries) + "\n\nINFO: " + str(self.infos) + "\nWARNING: " + str(self.warnings) + "\nERROR: " + str(self.errors) + "\n\nMost Common ERROR: \"" + self.comErr + "\" (" + str(self.count) + " times)"
        return report 
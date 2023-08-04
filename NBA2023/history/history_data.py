import json

from history_traditional import Traditional

def compare_traditional(traditional_row):
    return (traditional_row.YEAR)

class history_data:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.traditional_data   = []
        self.advanced_data      = []
        self.misc_data          = []
        self.scoring_data       = []
        self.usage_data         = []

    def to_dict(self):
        listTraditional = [row.to_dict() for row in self.traditional_data]
        listAdvanced = [row.to_dict() for row in self.advanced_data]
        listMisc = [row.to_dict() for row in self.misc_data]
        listScoring = [row.to_dict() for row in self.scoring_data]
        listUsage = [row.to_dict() for row in self.usage_data]
        return {
            'id':self.id,
            'name':self.name,
            'traditional':listTraditional,
            "advanced": listAdvanced,
            "misc": listMisc,
            "scoring": listScoring,
            "usage": listUsage
        }
    
    
    def to_csv(self):
        dataCsv = [["YEAR","YEAR_DATA",self.name]]
        
        arreglo_ordenado = sorted(self.traditional_data, key=compare_traditional)

        for indice,element in enumerate(arreglo_ordenado):
            dataCsv.append([indice + 1, element.YEAR, element.PTS])
        return dataCsv

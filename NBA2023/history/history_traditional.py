import json

class usage_row:
    def __init__(self, BY_YEAR, TEAM, GP, MIN, USG_PERCENT, FGM_PERCENT, FGA_PERCENT, THREE_PM_PERCENT, THREE_PA_PERCENT, FTM_PERCENT, FTA_PERCENT, OREB_PERCENT, DREB_PERCENT, REB_PERCENT, AST_PERCENT, TOV_PERCENT, STL_PERCENT, BLK_PERCENT, BLKA_PERCENT, PF_PERCENT, PFD_PERCENT, PTS_PERCENT):
        self.BY_YEAR = BY_YEAR
        self.TEAM = TEAM
        self.GP = GP
        self.MIN = MIN
        self.USG_PERCENT = USG_PERCENT
        self.FGM_PERCENT = FGM_PERCENT
        self.FGA_PERCENT = FGA_PERCENT
        self.THREE_PM_PERCENT = THREE_PM_PERCENT
        self.THREE_PA_PERCENT = THREE_PA_PERCENT
        self.FTM_PERCENT = FTM_PERCENT
        self.FTA_PERCENT = FTA_PERCENT
        self.OREB_PERCENT = OREB_PERCENT
        self.DREB_PERCENT = DREB_PERCENT
        self.REB_PERCENT = REB_PERCENT
        self.AST_PERCENT = AST_PERCENT
        self.TOV_PERCENT = TOV_PERCENT
        self.STL_PERCENT = STL_PERCENT
        self.BLK_PERCENT = BLK_PERCENT
        self.BLKA_PERCENT = BLKA_PERCENT
        self.PF_PERCENT = PF_PERCENT
        self.PFD_PERCENT = PFD_PERCENT
        self.PTS_PERCENT = PTS_PERCENT

    def to_json(self):
        return json.dumps(self.__dict__)

    def to_dict(self):
        return {
            'BY_YEAR': self.BY_YEAR,
            'TEAM': self.TEAM,
            'GP': self.GP,
            'MIN': self.MIN,
            'USG_PERCENT': self.USG_PERCENT,
            'FGM_PERCENT': self.FGM_PERCENT,
            'FGA_PERCENT': self.FGA_PERCENT,
            'THREE_PM_PERCENT': self.THREE_PM_PERCENT,
            'THREE_PA_PERCENT': self.THREE_PA_PERCENT,
            'FTM_PERCENT': self.FTM_PERCENT,
            'FTA_PERCENT': self.FTA_PERCENT,
            'OREB_PERCENT': self.OREB_PERCENT,
            'DREB_PERCENT': self.DREB_PERCENT,
            'REB_PERCENT': self.REB_PERCENT,
            'AST_PERCENT': self.AST_PERCENT,
            'TOV_PERCENT': self.TOV_PERCENT,
            'STL_PERCENT': self.STL_PERCENT,
            'BLK_PERCENT': self.BLK_PERCENT,
            'BLKA_PERCENT': self.BLKA_PERCENT,
            'PF_PERCENT': self.PF_PERCENT,
            'PFD_PERCENT': self.PFD_PERCENT,
            'PTS_PERCENT': self.PTS_PERCENT
        }
class scoring_row:
    def __init__(self, BY_YEAR, TEAM, GP, MIN, FGA_2PT_PERCENT, FGA_3PT_PERCENT, PTS_2PT_PERCENT, PTS_2PT_MR_PERCENT, PTS_3PT_PERCENT, PTS_FBPS_PERCENT, PTS_FT_PERCENT, PTS_OFFTO_PERCENT, PTS_PITP_PERCENT, FGM_2FGM_AST_PERCENT, FGM_2FGM_UAST_PERCENT, FGM_3FGM_AST_PERCENT, FGM_3FGM_UAST_PERCENT, FGM_AST_PERCENT, FGM_UAST_PERCENT):
        self.BY_YEAR = BY_YEAR
        self.TEAM = TEAM
        self.GP = GP
        self.MIN = MIN
        self.FGA_2PT_PERCENT = FGA_2PT_PERCENT
        self.FGA_3PT_PERCENT = FGA_3PT_PERCENT
        self.PTS_2PT_PERCENT = PTS_2PT_PERCENT
        self.PTS_2PT_MR_PERCENT = PTS_2PT_MR_PERCENT
        self.PTS_3PT_PERCENT = PTS_3PT_PERCENT
        self.PTS_FBPS_PERCENT = PTS_FBPS_PERCENT
        self.PTS_FT_PERCENT = PTS_FT_PERCENT
        self.PTS_OFFTO_PERCENT = PTS_OFFTO_PERCENT
        self.PTS_PITP_PERCENT = PTS_PITP_PERCENT
        self.FGM_2FGM_AST_PERCENT = FGM_2FGM_AST_PERCENT
        self.FGM_2FGM_UAST_PERCENT = FGM_2FGM_UAST_PERCENT
        self.FGM_3FGM_AST_PERCENT = FGM_3FGM_AST_PERCENT
        self.FGM_3FGM_UAST_PERCENT = FGM_3FGM_UAST_PERCENT
        self.FGM_AST_PERCENT = FGM_AST_PERCENT
        self.FGM_UAST_PERCENT = FGM_UAST_PERCENT

    def to_json(self):
        return json.dumps(self.__dict__)

    def to_dict(self):
        return {
            'BY_YEAR': self.BY_YEAR,
            'TEAM': self.TEAM,
            'GP': self.GP,
            'MIN': self.MIN,
            'FGA_2PT_PERCENT': self.FGA_2PT_PERCENT,
            'FGA_3PT_PERCENT': self.FGA_3PT_PERCENT,
            'PTS_2PT_PERCENT': self.PTS_2PT_PERCENT,
            'PTS_2PT_MR_PERCENT': self.PTS_2PT_MR_PERCENT,
            'PTS_3PT_PERCENT': self.PTS_3PT_PERCENT,
            'PTS_FBPS_PERCENT': self.PTS_FBPS_PERCENT,
            'PTS_FT_PERCENT': self.PTS_FT_PERCENT,
            'PTS_OFFTO_PERCENT': self.PTS_OFFTO_PERCENT,
            'PTS_PITP_PERCENT': self.PTS_PITP_PERCENT,
            'FGM_2FGM_AST_PERCENT': self.FGM_2FGM_AST_PERCENT,
            'FGM_2FGM_UAST_PERCENT': self.FGM_2FGM_UAST_PERCENT,
            'FGM_3FGM_AST_PERCENT': self.FGM_3FGM_AST_PERCENT,
            'FGM_3FGM_UAST_PERCENT': self.FGM_3FGM_UAST_PERCENT,
            'FGM_AST_PERCENT': self.FGM_AST_PERCENT,
            'FGM_UAST_PERCENT': self.FGM_UAST_PERCENT
        }
class misc_row:
    def __init__(self, BY_YEAR, TEAM, GP, MIN, PTS_OFF_TO, SECOND_PTS, FBPS, PITP, OPP_PTS_OFF_TO, OPP_SECOND_PTS, OPP_FBPS, OPP_PITP, BLK, BLKA, PF, PFD):
        self.BY_YEAR = BY_YEAR
        self.TEAM = TEAM
        self.GP = GP
        self.MIN = MIN
        self.PTS_OFF_TO = PTS_OFF_TO
        self.SECOND_PTS = SECOND_PTS
        self.FBPS = FBPS
        self.PITP = PITP
        self.OPP_PTS_OFF_TO = OPP_PTS_OFF_TO
        self.OPP_SECOND_PTS = OPP_SECOND_PTS
        self.OPP_FBPS = OPP_FBPS
        self.OPP_PITP = OPP_PITP
        self.BLK = BLK
        self.BLKA = BLKA
        self.PF = PF
        self.PFD = PFD

    def to_json(self):
        return json.dumps(self.__dict__)

    def to_dict(self):
        return {
            'BY_YEAR': self.BY_YEAR,
            'TEAM': self.TEAM,
            'GP': self.GP,
            'MIN': self.MIN,
            'PTS_OFF_TO': self.PTS_OFF_TO,
            'SECOND_PTS': self.SECOND_PTS,
            'FBPS': self.FBPS,
            'PITP': self.PITP,
            'OPP_PTS_OFF_TO': self.OPP_PTS_OFF_TO,
            'OPP_SECOND_PTS': self.OPP_SECOND_PTS,
            'OPP_FBPS': self.OPP_FBPS,
            'OPP_PITP': self.OPP_PITP,
            'BLK': self.BLK,
            'BLKA': self.BLKA,
            'PF': self.PF,
            'PFD': self.PFD
        }
class advanced_row:
    def __init__(self, YEAR, TEAM, GP, MIN, OFFRTG, DEFRTG, NETRTG, AST_PERCENT, AST_TO, AST_RATIO, OREB_PERCENT, DREB_PERCENT, REB_PERCENT, TO_RATIO, EFG_PERCENT, TS_PERCENT, USG_PERCENT, PACE, PIE):
        self.YEAR = YEAR
        self.TEAM = TEAM
        self.GP = GP
        self.MIN = MIN
        self.OFFRTG = OFFRTG
        self.DEFRTG = DEFRTG
        self.NETRTG = NETRTG
        self.AST_PERCENT = AST_PERCENT
        self.AST_TO = AST_TO
        self.AST_RATIO = AST_RATIO
        self.OREB_PERCENT = OREB_PERCENT
        self.DREB_PERCENT = DREB_PERCENT
        self.REB_PERCENT = REB_PERCENT
        self.TO_RATIO = TO_RATIO
        self.EFG_PERCENT = EFG_PERCENT
        self.TS_PERCENT = TS_PERCENT
        self.USG_PERCENT = USG_PERCENT
        self.PACE = PACE
        self.PIE = PIE

    def to_json(self):
        return json.dumps(self.__dict__)
    
    def to_dict(self):
        return {
            'YEAR': self.YEAR,
            'TEAM': self.TEAM,
            'GP': self.GP,
            'MIN': self.MIN,
            'OFFRTG': self.OFFRTG,
            'DEFRTG': self.DEFRTG,
            'NETRTG': self.NETRTG,
            'AST_PERCENT': self.AST_PERCENT,
            'AST_TO': self.AST_TO,
            'AST_RATIO': self.AST_RATIO,
            'OREB_PERCENT': self.OREB_PERCENT,
            'DREB_PERCENT': self.DREB_PERCENT,
            'REB_PERCENT': self.REB_PERCENT,
            'TO_RATIO': self.TO_RATIO,
            'EFG_PERCENT': self.EFG_PERCENT,
            'TS_PERCENT': self.TS_PERCENT,
            'USG_PERCENT': self.USG_PERCENT,
            'PACE': self.PACE,
            'PIE': self.PIE
        }
class traditional_row:
    def __init__(self, YEAR, TEAM, GP, MIN, PTS, FGM, FGA, FG_PERCENT, 
                 THREE_PM, THREE_PA, THREE_P_PERCENT, FTM, FTA, FT_PERCENT,
                 OREB, DREB, REB, AST, TOV, STL, BLK, PF, FP, DD2, TD3, PLUS_MINUS):
        self.YEAR = YEAR
        self.TEAM = TEAM
        self.GP = GP
        self.MIN = MIN
        self.PTS = PTS
        self.FGM = FGM
        self.FGA = FGA
        self.FG_PERCENT = FG_PERCENT
        self.THREE_PM = THREE_PM
        self.THREE_PA = THREE_PA
        self.THREE_P_PERCENT = THREE_P_PERCENT
        self.FTM = FTM
        self.FTA = FTA
        self.FT_PERCENT = FT_PERCENT
        self.OREB = OREB
        self.DREB = DREB
        self.REB = REB
        self.AST = AST
        self.TOV = TOV
        self.STL = STL
        self.BLK = BLK
        self.PF = PF
        self.FP = FP
        self.DD2 = DD2
        self.TD3 = TD3
        self.PLUS_MINUS = PLUS_MINUS

    def to_json(self):
        return json.dumps(self.__dict__)
    
    def to_dict(self):
        return {
            'YEAR': self.YEAR,
            'TEAM': self.TEAM,
            'GP': self.GP,
            'MIN': self.MIN,
            'PTS': self.PTS,
            'FGM': self.FGM,
            'FGA': self.FGA,
            'FG_PERCENT': self.FG_PERCENT,
            'THREE_PM': self.THREE_PM,
            'THREE_PA': self.THREE_PA,
            'THREE_P_PERCENT': self.THREE_P_PERCENT,
            'FTM': self.FTM,
            'FTA': self.FTA,
            'FT_PERCENT': self.FT_PERCENT,
            'OREB': self.OREB,
            'DREB': self.DREB,
            'REB': self.REB,
            'AST': self.AST,
            'TOV': self.TOV,
            'STL': self.STL,
            'BLK': self.BLK,
            'PF': self.PF,
            'FP': self.FP,
            'DD2': self.DD2,
            'TD3': self.TD3,
            'PLUS_MINUS': self.PLUS_MINUS
        }
class Traditional:
    def __init__(self):
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def to_json(self):
        rows_json = []
        for row in self.rows:
            rows_json.append(row.__dict__)
        return json.dumps(rows_json)

    def from_json(self, json_data):
        rows_json = json.loads(json_data)
        for row_json in rows_json:
            row = traditional_row(**row_json)
            self.add_row(row)

    def to_dict(self):
        list = [row.to_dict() for row in self.rows]
        return {
            'rows':list
        }

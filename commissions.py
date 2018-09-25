import backtrader as bt

PINNACLE_COMMISSIONS = [
# AP-AUS. INDEX
# BC-BRENT CRUDE
{'commission': 2.0, 'margin': 3150.0, 'mult': 1000.0, 'name': 'BC'},

# FC-FEED CATTLE
{'commission': 2.0, 'margin': 1500.0, 'mult': 500.0, 'name': 'FC'},
# LC-LIVE CATTLE
{'commission': 2.0, 'margin': 1500.0, 'mult': 400.0, 'name': 'LC'},
# CC-COCOA
{'commission': 2.0, 'margin': 1900.0, 'mult': 10.0, 'name': 'CC'},
# KC-COFFEE
{'commission': 2.0, 'margin': 2100.0, 'mult': 375.0, 'name': 'KC'},
# CR-CRB INDEX
{'commission': 2.0, 'margin': 4200.0, 'mult': 500.0, 'name': 'CR'},
# HG-COPPER #1
{'commission': 2.0, 'margin': 3100.0, 'mult': 25000.0, 'name': 'HG'},
# C_-CORN
{'commission': 2.0, 'margin': 800.0, 'mult': 5000.0, 'name': 'ZC'},
# CT-COTTON
{'commission': 2.0, 'margin': 2650.0, 'mult': 500.0, 'name': 'CT'},
# CL-CRUDE OIL
{'commission': 2.0, 'margin': 3100.0, 'mult': 1000.0, 'name': 'CL'},
# ED-EURODOLLARS
{'commission': 2.0, 'margin': 400.0, 'mult': 2500.0, 'name': 'ED'},
# FF-FED. FUNDS
{'commission': 2.0, 'margin': 500.0, 'mult': 4167.0, 'name': 'FF'},
# CB-10YR CAN BOND
{'commission': 2.0, 'margin': 2000.0, 'mult': 1000.0, 'name': 'CB'},
# GC-GOLD
{'commission': 2.0, 'margin': 3100.0, 'mult': 100.0, 'name': 'GC'},
# HO-HEATING OIL
{'commission': 2.0, 'margin': 3800.0, 'mult': 42000.0, 'name': 'HO'},

# LH-LIVE HOGS
{'commission': 2.0, 'margin': 1300.0, 'mult': 400.0, 'name': 'LH'},
# BG-BRENT GAS
# LB-LUMBER
{'commission': 2.0, 'margin': 2750.0, 'mult': 110.0, 'name': 'LH'},
# EC-EURODOLL COMP
# O_-OATS
{'commission': 2.0, 'margin': 675.0, 'mult': 5000.0, 'name': 'ZO'},
# JO-ORNGE JUICE
{'commission': 2.0, 'margin': 1000.0, 'mult': 150.0, 'name': 'OJ'},
# PA-PALLADIUM
{'commission': 2.0, 'margin': 6500.0, 'mult': 100.0, 'name': 'PA'},
# PL-PLATINUM
{'commission': 2.0, 'margin': 1900.0, 'mult': 50.0, 'name': 'PL'},
# DA-MILK III
{'commission': 2.0, 'margin': 850.0, 'mult': 2000.0, 'name': 'PL'},
# SP-S&P500, DAY
# SI-SILVER
{'commission': 2.0, 'margin': 3600.0, 'mult': 5000.0, 'name': 'SI'},
# S_-SOYBEANS
{'commission': 2.0, 'margin': 3600.0, 'mult': 5000.0, 'name': 'SI'},
# SM-SOYB. MEAL
# BO-SOYBEAN OIL
# SB-SUGAR #11
# SF-SWISS FRANC
# ER-MINI RUSSELL
# US-TBONDS COMP
# TY-TNOTE10 COMP
# FB-TNOTE5, COMP
# ZI-24HR SILVER
# W_-WHEAT
# KW-WHEAT, KC
# MW-WHEAT, MINN
# RB-RBOB GASOLINE
# NK-NIKKEI INDX
# DX-DOLLAR INDX
# NG-NATURAL GAS
# UA-TBONDS, DAY
# TA-TNOTE10 DAY
# AD-AUSTRAL. $
# MD-S&P 400
# NR-ROUGH RICE
# GI-GOLDMAN SAK
# XU-DJ EUROSTOXX
# EN-MINI NASDAQ
# RL-RUSS. 2000
# DJ-DOW JONES
# ES-MINI S&P500
# ND-NASDAQ 100
# MP-MEX. PESO
# SC-SP500, COMP
# AN-AUS $, COMP
# BN-B PND, COMP
# CN-CAN $, COMP
# SN-SW. FR COMP
# JN-YEN, COMP
# FX-EURO, DAY
# FN-EURO, COMP
# AX-GERMAN DAX
# DT-GERMAN BUND
# LX-FTSE 100
# GS-LONG GILT
# SS-STERLING
# FA-TNOTE5, DAY
# TD-TNOTE2, DAY
# TU-TNOTE2, COMP
# YM-MINI D.J.
# ZD-DOW JONE COMP
# XX-DJ STOXX 50
# HS-HANG SENG
# CA-CAC 40 INDEX
# UB-EURO BOBL
# UZ-EURO SCHATZ
# ZG-24HR GOLD
# ZC-24HR CORN
# ZL-24HR SOYOIL
# ZM-24HR SOYMEAL
# ZO-24HR OATS
# ZR-24HR R. RICE
# ZS-24HR SOYBEANS
# ZW-24HR WHEAT
# ZU-24HR CRUDEOIL
# ZB-24HR RBOB
# ZH-24HR HEAT OIL
# ZN-24HR NATL GAS
# ZK-24HR COPPER
# ZA-24HR PALADIUM
# ZP-24HR PLATINUM
# ZF-24HR FCATTLE
# ZT-24HR LCATTLE
# ZZ-24HR LEANHOGS


]

ALL_COMMISSIONS = [

# ES  CONTINUOUS E-MINI S&P 500 CONTRACT
{'commission': 2.0, 'margin': 6160.0, 'mult': 50.0, 'name': 'ES'},
# CL  CONTINUOUS CRUDE OIL CONTRACT
{'commission': 2.0, 'margin': 2695.0, 'mult': 1000.0, 'name': 'CL'},
# TY  CONTINUOUS 10 YR US TREASURY NOTE CONTRACT
{'commission': 2.0, 'margin': 990.0, 'mult': 1000.0, 'name': 'TY'}, #AKA ZN
# NQ  CONTINUOUS E-MINI NASDAQ 100 CONTRACT
{'commission': 2.0, 'margin': 6380.0, 'mult': 20.0, 'name': 'NQ'},
# EU  CONTINUOUS EURO FX CONTRACT
{'commission': 2.0, 'margin': 2310.0, 'mult': 125000.0, 'name': 'EU'}, # AKA 6E
# GC  CONTINUOUS GOLD CONTRACT
{'commission': 2.0, 'margin': 3000.0, 'mult': 100.0, 'name': 'GC'},
# FV  CONTINUOUS 5 YR US TREASURY NOTE CONTRACT
{'commission': 2.0, 'margin': 616.0, 'mult': 1000.0, 'name': 'FV'}, # AKA ZF
# YM  CONTINUOUS E-MINI DOW JONES $5 CONTRACT
{'commission': 2.0, 'margin': 5390.0, 'mult': 5.0, 'name': 'YM'},
# US  CONTINUOUS 30 YR US TREASURY BOND CONTRACT
{'commission': 2.0, 'margin': 2365.0, 'mult': 1000.0, 'name': 'US'}, # AKA ZB
# JY  CONTINUOUS JAPANESE YEN CONTRACT
{'commission': 2.0, 'margin': 2200.0, 'mult': 12500000.0, 'name': 'JY'}, # AKA 6J
# BP  CONTINUOUS BRITISH POUND CONTRACT
{'commission': 2.0, 'margin': 1980.0, 'mult': 62500.0, 'name': 'BP'}, #AKA 6B
# AD  CONTINUOUS AUSTRALIAN DOLLAR CONTRACT
{'commission': 2.0, 'margin': 1375.0, 'mult': 100000.0, 'name': 'AD'}, # AKA 6A
# NG  CONTINUOUS NATURAL GAS CONTRACT
{'commission': 2.0, 'margin': 1320.0, 'mult': 10000.0, 'name': 'NG'},
# TU  CONTINUOUS 2 YR US TREASURY NOTE CONTRACT
{'commission': 2.0, 'margin': 418.0, 'mult': 200000.0, 'name': 'TU'}, #AKA ZT
# CD  CONTINUOUS CANADIAN DOLLAR CONTRACT
{'commission': 2.0, 'margin': 1210.0, 'mult': 100000.0, 'name': 'CD'}, #AKA 6C
# C   CONTINUOUS CORN CONTRACT
{'commission': 2.0, 'margin': 792.0, 'mult': 50.0, 'name': 'C'}, #AKA C
# SI  CONTINUOUS SILVER CONTRACT
{'commission': 2.0, 'margin': 4000.0, 'mult': 5000.0, 'name': 'SI'},
# HG  CONTINUOUS COPPER CONTRACT
{'commission': 2.0, 'margin': 3000.0, 'mult': 25000.0, 'name': 'HG'},
# S   CONTINUOUS SOYBEANS CONTRACT
{'commission': 2.0, 'margin': 2035.0, 'mult': 50.0, 'name': 'S'}, #AKA ZS
# UB  CONTINUOUS ULTRA US TREASURY BOND CONTRACT
{'commission': 2.0, 'margin': 3410.0, 'mult': 1000.0, 'name': 'UB'}, #AKA TN
# LG  CONTINUOUS LONG GILT CONTRACT
{'commission': 2.0, 'margin': 2178.0, 'mult': 100000.0, 'name': 'LG'}, #AKA GLTL
# NN  CONTINUOUS NIKKEI 225 YEN INDEX CONTRACT
{'commission': 2.0, 'margin': 5720.0, 'mult': 5.0, 'name': 'NN'}, # AKA NKD
# W   CONTINUOUS WHEAT CONTRACT
{'commission': 2.0, 'margin': 1485.0, 'mult': 50.0, 'name': 'W'}, #AKA ZW
# SF  CONTINUOUS SWISS FRANC CONTRACT
{'commission': 2.0, 'margin': 3080.0, 'mult': 125000.0, 'name': 'SF'}, # AKA 6S
# HO  CONTINUOUS NEW YORK HARBOR ULSD CONTRACT
{'commission': 2.0, 'margin': 3200.0, 'mult': 4.2, 'name': 'HO'},
# EMD CONTINUOUS E-MINI S&P MIDCAP 400 CONTRACT
# RB  CONTINUOUS RBOB GASOLINE CONTRACT
{'commission': 2.0, 'margin': 3795.0, 'mult': 42000.0, 'name': 'RB'},
# DX  CONTINUOUS US DOLLAR INDEX CONTRACT
{'commission': 2.0, 'margin': 1815.0, 'mult': 1000.0, 'name': 'DX'},
# BO  CONTINUOUS SOYBEAN OIL CONTRACT
{'commission': 2.0, 'margin': 660.0, 'mult': 6000.0, 'name': 'BO'}, #AKA ZL
# SB  CONTINUOUS SUGAR #11 WORLD CONTRACT
{'commission': 2.0, 'margin': 1047.0, 'mult': 1120.0, 'name': 'SB'}, #AKA
# PX  CONTINUOUS MEXICAN PESO CONTRACT
{'commission': 2.0, 'margin': 1265.0, 'mult': 500000.0, 'name': 'PX'},#AKA 6M
# SM  CONTINUOUS SOYBEAN MEAL CONTRACT
{'commission': 2.0, 'margin': 1815.0, 'mult': 100.0, 'name': 'SM'},#AKA ZM
# NE  CONTINUOUS NEW ZEALAND DOLLAR CONTRACT
{'commission': 2.0, 'margin': 1430.0, 'mult': 100000.0, 'name': 'NE'}, #AKA 6N
# TN  CONTINUOUS ULTRA 10 YR US TREASURY NOTE CONTRACT
# VX  CONTINUOUS CBOE VOLATILITY INDEX (VIX) CONTRACT
# NKD CONTINUOUS NIKKEI 225 DOLLAR INDEX CONTRACT
# KC  CONTINUOUS COFFEE CONTRACT
{'commission': 2.0, 'margin': 2310.0, 'mult': 375.0, 'name': 'KC'},
# PL  CONTINUOUS PLATINUM CONTRACT
{'commission': 2.0, 'margin': 1650.0, 'mult': 50.0, 'name': 'PL'},
# RTY CONTINUOUS E-MINI RUSSELL 2000 CONTRACT
# SS  CONTINUOUS MSCI SINGAPORE INDEX CONTRACT
# ED  CONTINUOUS EURODOLLAR CONTRACT
# XT  CONTINUOUS 10 YR AUSTRALIAN T BOND CONTRACT
# CT  CONTINUOUS COTTON #2 CONTRACT
# KW  CONTINUOUS HARD RED WINTER WHEAT CONTRACT
{'commission': 2.0, 'margin': 1850.0, 'mult': 50.0, 'name': 'KW'}, #AKA KE
# CC  CONTINUOUS COCOA CONTRACT
{'commission': 2.0, 'margin': 2090.0, 'mult': 10.0, 'name': 'CC'},
# HE  CONTINUOUS LEAN HOGS CONTRACT
{'commission': 2.0, 'margin': 1320.0, 'mult': 400.0, 'name': 'HE'},
# LE  CONTINUOUS LIVE CATTLE CONTRACT
{'commission': 2.0, 'margin': 1650.0, 'mult': 400.0, 'name': 'LE'},
# PA  CONTINUOUS PALLADIUM CONTRACT
{'commission': 2.0, 'margin': 8250.0, 'mult': 100.0, 'name': 'PA'},
# QW  CONTINUOUS WHITE SUGAR CONTRACT
# RS  CONTINUOUS CANOLA CONTRACT
# QC  CONTINUOUS LONDON COCOA CONTRACT
# GF  CONTINUOUS FEEDER CATTLE CONTRACT
{'commission': 2.0, 'margin': 3080.0, 'mult': 500.0, 'name': 'GF'},
# MW  CONTINUOUS HARD RED SPRING WHEAT CONTRACT
# LRC CONTINUOUS ROBUSTA COFFEE CONTRACT
# OJ  CONTINUOUS ORANGE JUICE - A CONTRACT
{'commission': 2.0, 'margin': 1249.0, 'mult': 150.0, 'name': 'OJ'},
# KPO CONTINUOUS CRUDE PALM OIL CONTRACT
# FN  CONTINUOUS NATURAL GAS BALANCING POINT CONTRACT
# MXE CONTINUOUS MDAX CONTRACT
# TA  CONTINUOUS STOXX EUROPE 600 BANKS CONTRACT
# SQ  CONTINUOUS STOXX EUROPE 50 INDEX CONTRACT
# FF  CONTINUOUS 30 DAY FED FUND CONTRACT
# STS CONTINUOUS STOXX EUROPE 600 BASIC RESOURCES CONTRACT
# CCM CONTINUOUS BRAZILIAN YELLOW CORN CONTRACT
# RR  CONTINUOUS ROUGH RICE CONTRACT
{'commission': 2.0, 'margin': 1210.0, 'mult': 12.5, 'name': 'RR'},#AKA ZR
# O   CONTINUOUS OATS CONTRACT
{'commission': 2.0, 'margin': 742.0, 'mult': 12.5, 'name': 'O'},#AKA ZO
# LB  CONTINUOUS RANDOM LENGTH LUMBER CONTRACT
{'commission': 2.0, 'margin': 1760.0, 'mult': 110.0, 'name': 'LB'},
# IR  CONTINUOUS 90 DAY BANK ACCEPTED BILL CONTRACT
# SEE CONTINUOUS STOXX EUROPE 600 OIL & GAS CONTRACT
# NCB CONTINUOUS ULTRA 10YR NOTE- T BOND CONTRACT
# BGI CONTINUOUS LIVE CATTLE CONTRACT
# DIJ CONTINUOUS 1 DAY BANK DEPOSITS CONTRACT
# ICF CONTINUOUS ARABICA COFFEE 4/5 CONTRACT
# TEX CONTINUOUS 10YR NOTE- ULTRA 10 YR NOTE 3:2 CONTRACT
# UX  CONTINUOUS EUA CONTRACT
# IHO CONTINUOUS HEATING OIL CONTRACT
{'commission': 2.0, 'margin': 3520.0, 'mult': 42000.0, 'name': 'IHO'}, #AKA HO
# BR  CONTINUOUS BRAZILIAN REAL CONTRACT

#FOREX
{'commission': 0.0, 'margin': 1.0, 'mult': 50.0, 'name': 'EURUSD'},


]

class forexSpreadCommisionScheme(bt.CommInfoBase):
    '''
    This commission scheme attempts to calcuate the commission hidden in the
    spread by most forex brokers. It assumes a mid point data is being used.

    *New Params*
    spread: Float, the spread in pips of the instrument
    JPY_pair: Bool, states whether the pair being traded is a JPY pair
    acc_counter_currency: Bool, states whether the account currency is the same
    as the counter currency. If false, it is assumed to be the base currency
    '''
    params = (
        ('spread', 2.0),
        ('stocklike', False),
        ('JPY_pair', False),
        ('acc_counter_currency', True),
        ('commtype', bt.CommInfoBase.COMM_FIXED),
        ('leverage',50),
        )

    def _getcommission(self, size, price, pseudoexec):
        '''
        This scheme will apply half the commission when buying and half when selling.
        If JPY pair change the multiplier accordingly.
        If account currency is same as the base currency, change pip value calc.
        '''
        if self.p.JPY_pair == True:
            multiplier = 0.01
        else:
            multiplier = 0.0001

        if self.p.acc_counter_currency == True:
            comm = abs((self.p.spread * (size * multiplier)/2))

        else:
            comm =  abs((self.p.spread * ((size / price) * multiplier)/2))

        return comm


code_to_month_name = {
    'F':	'January',
    'G':	'February',
    'H':	'March',
    'J':	'April',
    'K':	'May',
    'M':	'June',
    'N':	'July',
    'Q':	'August',
    'U':	'September',
    'V':	'October',
    'X':	'November',
    'Z':	'December',
}

code_to_month_num = {
    'F':	1,
    'G':	2,
    'H':	3,
    'J':	4,
    'K':	5,
    'M':	6,
    'N':	7,
    'Q':	8,
    'U':	9,
    'V':	10,
    'X':	11,
    'Z':	12,
}

sym_to_months = {
#Currencies

'AD': 	['H','M','U','Z'],
'BP': 	['H','M','U','Z'],
'CD': 	['H','M','U','Z'],
'DX': 	['H','M','U','Z'],
'EU': 	['H','M','U','Z'],
'JY': 	['H','M','U','Z'],
'SF': 	['H','M','U','Z'],

#Energies

'CL': 	['F','G','H','J','K','M','N','Q','U','V','X','Z'],
'HO': 	['F','G','H','J','K','M','N','Q','U','V','X','Z'],
'HU': 	['F','G','H','J','K','M','N','Q','U','V','X','Z'],
'NG': 	['F','G','H','J','K','M','N','Q','U','V','X','Z'],
'RB': 	['F','G','H','J','K','M','N','Q','U','V','X','Z'],
'ITCO': ['F','G','H','J','K','M','N','Q','U','V','X','Z'],

#Grains & Soy Complex

'BO': 	['F','H','K','N','Q','U','V','Z'],
'C': 	['F','H','K','N','U','X','Z'],
'KW': 	['H','K','N','U','Z'],
'MW': 	['H','K','N','U','Z'],
'O': 	['H','K','N','U','Z'],
'S': 	['F','H','K','N','Q','U','X'],
'SM': 	['F','H','K','N','Q','U','V','Z'],
'W': 	['H','K','N','U','Z'],

#Stock Indices

'ES': 	['H','M','U','Z'],

#Interest Rates

'ED': 	['H','M','U','Z'],
'FV': 	['H','M','U','Z'],
'MB': 	['H','M','U','Z'],
'TU': 	['H','M','U','Z'],
'TY': 	['H','M','U','Z'],
'US': 	['H','M','U','Z'],

#Meats

'FC': 	['F','H','J','K','Q','U','V','X'],
'LC': 	['G','J','M','Q','V','Z'],
'HE': 	['G','J','K','M','N','Q','V','Z'],
'PB': 	['G','H','K','N','Q'],
'DA': 	['F','G','H','J','K','M','N','Q','U','V','X','Z'],

#Metals

'GC': 	['G','J','M','Q','V','Z'],
'HG': 	['H','K','N','U','Z'],
'PL': 	['F','J','N','V'],
'SI': 	['H','K','N','U','Z'],

#Softs & Fibers

'RR': 	['F','H','K','N','U','X'],
'CC': 	['H','K','N','U','Z'],
'CT': 	['H','K','N','V','Z'],
'KC': 	['H','K','N','U','Z'],
'LB': 	['F','H','K','N','U','X'],
'JO': 	['F','H','K','N','U','X'],
'SB': 	['H','K','N','V'],
}

def get_contract_month_names(symbol):
    return list(map(lambda x: code_to_month_name[x],sym_to_months[symbol]))

def get_contract_month_nums(symbol):
    return list(map(lambda x: code_to_month_num[x],sym_to_months[symbol]))

def get_closest_contract(symbol,month):
    months = get_contract_month_nums(symbol)
    cur_contract = list(filter(lambda x: month <= x, months))
    return list(cur_contract)[0]

def get_next_contract_month(symbol,cur_month):
    cur_month = get_closest_contract(symbol,cur_month)
    months = get_contract_month_nums(symbol)
    next_index = (months.index(cur_month) + 1) % len(months)
    return get_contract_month_nums(symbol)[next_index]

def get_next_contract_distance(symbol,cur_month):
    cur_month = get_closest_contract(symbol,cur_month)
    next_month = get_next_contract_month(symbol,cur_month)
    if next_month < cur_month:
        next_month += 12

    return abs((cur_month - next_month) / 12)
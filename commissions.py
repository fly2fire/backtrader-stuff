import backtrader as bt

STEVENS_COMMISSIONS = [
#Symbol,Globex Symbol,Name,Exchange,Start Date,First Contract,Months,Number of Contracts,Contract Size,Tick Size,Pricing Unit,Deliverable,Big Point Value

# "CL","CL","NYMEX WTI Crude Oil","CME","1983-05-18","M1983","FGHJKMNQUVXZ","9","1,000 barrels","$0.01per barrel","U.S. Dollars and Cents per barrel","Delivery shall be made free-on-board (F.O.B.) at any pipeline or storage facility in Cushing Oklahoma with pipeline access to Enterprise Cushing storage or Enbridge Cushing storage. Delivery shall be made in accordance with all applicable Federal executive orders and all applicable Federal  State and local laws and regulations.","1000"
{'margin': 3150.0, 'mult': 1000.0, 'name': 'CME_CL'},
# "LN","HE","CME Lean Hogs","CME","1970-02-20","G1970","GJMNQVZ","2","40,000 pounds (~18 metric tons)","$.00025 per pound ($10 per contract)","Cents per pound","Hog (barrow and gilt) carcasses","400"
{'margin': 1350.0, 'mult': 400.0, 'name': 'CME_LN'},
# "W","ZW","CBOT Wheat","CME","1959-12-21","Z1959","HKNUZ","4","5,000 bushels (~ 136 metric tons)","1/4 of one cent per bushel ($12.50 per contract)","Cents per bushel","#2 Soft Red Winter at contract price, #1 Soft Red Winter at a 3 cent premium, other deliverable grades listed in Rule 14104.","50"
{'margin': 1550.0, 'mult': 50.0, 'name': 'CME_W'},
# "NK","NKD","CME Nikkei 225","CME","1990-12-13","Z1990","HMUZ","2","$5.00 x Nikkei Stock Average","5.00 index points=$25.00","Index Points","None, this contract is cash settled.","5"
{'margin': 5200.0, 'mult': 5.0, 'name': 'CME_NK'},
# "S","ZS","CBOT Soybeans","CME","1970-01-21","F1970","FHKNQUX","6","5,000 bushels (~136 metric tons)","1/4 of one cent per bushel ($12.50 per contract)","Cents per bushel","#2 Yellow at contract price, #1 Yellow at a 6 cent/bushel premium, #3 Yellow at a 6 cent/bushel discount","50"
{'margin': 2350.0, 'mult': 50.0, 'name': 'CME_S'},
# "ES","ES","CME S&P 500 Index E-Mini","CME","1997-12-18","Z1997","HMUZ","1","$50 x S&P 500 Index","0.25 index points=$12.50","Index Points","None, this contract is cash settled","50"
{'margin': 6000.0, 'mult': 50.0, 'name': 'CME_ES'},
# "MD","MD","CME S&P 400 Midcap Index","CME","1992-03-19","H1992","HMUZ","2","$100 x S&P 400 MidCap Index","0.10=$10.00","Index Points","None, this contract is cash settled.","500"
{'margin': 8200.0, 'mult': 500.0, 'name': 'CME_MD'},
# "AD","6A","CME Australian Dollar AUD","CME","1987-03-16","H1987","HMUZ","1","100,000 Australian dollars","$.0001 per Australian dollar increments ($10.00/contract). $.00005 per Australian dollar increments ($5.00/contract) for AUD/USD futures intra-currency spreads executed on the trading floor and electronically, and for AON transactions.","US dollars and cents per Australian dollars","100,000 Australian dollars","100000"
{'margin': 1250.0, 'mult': 100000.0, 'name': 'CME_AD'},
# "BO","ZL","CBOT Soybean Oil","CME","1961-09-20","U1961","FHKNQUVZ","2","60,000 pounds (lbs) (~ 27 metric tons)","1/100 of a cent ($0.0001) per pound ($6.00 per contract)","Cents per pound","Crude soybean oil meeting exchange-approved grades and standards-see exchange Rules and Regulations for exact specifications.","600"
{'margin': 600.0, 'mult': 600.0, 'name': 'CME_BO'},
# "B","","ICE Brent Crude Oil","ICE","1993-12-16","F1994","FGHJKMNQUVXZ","12","1,000 barrels","US dollars and cents","one cent per barrel","The ICE Brent Crude futures contract is a deliverable contract based on EFP delivery with an option to cash settle, i.e the ICE Brent Index price for the day following the last trading day of the futures contract.","1000"
#{'margin': 2350.0, 'mult': 1000.0, 'name': 'ICE_B'},
# "SI","SI","NYMEX Silver","CME","1964-03-30","H1964","FHKNUZ","1","5,000 troy ounces","Outright transactions including EFP: $0.005 per troy ounce. Straddle or spread transactions and settlement prices: $0.001 per troy ounce.","U.S. Cents per troy ounce","Silver delivered under this contract shall assay to a minimum of 999 fineness.","5000"
{'margin': 3600.0, 'mult': 5000.0, 'name': 'CME_SI'},
# "GC","GC","NYMEX Gold","CME","1975-02-25","G1975","GJMQVZ","2","100 troy ounces","$0.10 per troy ounce","U.S. Dollars and Cents per troy ounce","Gold delivered under this contract shall assay to a minimum of 995 fineness.","100"
{'margin': 3100.0, 'mult': 100.0, 'name': 'CME_GC'},
# "PA","PA","NYMEX Palladium","CME","1977-03-14","H1977","HMUZ","1","100 troy ounces","$0.05 per troy ounce","US dollars and cents per troy ounce","Palladium that is a minimum of 99.95% pure","100"
{'margin': 6500.0, 'mult': 100.0, 'name': 'CME_PA'},
# "HO","HO","NYMEX Heating Oil","CME","1979-12-28","F1980","FGHJKMNQUVXZ","2","42,000 gallons","$0.0001 per gallon","U.S. dollars and cents per gallon","The oil delivered shall be a pure hydrocarbon oil free from renewable fuel, biodiesel, alkali, mineral acid, grit, fibrous or other foreign matter, meeting the Delivery specifications of the Colonial Pipeline's Fungible Grade 62 for Ultra Low Sulfur Diesel","42000"
{'margin': 3800.0, 'mult': 42000.0, 'name': 'CME_HO'},
# "SF","6S","CME Swiss Franc CHF","CME","1975-09-15","U1975","HMUZ","1","125,000 Swiss francs","$.0001 per Swiss Franc increments ($12.50/contract). $.00005 per Swiss Franc increments ($6.25/contract) for CHF/USD futures intra-currency spreads executed on the trading floor and electronically, and for AON transactions.","US dollars and cents per Swiss Franc","125,000 Swiss Francs","125000"
#{'margin': 2600.0, 'mult': 125000.0, 'name': 'CME_SF'},
# "PL","PL","NYMEX Platinum","CME","1970-01-14","F1970","FJNV","1","50 troy ounces","$0.10 per troy ounce","dollars and Cents per troy ounce","Platinum that is a minimum of 99.95% pure","50"
{'margin': 1900.0, 'mult': 50.0, 'name': 'CME_PL'},
# "C","ZC","CBOT Corn","CME","1960-03-22","H1960","HKNUZ","4","5,000 bushels (~ 127 Metric Tons)","1/4 of one cent per bushel ($12.50 per contract)","Cents per bushel","#2 Yellow at contract Price, #1 Yellow at a 1.5 cent/bushel premium #3 Yellow at a 1.5 cent/bushel discount","50"
{'margin': 800.0, 'mult': 50.0, 'name': 'CME_C'},
# "SM","ZM","CBOT Soybean Meal","CME","1964-03-19","H1964","FHKNQUVZ","2","100 Short Tons (~ 91 metric tons)","10 cents per short ton ($10.00 per contract)","Dollars and Cents per short ton","48% Protein Soybean Meal, meeting the requirements listed in the CBOT Rules and Regulations","100"
{'margin': 1650.0, 'mult': 100.0, 'name': 'CME_SM'},
# "FV","ZF","CBOT 5-year US Treasury Note","CME","1988-06-21","M1988","HMUZ","1","One U.S. Treasury note having a face value at maturity of $100,000.","One-quarter of one thirty-second (1/32) of one point ($7.8125, rounded up to the nearest cent per contract), including intermonth spreads.","Points ($1,000) and quarters of 1/32 of a point. For example, 119-16 represents 119 16/32, 119-162 represents 119 16.25/32, 119-165 represents 119 16.5/32, and 119-167 represents 119 16.75/32. Par is on the basis of 100 points.","U.S. Treasury notes with an original term to maturity of not more than five years and three months and a remaining term to maturity of not less than four years and two months as of the first day of the delivery month. The invoice price equals the futures settlement price times a conversion factor, plus accrued interest. The conversion factor is the price of the delivered note ($1 par value) to yield 6 percent.","1000"
{'margin': 680.0, 'mult': 1000.0, 'name': 'CME_FV'},
# "NG","NG","NYMEX Natural Gas","CME","1990-05-22","M1990","FGHJKMNQUVXZ","9","10,000 million British thermal units (mmBtu).","$0.001 per MMBtu","U.S. dollars and cents per mmBtu.","Natural Gas meeting the specifications set forth in the FERC-approved tariff of Sabine Pipe Line Company as then in effect at the time of delivery shall be deliverable in satisfaction of futures contract delivery obligations.","10000"
{'margin': 1350.0, 'mult': 10000.0, 'name': 'CME_NG'},
# "ATW","","ICE Rotterdam Coal","ICE","2006-09-01","Z2006","FGHJKMNQUVXZ","2","1,000 metric tons","US dollars and cents per tonne","5 cents per tonne","Contracts are financially settled based upon the price of coal delivered into the Amsterdam, Rotterdam, and Antwerp region in the Netherlands. The contract is cash settled against the API 2 Index published in the Argus/McCloskey Coal Price Index Report.","50"
{'margin': 3000.0, 'mult': 50.0, 'name': 'ICE_ATW'},
# "RF","","ICE Russell 1000 Index Mini","ICE","2007-09-25","U2007","HMUZ","2","$100 times the Index","Index points, to two decimal places",".10 Index points","$100 times the Index Deliverable Good: Cash settlement to a special opening calculation of the Russell 2000 Index based on the opening prices of the component stocks on the third Friday of the contract month. Please see Exchange Rules 19.04 and 19.26 for additional information.","100"
#{'margin': 0.0, 'mult': 100.0, 'name': 'ICE_RF'},
# "DJ","ZD","CBOT Dow Jones Ind Avg (DJIA)","CME","1998-03-19","H1998","HMUZ","2","$10 x Dow Jones Industrial Average (DJIA)","1.00 index points=$10.00","Index Points","None, this contract is cash settled.","10"
#{'margin': 0.0, 'mult': 10.0, 'name': 'CME_DJ'},
# "TY","ZN","CBOT 10-year US Treasury Note","CME","1982-06-21","M1982","HMUZ","1","One U.S. Treasury note having a face value at maturity of $100,000.","One-half of one thirty-second (1/32) of one point ($15.625, rounded up to the nearest cent per contract), except for intermonth spreads, where the minimum price fluctuation shall be one-quarter of one thirty-second of one point ($7.8125 per contract).","Points ($1,000) and halves of 1/32 of a point. For example, 126-16 represents 126 16/32 and 126-165 represents 126 16.5/32. Par is on the basis of 100 points.","U.S. Treasury notes with a remaining term to maturity of at least six and a half years, but not more than 10 years, from the first day of the delivery month. The invoice price equals the futures settlement price times a conversion factor, plus accrued interest. The conversion factor is the price of the delivered note ($1 par value) to yield 6 percent.","1000"
{'margin': 1050.0, 'mult': 1000.0, 'name': 'CME_TY'},
# "KC","","ICE Coffee C","ICE","1973-12-26","Z1973","HKNUZ","2","37,500 pounds","Cents and hundredths of a cent up to two decimal places","5/100 cent/lb","Mexico, Salvador, Guatemala, Costa Rica, Nicaragua, Kenya, New Guinea, Panama, Tanzania, Uganda, Honduras, and Peru all at par, Colombia at 200 point premium, Burundi, Rwanda, Venezuela and India at 100 point discount, Dominican Republic and Ecuador at 400 point discount, and Brazil at 900 point discount.Effective starting with the May 2016 contract the differential for Colombia will become 400 points premium and the differential for Brazil will become 600 points discount.","375"
{'margin': 2100.0, 'mult': 375.0, 'name': 'ICE_KC'},
# "BP","B6","CME British Pound GBP","CME","1975-09-15","U1975","HMUZ","2","62,500 British pounds","$.0001 per British pound increments ($6.25/contract).","US dollars and cents","62,500 British pounds","62500"
{'margin': 1500.0, 'mult': 62500.0, 'name': 'CME_BP'},
# "JY","6J","CME Japanese Yen JPY","CME","1977-03-11","H1977","HMUZ","2","12,500,000 Japanese yen","$.000001 per Japanese yen increments ($12.50/contract). $.0000005 per Japanese yen increments ($6.25/contract) for JPY/USD futures intra-currency spreads executed on the trading floor and electronically, and for AON transactions.","US dollars and cents","12,500,000 Japanese yen","12.5"
{'margin': 2000.0, 'mult': 12.5, 'name': 'CME_JY'},
# "CD","D6","CME Canadian Dollar CAD","CME","1977-06-14","M1977","HMUZ","2","100,000 Canadian dollars","$.0001 per Canadian dollar increments ($10.00/contract). $.00005 per Canadian dollar increments ($5.00/contract) for CAD/USD futures intra-currency spreads executed on the trading floor and electronically, and for AON transactions.","US dollars and cents","100,000 Canadian dollars","100000"
{'margin': 1150.0, 'mult': 100000.0, 'name': 'CME_CD'},
# "DX","","ICE US Dollar Index","ICE","1999-03-18","H1999","HMUZ","2","$1,000 times the index ","US Dollar index points, calculated to three decimal places",".10 Index points","$1000 times the index value Deliverable Good: The US Dollar Index is physically settled on the third Wednesday of the expiration month against six component currencies (euro, Japanese yen, British pound, Canadian dollar, Swedish krona and Swiss franc) in their respective percentage weights in the Index. Settlement rates may be quoted to three decimal places.","1000"
{'margin': 1800.0, 'mult': 1000.0, 'name': 'ICE_DX'},
# "ED","GE","CME Eurodollar","CME","1982-03-15","H1982","HMUZ","9","Interest on Eurodollar deposits having a face value of $1,000,000 for three months.","Nearest expiring contract month: One quarter of one interest rate basis point = 0.0025 price points = $6.25 per contract. All other contract months:One half of one interest rate basis point = 0.005 price points = $12.50 per contract.","Quoted in IMM Three-Month LIBOR index points or 100 minus the rate on an annual basis over a 360 day year (e.g., a rate of 2.5% shall be quoted as 97.50). 1 basis point = .01 = $25.","None, this contract is cash settled","2500"
{'margin': 400.0, 'mult': 2500.0, 'name': 'CME_ED'},
# "M","","ICE UK Natural Gas","ICE","1997-02-27","H1997","FGHJKMNQUVXZ","2","1,000 therms per day per period","Sterling and pence per therm","5000 therms per day","Matching Acquiring and Disposing Trade Nominations (buyer from ICEU, seller to ICEU) are input by buyer and seller to National Grid via Gemini before 18:30 on the business day prior to the commencement of the delivery period. Delivery takes place in kilowatt-hours (29.3071 kilowatt hours per therm).","1"
#{'margin': 0.0, 'mult': 1.0, 'name': 'ICE_M'},
# "SP","SP","CME S&P 500 Index","CME","1982-06-17","M1982","HMUZ","2","$250 x S&P 500 Index","0.10 index points=$25","Index Points","None, this contract is cash settled.","250"
#{'margin': 0.0, 'mult': 250.0, 'name': 'CME_SP'},
# "T","","ICE WTI Crude Oil","ICE","2006-02-17","H2006","FGHJKMNQUVXZ","2","1,000 barrels","US dollars and cents","one cent per barrel","The West Texas Intermediate Light Sweet Crude Oil futures contract is cash settled against the prevailing market price for US light sweet crude. It is a price in USD per barrel equal to the penultimate settlement price for WTI crude futures as made public by NYMEX for the month of production per 2005 ISDA Commodity Definitions.","1000"
#{'margin': 0.0, 'mult': 1000.0, 'name': 'ICE_T'},
# "EC","6E","CME Euro FX","CME","1999-03-15","H1999","HMUZ","2","125,000 Euros","$.0001 per euro increments ($12.50/contract). $.00005 per euro increments ($6.25/contract) for EUR/USD futures intra-currency spreads executed on the trading floor and electronically, and for AON transactions.","US dollars and cents","None, this contract is cash settled.","125000"
{'margin': 2300.0, 'mult': 125000.0, 'name': 'CME_EC'},
# "CT","","ICE Cotton","ICE","1972-12-06","Z1972","HKNVZ","2","50,000 pounds net weight","Cents and hundredths of a cent per pound","/100 of a cent (one point) per pound","Quality : Strict Low Middling Staple Length: 1 2/32nd inc. Deliverable to: Galveston, TX, Houston, TX, Dallas/Ft. Worth, TS, Memphis, TN and Greenville/Spartanburg, SC.","500"
{'margin': 2650.0, 'mult': 500.0, 'name': 'ICE_CT'},
# "G","","ICE Gasoil","ICE","1990-09-12","U1990","FGHJKMNQUVXZ","2","100 metric tons",".US dollars and cents","25 cents per tonne","One or more lots of 100 metric tonnes of gasoil, with delivery by volume namely 118.35 cubic metres per lot being the equivalent of 100 metric tonnes of gasoil, at a density of 0.845 kg/litre in vacuum at 15C.","100"
{'margin': 3100.0, 'mult': 100.0, 'name': 'ICE_G'},
# "CC","","ICE Cocoa","ICE","1970-03-24","H1970","HKNUZ","1","10 metric tons","Dollars per metric tons","Dollar per metric ton","The growth of any country or clime, including new or yet unknown growths. Growths are divided into three classifications. Group A-Deliverable at a premium of $160/ton (including main crops of Ghana, Lome, Nigeria, Ivory Coast and Sierra Leone). Group B-Deliverable at a premium of $80/ton (includes Bahia, Arriba, Venezuela,Sanchez among others). Group C-Deliverable at par (includes Haiti, Malaysia and all others).Commencing with the July 2015 expiry, the growths of Peru and Colombia will be included in Group B.","10"
{'margin': 1900.0, 'mult': 10.0, 'name': 'ICE_CC'},
# "OJ","","ICE Orange Juice","ICE","1967-11-17","X1967","FHKNUX","2","15,000 pounds of orange juice solids (3% or less)","Cents and hundredths of a cent to two decimal places","5/100 of a cent per pound","The contract prices physical delivery of U.S. Grade A juice (with grading performed by the U.S. Department of Agriculture), in storage in exchange licensed warehouse in several U.S. delivery points. Allowed countries of origin are the U.S., Brazil, Costa Rica and Mexico.","150"
{'margin': 1000.0, 'mult': 150.0, 'name': 'ICE_OJ'},
# "LC","LE","CME Live Cattle","CME","1965-04-20","J1965","GJMQVZ","2","40,000 pounds (~18 metric tons)","$.00025 per pound (=$10 per contract)","Cents per pound","55% Choice, 45% Select, Yield Grade 3 live steers (or live heifers, effective with the August 2015 contract)","400"
{'margin': 1500.0, 'mult': 400.0, 'name': 'CME_LC'},
# "RB","RB","NYMEX Gasoline","CME","2005-12-30","F2006","FGHJKMNQUVXZ","2","42,000 gallons","$0.0001 per gallon","U.S. dollars and cents per gallon.","hydrocarbon oil free from alkali, mineral acid, grit, fibrous or other foreign matter, meeting the specifications as are in effect for downstream parties at the time of delivery meeting the requirements of Colonial Pipeline Company (Atlanta, Georgia) for: Fungible F Grade, Reformulated Regular Gasoline Blendstock (RBOB) for blending with 10% Denatured Fuel Ethanol (92% Purity) as defined in ASTM D-4806 as listed by the Colonial Pipeline as being properly designated for sale in New York and New Jersey in accordance with EPA regulations; provided, however, and notwithstanding anything to the contrary in the Colonial Pipeline specifications, the specifications set forth in Sections 101.1. through 101.5.","42000"
#XXX: RB throws everything off by a lot
#{'margin': 4000.0, 'mult': 42000.0, 'name': 'CME_RB'},
# "KW","KE","CME Kansas City Wheat","CME","1976-09-21","U1976","HKNUZ","2","5,000 bushels (~136 metric tons)","1/4 cent per bushel ($12.50 per contract)","Cents and quarter cents per bushel","No. 2 at contract price with a maximum of 10 IDK per 100 grams; No. 1 at a 1 1/2-cent premium. Deliverable grades of HRW shall contain a minimum 11% protein level. However, protein levels of less than 11%, but equal to or greater than 10.5% are deliverable at a ten cent (10) discount to contract price. Protein levels of less than 10.5% are not deliverable. When warehouse receipts are surrendered to the issuer for load-out, the taker of delivery shall have the option to, at the takers expense, request in the written load-out instructions that the wheat contain no more than 2 ppm of deoxynivalenol (vomitoxin). A determination of the level of vomitoxin shall be made at the point of origin by the Federal Grain Inspection Service or such other third party inspection service mutually agreeable to the maker and taker of delivery. A determination of the level of vomitoxin shall be based on the average test results of the wheat loaded in a single day from a single warehouse for each taker of delivery.","50"
{'margin': 1600.0, 'mult': 50.0, 'name': 'CME_KW'},
# "TF","","ICE Russell 2000 Index Mini","ICE","2007-03-16","H2007","HMUZ","2","$100 times the Index","Index points, to two decimal placse",".10 Index points","Cash settlement to a special opening calculation of the Russell 2000 Index based on the opening prices of the component stocks on the third Friday of the contract month. Please see Exchange Rules 19.04 and 19.26 for additional information.","100"
#{'margin': 0.0, 'mult': 100.0, 'name': 'ICE_TF'},
# "ZN","","SHFE Zinc","SHFE","2007-07-16","N2007","FHJKMNQUVXZ","2","5 ton","Yuan per ton","10 Yuan per ton","Standard products: 1# Standard Copper Cathode (Cu-CATH-2) as prescribed in the National Standard of GB/T467-2010, with Copper+Silver99.95%. Substitutions: Grade-A Copper (Cu-CATH-1) as prescribed in the National Standard of GB/T467-2010; or Grade-A Copper (Cu-CATH-1) as prescribed in BS EN 1978:1998",""
#{'margin': 0.0, 'mult': 1.0, 'name': 'SHFE_ZN'},
# "MP","","ICE British Pound GBP","ICE","2007-03-21","H2007","HMUZ","2","62,500 pounds","U.S. dollars per pound to 4 decimal places",".0001 or 6.25 U.S. dollars per contract","Cash settled based on exchange rate.","62500"
#{'margin': 0.0, 'mult': 62500.0, 'name': 'ICE_MP'},
# "NE","6N","CME New Zealand Dollar NZD","CME","2004-12-13","Z2004","HMUZ","1","100,000 New Zealand dollars","$.0001 per New Zealand dollar increments ($10.00/contract). $.00005 per New Zealand dollar ($5.00/contract) for NZD/USD futures intra-currency spreads executed on the trading floor and electronically, and for AON transactions.","US dollars and cents per New Zealand Dollar","100,000 New Zealand Dollars","100000"
{'margin': 1200.0, 'mult': 100000.0, 'name': 'CME_NE'},
# "NQ","NQ","CME NASDAQ 100 Index Mini","CME","1999-09-17","U1999","HMUZ","1","$20 x NASDAQ 100 Index","0.25 index points=$5.00","Index Points","None, this contract is cash settlted.","20"
{'margin': 6150.0, 'mult': 20.0, 'name': 'CME_NQ'},
# "O","","ICE Heating Oil","ICE","2006-04-27","K2006","FGHJKMNQUVXZ","2","42,000 gallons"," US dollars and cents",".01 cents per gallon","The cash settlement price in US Dollars and cents per Gallon is equal to the penultimate settlement price for New York Harbor ULSD Heating Oil Futures Contract as made public by NYMEX for the month of production as specified within the relevant Contract Rules by reference to the 2005 ISDA Commodity Definitions.","1000"
#{'margin': 0.0, 'mult': 1000.0, 'name': 'ICE_O'},
# "AL","","SHFE Aluminium","SHFE","2000-01-17","F2000","FHJKMNQUVXZ","2","5 ton","Yuan per ton","10 Yuan per ton","Standard products: 1# Standard Copper Cathode (Cu-CATH-2) as prescribed in the National Standard of GB/T467-2010, with Copper+Silver99.95%. Substitutions: Grade-A Copper (Cu-CATH-1) as prescribed in the National Standard of GB/T467-2010; or Grade-A Copper (Cu-CATH-1) as prescribed in BS EN 1978:1998",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'SHFE_AL'},
# "VX","","CBOE VIX Futures","CBOE","2007-12-19","Z2007","FHJKMNQUVXZ","2","The contract multiplier for each VX futures contract is $1000.","0.05 points, equal to $50.00 per contract","Index Points","None, this contract is cash settled",""
{'margin': 9000.0, 'mult': 1000.0, 'name': 'CBOE_VX'},
# "FGBM","","EUREX Euro-Bobl","EUREX","1995-12-08","Z1995","HMUZ","2","One German debt security with valute at maturity of EUR100000",".01 percent = EUR10","Percent of the par value","German debt security  with remaining term of 4.5 to 5.5 years with a 6% coupon.",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'EUREX_FBGM'},
# "US","ZB","CBOT 30-year US Treasury Bond","CME","1977-12-20","Z1977","HMUZ","2","One U.S. Treasury bond having a face value at maturity of $100,000.","One thirty-second (1/32) of one point ($31.25), except for intermonth spreads, where the minimum price fluctuation shall be one-quarter of one thirty-second of one point ($7.8125 per contract).","Points ($1,000) and 1/32 of a point. For example, 134-16 represents 134 16/32. Par is on the basis of 100 points.","U.S. Treasury bonds that, if callable, are not callable for at least 15 years from the first day of the delivery month or, if not callable, have a remaining term to maturity of at least 15 years from the first day of the delivery month. Note: Beginning with the March 2011 expiry, the deliverable grade for T-Bond futures will be bonds with remaining maturity of at least 15 years, but less than 25 years, from the first day of the delivery month. The invoice price equals the futures settlement price times a conversion factor, plus accrued interest. The conversion factor is the price of the delivered bond ($1 par value) to yield 6 percent.","1000"
{'margin': 2300.0, 'mult': 1000.0, 'name': 'CME_US'},
# "I","","LIFFE EURIBOR","LIFFE","1996-03-18","H1996","HMUZ","2","EUR1000000","0.005 (EUR12.50)","100.00 minus rate of interest","None, this contract is cash settled",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'LIFFE_I'},
# "PB","","SHFE Lead","SHFE","2011-09-15","U2011","FHJKMNQUVXZ","2","5 ton","Yuan per ton","10 Yuan per ton","Standard products: 1# Standard Copper Cathode (Cu-CATH-2) as prescribed in the National Standard of GB/T467-2010, with Copper+Silver99.95%. Substitutions: Grade-A Copper (Cu-CATH-1) as prescribed in the National Standard of GB/T467-2010; or Grade-A Copper (Cu-CATH-1) as prescribed in BS EN 1978:1998",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'SHFE_PB'},
# "C","","LIFFE London Cocoa","LIFFE","1993-09-30","U1993","HKNUZ","2","10 tonnes","GBP per metric tonne","1GBP per tonne","Physical Delivery: Standard Delivery Unit (SDU)  bagged cocoa with a nominal net weight of ten tonnes. Large Delivery Unit (LDU)  bagged cocoa with a nominal net weight of 100 tonnes. Bulk Delivery Unit (BDU)  loose cocoa with a nominal net weight of 1,000 tonnes",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'LIFFE_C'},
# "O","","CBOT Oats","CME","1970-03-19","H1970","HKNUZ","2","5000 bushels (86 metric tons)","1/4 of one cent per bushel ($12.50 per contract","US cents per bushel","No. 2 Heavy and No. 1 at par. No. 1 Extra Heavy at 7 cents per bushel over contract price. No. 2 Extra Heavy at 4 cents per bushel over contract price, and No. 1 Heavy at 3 cents per bushel over contract price. No. 2(36 pound total minimum test weight) at 3 cents per bushel under contract price and No. 2 (34 pound total minimum test weight) at 6 cents per bushel under contract price.",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'CME_O'},
# "RR","","CBOT Rough Rice","CME","1988-09-21","U1988","FHKNUX","2","2000 hundredweights (CWT) (91 Metric Tons)","1/2 cent per hundredweight ($10.00 per contract)","US cents per hundredweight","U.S. No. 2 or better long grain rough rice with a total milling yield of not less than 65% including head rice of not less than 48%. Premiums and discounts are provided for each percent of head rice over or below 55%, and for each percent of broken rice over or below 15%. No heat-damaged kernels are permitted in a 500-gram sample and no stained kernels are permitted in a 500-gram sample.  A maximum of 75 lightly discolored kernels are permitted in a 500-gram sample.",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'CME_RR'},
# "SXF","","MX Montreal S&P/TSX 60 Index","MX","1999-12-16","Z1999","HMUZ","2","C$200 times the S&P/TSX 60 Index Standard Futures contract value.","0.10 index points","Quoted in index points, expressed to two decimals.","None, this contract is cash settled",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'MX_SXF'},
# "LB","","CME Random Length Lumber","CME","1973-09-14","U1973","FHKNUX","2","110,000 nominal board feet (260 cubic meters)","$.10 per mbf ($11 per contract)","Dollars per 1,000 board feet (mbf)","2-inch by 4-inch nominal lumber, 8-20 feet long",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'CME_LB'},
# "FF","ZQ","CBOT 30-day Federal Funds","CME","1988-12-01","X1988","FGHJKMNQUVXZ","2","Interest on Fed Funds having a face value of $5,000,000 for one month.","Nearest expiring contract month: One-quarter of one basis point (0.0025), or $10.4175 per contract (1/4 of 1/100 of one percent of $5 million on a 30-day basis, rounded up to the nearest cent per contract). All other contract months: One-half of one basis point (0.005), or $20.835 per contract.","100 minus the average daily Fed Funds overnight rate for the delivery month (e.g., a 7.25 percent rate equals 92.75).","Expiring contracts are cash settled against the average daily Fed Funds overnight rate for the delivery month, rounded to the nearest one-tenth of one basis point. Final settlement occurs on the first business day following the last trading day. The daily Fed Funds overnight rate is calculated and reported by the Federal Reserve Bank of New York.","4167"
{'margin': 400.0, 'mult': 4167.0, 'name': 'CME_FF'},
# "HG","HG","COMEX Copper","CME","1959-12-29","Z1959","FHKNUZ","2","25,000 pounds","$0.0005 per pound","U.S. Cents per pound","25,000 pounds","25000"
{'margin': 3100.0, 'mult': 25000.0, 'name': 'CME_HG'},
# "SB","","ICE Sugar No. 11","ICE","1964-02-14","H1964","HKNV","2","112,000 pounds","Cents and hundredths of a cent per pound to two decimal places","1/100 cent/lb","Growths of Argentina, Australia, Barbados, Belize, Brazil, Colombia, Costa Rica, Dominican Republic, El Salvador, Ecuador, Fiji Islands, French Antilles, Guatemala, Honduras, India, Jamaica, Malawi, Mauritius, Mexico, Mozambique,Nicaragua, Peru, Republic of the Philippines, South Africa, Swaziland, Taiwan, Thailand, Trinidad, United States, and Zimbabwe acceptable. Deliverable to  port in the country of origin or in the case of landlocked countries, at a berth or anchorage in the customary port of export.","1120"
{'margin': 1100.0, 'mult': 1120.0, 'name': 'ICE_SB'},
# "TU","ZT","CBOT 2-year US Treasury Note","CME","1990-09-19","U1990","HMUZ","1","One U.S. Treasury note having a face value at maturity of $200,000.","One-quarter of one thirty-second (1/32) of one point ($15.625, rounded up to the nearest cent per contract), including intermonth spreads.","Points ($2,000) and quarters of 1/32 of a point. For example, 109-16 represents 109 16/32, 109-162 represents 109 16.25/32, 109-165 represents 109 16.5/32, and 109-167 represents 109 16.75/32. Par is on the basis of 100 points.",".S. Treasury notes with an original term to maturity of not more than five years and three months and a remaining term to maturity of not less than one year and nine months from the first day of the delivery month and a remaining term to maturity of not more than two years from the last day of the delivery month. The invoice price equals the futures settlement price times a conversion factor, plus accrued interest. The conversion factor is the price of the delivered note ($1 par value) to yield 6 percent.","2000"
{'margin': 460.0, 'mult': 2000.0, 'name': 'CME_TU'},
# "RB","","SHFE Rebar","SHFE","2009-09-15","U2009","FHJKMNQUVXZ","2","5 ton","Yuan per ton","10 Yuan per ton","Standard products: 1# Standard Copper Cathode (Cu-CATH-2) as prescribed in the National Standard of GB/T467-2010, with Copper+Silver99.95%. Substitutions: Grade-A Copper (Cu-CATH-1) as prescribed in the National Standard of GB/T467-2010; or Grade-A Copper (Cu-CATH-1) as prescribed in BS EN 1978:1998",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'SHFE_RB'},
# "MW","","MGEX Hard Red Spring Wheat","MGEX","1995-07-20","N1995","HKNUZ","2","5000 bushels","1/4 cent per bushel or $12.50 per contract","US Dollars and Cents per bushel","No. 2 or better Northern Spring Wheat with a protein content of 13.5% or higher, with 13% protein deliverable at a discount.",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'MGEX_MW'},
# "RU","","SHFE Natural Rubber","SHFE","2002-01-15","F2002","FHJKMNQUVX","2","10 ton","Yuan per ton","5 Yuan per ton","Standard goods: 1.Domestic: SCR WF as specified in the National Standard of GB8081-8089-87 2.Imported: RSS3 as specified in the International Quality And Packaging Standard of Rubber(1979)",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'SHFE_RU'},
# "FGBL","","EUREX Euro-Bund","EUREX","1991-03-06","H1991","HMUZ","2","One German debt security with valute at maturity of EUR100000",".01 percent = EUR10","Percent of the par value","German debt security  with remaining term of 8.5 to 10.5 years with a 6% coupon.",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'EUREX_FGBL'},
# "FDAX","","EUREX DAX","EUREX","1997-12-18","Z1997","HMUZ","2","25EUR per index point",".5 index point =12.5EUR","Index Points","None, this contract is cash settled.",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'EUREX_FDAX'},
# "L","","LIFFE Short Sterling","LIFFE","1990-09-19","U1990","HMUZ","2","Interest rate on three month depoist of GBP500000","0.01 (12.50)","100.00 minus rate of interest","None, this contract is cash-settled",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'LIFFE_L'},
# "CU","","SHFE Copper","SHFE","2000-01-17","F2000","FHJKMNQUVXZ","2","5 ton","Yuan per ton","10 Yuan per ton","Standard products: 1# Standard Copper Cathode (Cu-CATH-2) as prescribed in the National Standard of GB/T467-2010, with Copper+Silver99.95%. Substitutions: Grade-A Copper (Cu-CATH-1) as prescribed in the National Standard of GB/T467-2010; or Grade-A Copper (Cu-CATH-1) as prescribed in BS EN 1978:1998",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'SHFE_CU'},
# "FESX","","EUREX EURO STOXX 50 Index","EUREX","1998-09-18","U1998","HMUZ","2","10EUR per index point","1 index point =10EUR","Index Points","None, this contract is cash settled.",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'EUREX_FESX'},
# "FBTP","","EUREX Euro-BTP","EUREX","2010-03-08","H2010","HMUZ","2","One Italian debt security with valute at maturity of EUR100000","0.01 percent = EUR10","Percent of the par value","Italian debt security  with remaining term of 8.5 to 11 years with a 6% coupon.",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'EUREX_PBTP'},
# "MP","","CME Mexican Peso","CME","1995-06-19","M1995","HMUZ","2","500,000 Mexican pesos","$.00001 per Mexican peso increments ($5.00/contract)","US Dollars and cents","500,000 Mexican pesos",""
#TODO: pesos are also messed up
#{'margin': 1200.0, 'mult': 500000.0, 'name': 'CMD_MP'},
# "Z","","LIFFE FTSE 100 Index","LIFFE","1984-06-29","M1984","HMUZ","2"," 10 per index point",".5 index points = 5","Index Points","None, this contract is cash settled",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'LIFFE_Z'},
# "DA","","CME Class III Milk","CME","1997-12-31","Z1997","FGHJKMNQUVXZ","2","200,000 lbs. of Class III Milk ( 90 metric tons)","$0.01 per cwt (= $20.00 per contract)","Cents per hundredweight (cwt.)","Class III Milk",""
{'margin': 800.0, 'mult': 2000.0, 'name': 'CME_DA'},
# "YM","","CME E-mini Dow Jones","CME","1997-12-18","Z1997","HMUZ","2","$5 x Dow Jones Industrial Average (DJIA)","1.00 index points=$5.00","Index points","None this contract is cash settled",""
{'margin': 5300.0, 'mult': 4.0, 'name': 'CME_YM'},
# "FOAT","","EUREX Euro-OAT","EUREX","2013-03-07","H2013","HMUZ","2","One French debt security with valute at maturity of EUR100000","0.01 percent = EUR10","Percent of the par value","French debt security  with remaining term of 8.5 to 10.5 years with a 6% coupon.",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'EUREX_FOAT'},
# "FGBS","","EUREX Euro-Schatz","EUREX","1999-03-08","H1999","HMUZ","2","One German debt security with valute at maturity of EUR100000","0.005 percent = EUR5","Percent of the par value","German debt security  with remaining term of 1.75 to 2.25 years with a 6% coupon.",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'EUREX_FGBS'},
# "R","","LIFFE Long Gilt","LIFFE","1990-09-26","U1990","HMUZ","2","GBP100,000 nominal value notional Gilt with 4% coupon","0.01 (10)","Per GBP100 nominal","Delivery may be made of any gilts on the List of Deliverable Gilts in respect of a delivery month of an Exchange Contract, as published by the Exchange on or before the tenth business day prior to the First Notice Day of such delivery month. Holders of long positions on any day within the Notice Period may be delivered against during the delivery month. All gilt issues included in the List will have the following characteristics: having terms as to redemption such as provide for redemption of the entire gilt issue in a single instalment such that the length of time to the maturity date from, and excluding, the first date of the relevant delivery month is within the maturity range for the relevant Exchange Contract specified by the Board in the Contract Details; having no terms permitting or requiring early redemption; bearing interest at a single fixed rate throughout the term of the issue payable in arrears semi-annually (except in the case of the first interest payment period which may be more or less than six months); being denominated and payable as to the principal and interest only in Pounds and pence; being fully paid or, in the event that the gilt issue is in its first period and is partly paid, being anticipated by the Board to be fully paid on or before the Last Notice Day of the relevant delivery month; not being convertible; not being in bearer form; having been admitted to the Official List of the UK Listing Authority; and being anticipated by the Board to have on one or more days in the delivery month an aggregate principal amount outstanding of not less than 1.5 billion which, by its terms and conditions, if issued in more than one tranche or tap or issue, is fungible. UK Government bonds eligible for the list of deliverable Gilts in the Long Gilt futures contract must have a coupon within a 1% - 7% coupon range inclusive.",""
#{'margin': 0.0, 'mult': 0.0, 'name': 'LIFFE_R'},
]

STEVENS_MARGIN_RATIOS = {
'VX': 0.6095496105655266,
'AD': 0.017172688556120346,
'BO': 0.03496014543420501,
'BP': 0.018139218502002872,
'C': 0.0440771349862259,
'CD': 0.014929248344800727,
'CL': 0.04401285454799497,
'DA': 0.02480466327669602,
'EC': 0.015544479175466757,
'ED': 0.0016439763678397124,
'ES': 0.04121586810922205,
'FF': 0.0009812857979652112,
'FV': 0.00604738414507052,
'GC': 0.025913665696994014,
'HG': 0.04384724186704384,
'HO': 0.0393142274464623,
'JY': 0.01794526693584567,
'KW': 0.061420345489443376,
'LC': 0.032365252664739136,
'LN': 0.05605381165919283,
'MD': 0.008131290594476672,
'NE': 0.01799370220422852,
'NG': 0.045177698949200186,
'NK': 0.04348735103491533,
'NQ': 0.04051249958828761,
'PA': 0.06114194337315399,
'PL': 0.045949214026602174,
'S': 0.05529411764705883,
'SF': 0.019927189116689017,
'SI': 0.04999652801888758,
'SM': 0.05340151466114312,
'TU': 0.0021830045973602256,
'TY': 0.008843268851164626,
'US': 0.016366466533244386,
'W': 0.05990338164251208,
'YM': 0.05015329876225444,
'ATW': 0.5873140172278778,
'B': 0.03024219493990168,
'CC': 0.08833100883310088,
'CT': 0.06724181679776707,
'DX': 0.01919529075533469,
'G': 0.043615898698557864,
'KC': 0.05728900255754476,
'OJ': 0.04510599909788002,
'SB': 0.09531665927240461,

}


CURRENCIES = ['AD','BP','CD','DX','JY','MP','NE','SF','EC']
INDICIES = ['DJ','YM','NQ','NK','MD','SP','ES','RS1','RTY','FDAX','FESX',]
ENERGIES = ['RB','HO','NG','CL','B']
METALS = ['GC','SI','HG','PA','PL']
INTEREST_RATES = ['TY','TU','FF','US','FV',]
SOFTS = ['CC','KC','CY','SB','OJ','LB','DA']
LIVESTOCK = ['LN','LC',]
GRAINS = ['C','O','RR','SM','BO','S','KW',]
VOLATILITY = ['VX']

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
{'commission': 2.0, 'margin': 2750.0, 'mult': 110.0, 'name': 'LB'},
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
{'commission': 2.0, 'margin': 850.0, 'mult': 2000.0, 'name': 'DA'},
# SP-S&P500, DAY
# SI-SILVER
{'commission': 2.0, 'margin': 3600.0, 'mult': 5000.0, 'name': 'SI'},
# S_-SOYBEANS
{'commission': 2.0, 'margin': 3600.0, 'mult': 5000.0, 'name': 'ZS'},
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
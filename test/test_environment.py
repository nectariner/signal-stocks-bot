import sys
import unittest
sys.path.append("../src")
print(sys.path)
from main import Instrument

# NOTE THAT FOR ALL THINGS THAT SAID "NULL" IN THE REPONSE
# I REPLACED WITH a 1 TO REMOVE THIS ISSUE
EXAMPLE_API_RESULT_MSFT_LOW = {
	"zip": "98052-6399",
	"sector": "Technology",
	"fullTimeEmployees": 163000,
	"longBusinessSummary": "Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide. Its Productivity and Business Processes segment offers Office, Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance, and Skype for Business, as well as related Client Access Licenses (CAL); Skype, Outlook.com, OneDrive, and LinkedIn; and Dynamics 365, a set of cloud-based and on-premises business solutions for small and medium businesses, large organizations, and divisions of enterprises. Its Intelligent Cloud segment licenses SQL and Windows Servers, Visual Studio, System Center, and related CALs; GitHub that provides a collaboration platform and code hosting service for developers; and Azure, a cloud platform. It also offers support services and Microsoft consulting services to assist customers in developing, deploying, and managing Microsoft server and desktop solutions; and training and certification to developers and IT professionals on various Microsoft products. Its More Personal Computing segment provides Windows original equipment manufacturer (OEM) licensing and other non-volume licensing of the Windows operating system; Windows Commercial, such as volume licensing of the Windows operating system, Windows cloud services, and other Windows commercial offerings; patent licensing; Windows Internet of Things; and MSN advertising. It also offers Surface, PC accessories, PCs, tablets, gaming and entertainment consoles, and other devices; Gaming, including Xbox hardware, and Xbox content and services; video games and third-party video game royalties; and Search, including Bing and Microsoft advertising. It sells its products through OEMs, distributors, and resellers; and directly through digital marketplaces, online stores, and retail stores. It has a strategic collaboration with DXC Technology. The company was founded in 1975 and is headquartered in Redmond, Washington.",
	"city": "Redmond",
	"phone": "425-882-8080",
	"state": "WA",
	"country": "United States",
	"companyOfficers": [],
	"website": "http://www.microsoft.com",
	"maxAge": 1,
	"address1": "One Microsoft Way",
	"industry": "Software\u2014Infrastructure",
	"previousClose": 244.49,
	"regularMarketOpen": 243.9332,
	"twoHundredDayAverage": 216.58533,
	"trailingAnnualDividendYield": 0.008752914,
	"payoutRatio": 0.31149998,
	"volume24Hr": 1,
	"regularMarketDayHigh": 245.29,
	"navPrice": 1,
	"averageDailyVolume10Day": 21346962,
	"totalAssets": 1,
	"regularMarketPreviousClose": 244.49,
	"fiftyDayAverage": 228.35303,
	"trailingAnnualDividendRate": 2.14,
	"open": 243.9332,
	"toCurrency": 1,
	"averageVolume10days": 21346962,
	"expireDate": 1,
	"yield": 1,
	"algorithm": 1,
	"dividendRate": 2.24,
	"exDividendDate": 1613520000,
	"beta": 0.816969,
	"circulatingSupply": 1,
	"startDate": 1,
	"regularMarketDayLow": 242.74,
	"priceHint": 2,
	"currency": "USD",
	"trailingPE": 36.52751,
	"regularMarketVolume": 16561079,
	"lastMarket": 1,
	"maxSupply": 1,
	"openInterest": 1,
	"marketCap": 1847768514560,
	"volumeAllCurrencies": 1,
	"strikePrice": 1,
	"averageVolume": 28143637,
	"priceToSalesTrailing12Months": 12.054543,
	"dayLow": 242.74,
	"ask": 245.3,
	"ytdReturn": 1,
	"askSize": 800,
	"volume": 16561079,
	"fiftyTwoWeekHigh": 245.92,
	"forwardPE": 30.283066,
	"fromCurrency": 1,
	"fiveYearAvgDividendYield": 1.71,
	"fiftyTwoWeekLow": 132.52,
	"bid": 245.26,
	"tradeable": 1,
	"dividendYield": 0.0091,
	"bidSize": 1000,
	"dayHigh": 245.29,
	"exchange": "NMS",
	"shortName": "Microsoft Corporation",
	"longName": "Microsoft Corporation",
	"exchangeTimezoneName": "America/New_York",
	"exchangeTimezoneShortName": "EST",
	"isEsgPopulated": 1,
	"gmtOffSetMilliseconds": "-18000000",
	"quoteType": "EQUITY",
	"symbol": "MSFT",
	"messageBoardId": "finmb_21835",
	"market": "us_market",
	"annualHoldingsTurnover": 1,
	"enterpriseToRevenue": 11.734,
	"beta3Year": 1,
	"profitMargins": 0.33473998,
	"enterpriseToEbitda": 25.089,
	"52WeekChange": 0.30849767,
	"morningStarRiskRating": 1,
	"forwardEps": 8.09,
	"revenueQuarterlyGrowth": 1,
	"sharesOutstanding": 7560500224,
	"fundInceptionDate": 1,
	"annualReportExpenseRatio": 1,
	"bookValue": 17.259,
	"sharesShort": 44533174,
	"sharesPercentSharesOut": 0.0058999998,
	"fundFamily": 1,
	"lastFiscalYearEnd": 1593475200,
	"heldPercentInstitutions": 0.71844,
	"netIncomeToCommon": 51309998080,
	"trailingEps": 6.707,
	"lastDividendValue": 0.56,
	"SandP52WeekChange": 0.1675049,
	"priceToBook": 14.194913,
	"heldPercentInsiders": 0.00059,
	"nextFiscalYearEnd": 1656547200,
	"mostRecentQuarter": 1609372800,
	"shortRatio": 1.39,
	"sharesShortPreviousMonthDate": 1609372800,
	"floatShares": 7431722306,
	"enterpriseValue": 1798560415744,
	"threeYearAverageReturn": 1,
	"lastSplitDate": 1045526400,
	"lastSplitFactor": "2:1",
	"legalType": 1,
	"lastDividendDate": 1605657600,
	"morningStarOverallRating": 1,
	"earningsQuarterlyGrowth": 0.327,
	"dateShortInterest": 1611878400,
	"pegRatio": 1.82,
	"lastCapGain": 1,
	"shortPercentOfFloat": 0.0058999998,
	"sharesShortPriorMonth": 39201229,
	"impliedSharesOutstanding": 1,
	"category": 1,
	"fiveYearAverageReturn": 1,
	"regularMarketPrice": 243.9332,
	"logo_url": "https://logo.clearbit.com/microsoft.com"
}

EXAMPLE_API_RESULT_MSFT_HIGH = {
	"zip": "98052-6399",
	"sector": "Technology",
	"fullTimeEmployees": 163000,
	"longBusinessSummary": "Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide. Its Productivity and Business Processes segment offers Office, Exchange, SharePoint, Microsoft Teams, Office 365 Security and Compliance, and Skype for Business, as well as related Client Access Licenses (CAL); Skype, Outlook.com, OneDrive, and LinkedIn; and Dynamics 365, a set of cloud-based and on-premises business solutions for small and medium businesses, large organizations, and divisions of enterprises. Its Intelligent Cloud segment licenses SQL and Windows Servers, Visual Studio, System Center, and related CALs; GitHub that provides a collaboration platform and code hosting service for developers; and Azure, a cloud platform. It also offers support services and Microsoft consulting services to assist customers in developing, deploying, and managing Microsoft server and desktop solutions; and training and certification to developers and IT professionals on various Microsoft products. Its More Personal Computing segment provides Windows original equipment manufacturer (OEM) licensing and other non-volume licensing of the Windows operating system; Windows Commercial, such as volume licensing of the Windows operating system, Windows cloud services, and other Windows commercial offerings; patent licensing; Windows Internet of Things; and MSN advertising. It also offers Surface, PC accessories, PCs, tablets, gaming and entertainment consoles, and other devices; Gaming, including Xbox hardware, and Xbox content and services; video games and third-party video game royalties; and Search, including Bing and Microsoft advertising. It sells its products through OEMs, distributors, and resellers; and directly through digital marketplaces, online stores, and retail stores. It has a strategic collaboration with DXC Technology. The company was founded in 1975 and is headquartered in Redmond, Washington.",
	"city": "Redmond",
	"phone": "425-882-8080",
	"state": "WA",
	"country": "United States",
	"companyOfficers": [],
	"website": "http://www.microsoft.com",
	"maxAge": 1,
	"address1": "One Microsoft Way",
	"industry": "Software\u2014Infrastructure",
	"previousClose": 244.49,
	"regularMarketOpen": 243.9332,
	"twoHundredDayAverage": 216.58533,
	"trailingAnnualDividendYield": 0.008752914,
	"payoutRatio": 0.31149998,
	"volume24Hr": 1,
	"regularMarketDayHigh": 245.29,
	"navPrice": 1,
	"averageDailyVolume10Day": 21346962,
	"totalAssets": 1,
	"regularMarketPreviousClose": 244.49,
	"fiftyDayAverage": 228.35303,
	"trailingAnnualDividendRate": 2.14,
	"open": 243.9332,
	"toCurrency": 1,
	"averageVolume10days": 21346962,
	"expireDate": 1,
	"yield": 1,
	"algorithm": 1,
	"dividendRate": 2.24,
	"exDividendDate": 1613520000,
	"beta": 0.816969,
	"circulatingSupply": 1,
	"startDate": 1,
	"regularMarketDayLow": 242.74,
	"priceHint": 2,
	"currency": "USD",
	"trailingPE": 36.52751,
	"regularMarketVolume": 16561079,
	"lastMarket": 1,
	"maxSupply": 1,
	"openInterest": 1,
	"marketCap": 1847768514560,
	"volumeAllCurrencies": 1,
	"strikePrice": 1,
	"averageVolume": 28143637,
	"priceToSalesTrailing12Months": 12.054543,
	"dayLow": 242.74,
	"ask": 245.3,
	"ytdReturn": 1,
	"askSize": 800,
	"volume": 16561079,
	"fiftyTwoWeekHigh": 245.92,
	"forwardPE": 30.283066,
	"fromCurrency": 1,
	"fiveYearAvgDividendYield": 1.71,
	"fiftyTwoWeekLow": 132.52,
	"bid": 245.26,
	"tradeable": 1,
	"dividendYield": 0.0091,
	"bidSize": 1000,
	"dayHigh": 245.29,
	"exchange": "NMS",
	"shortName": "Microsoft Corporation",
	"longName": "Microsoft Corporation",
	"exchangeTimezoneName": "America/New_York",
	"exchangeTimezoneShortName": "EST",
	"isEsgPopulated": 1,
	"gmtOffSetMilliseconds": "-18000000",
	"quoteType": "EQUITY",
	"symbol": "MSFT",
	"messageBoardId": "finmb_21835",
	"market": "us_market",
	"annualHoldingsTurnover": 1,
	"enterpriseToRevenue": 11.734,
	"beta3Year": 1,
	"profitMargins": 0.33473998,
	"enterpriseToEbitda": 25.089,
	"52WeekChange": 0.30849767,
	"morningStarRiskRating": 1,
	"forwardEps": 8.09,
	"revenueQuarterlyGrowth": 1,
	"sharesOutstanding": 7560500224,
	"fundInceptionDate": 1,
	"annualReportExpenseRatio": 1,
	"bookValue": 17.259,
	"sharesShort": 44533174,
	"sharesPercentSharesOut": 0.0058999998,
	"fundFamily": 1,
	"lastFiscalYearEnd": 1593475200,
	"heldPercentInstitutions": 0.71844,
	"netIncomeToCommon": 51309998080,
	"trailingEps": 6.707,
	"lastDividendValue": 0.56,
	"SandP52WeekChange": 0.1675049,
	"priceToBook": 14.194913,
	"heldPercentInsiders": 0.00059,
	"nextFiscalYearEnd": 1656547200,
	"mostRecentQuarter": 1609372800,
	"shortRatio": 1.39,
	"sharesShortPreviousMonthDate": 1609372800,
	"floatShares": 7431722306,
	"enterpriseValue": 1798560415744,
	"threeYearAverageReturn": 1,
	"lastSplitDate": 1045526400,
	"lastSplitFactor": "2:1",
	"legalType": 1,
	"lastDividendDate": 1605657600,
	"morningStarOverallRating": 1,
	"earningsQuarterlyGrowth": 0.327,
	"dateShortInterest": 1611878400,
	"pegRatio": 1.82,
	"lastCapGain": 1,
	"shortPercentOfFloat": 0.0058999998,
	"sharesShortPriorMonth": 39201229,
	"impliedSharesOutstanding": 1,
	"category": 1,
	"fiveYearAverageReturn": 1,
	"regularMarketPrice": 300.0000,
	"logo_url": "https://logo.clearbit.com/microsoft.com"
}

EXAMPLE_API_RESULT_IBM_LOW = {
	"zip": "10504",
	"sector": "Technology",
	"longBusinessSummary": "International Business Machines Corporation provides integrated solutions and services worldwide. Its Cloud & Cognitive Software segment offers software for vertical and domain-specific solutions in health, financial services, and Internet of Things (IoT), weather, and security software and services application areas; and customer information control system and storage, and analytics and integration software solutions to support client mission critical on-premise workloads in banking, airline, and retail industries. It also offers middleware and data platform software, including Red Hat that enables the operation of clients' hybrid multi-cloud environments; and Cloud Paks, WebSphere distributed, and analytics platform software, such as DB2 distributed, information integration, and enterprise content management, as well as IoT, Blockchain and AI/Watson platforms. The company's Global Business Services segment offers business consulting services; system integration, application management, maintenance, and support services for packaged software; finance, procurement, talent and engagement, and industry-specific business process outsourcing services; and IT infrastructure and platform services. Its Global Technology Services segment provides project, managed, outsourcing, and cloud-delivered services for enterprise IT infrastructure environments; and IT infrastructure support services. The company's Systems segment offers servers for businesses, cloud service providers, and scientific computing organizations; data storage products and solutions; and z/OS, an enterprise operating system, as well as Linux. Its Global Financing segment provides lease, installment payment, loan financing, short-term working capital financing, and remanufacturing and remarketing services. The company was formerly known as Computing-Tabulating-Recording Co. The company was founded in 1911 and is headquartered in Armonk, New York.",
	"city": "Armonk",
	"phone": "914 499 1900",
	"state": "NY",
	"country": "United States",
	"companyOfficers": [],
	"website": "http://www.ibm.com",
	"maxAge": 1,
	"address1": "One New Orchard Road",
	"industry": "Information Technology Services",
	"previousClose": 120.91,
	"regularMarketOpen": 121,
	"twoHundredDayAverage": 122.43841,
	"trailingAnnualDividendYield": 0.0538417,
	"payoutRatio": 1.0619999,
	"volume24Hr": 1,
	"regularMarketDayHigh": 121.36,
	"navPrice": 1,
	"averageDailyVolume10Day": 4835728,
	"totalAssets": 1,
	"regularMarketPreviousClose": 120.91,
	"fiftyDayAverage": 124.28667,
	"trailingAnnualDividendRate": 6.51,
	"open": 121,
	"toCurrency": 1,
	"averageVolume10days": 4835728,
	"expireDate": 1,
	"yield": 1,
	"algorithm": 1,
	"dividendRate": 6.52,
	"exDividendDate": 1612828800,
	"beta": 1.248132,
	"circulatingSupply": 1,
	"startDate": 1,
	"regularMarketDayLow": 120.09,
	"priceHint": 2,
	"currency": "USD",
	"trailingPE": 19.393162,
	"regularMarketVolume": 3879636,
	"lastMarket": 1,
	"maxSupply": 1,
	"openInterest": 1,
	"marketCap": 107639693312,
	"volumeAllCurrencies": 1,
	"strikePrice": 1,
	"averageVolume": 6234309,
	"priceToSalesTrailing12Months": 1.4620986,
	"dayLow": 120.09,
	"ask": 120.91,
	"ytdReturn": 1,
	"askSize": 800,
	"volume": 3879636,
	"fiftyTwoWeekHigh": 151.89,
	"forwardPE": 10,
	"fromCurrency": 1,
	"fiveYearAvgDividendYield": 4.31,
	"fiftyTwoWeekLow": 90.56,
	"bid": 120.9,
	"tradeable": 1,
	"dividendYield": 0.054,
	"bidSize": 1000,
	"dayHigh": 121.36,
	"exchange": "NYQ",
	"shortName": "International Business Machines",
	"longName": "International Business Machines Corporation",
	"exchangeTimezoneName": "America/New_York",
	"exchangeTimezoneShortName": "EST",
	"isEsgPopulated": 1,
	"gmtOffSetMilliseconds": "-18000000",
	"quoteType": "EQUITY",
	"symbol": "IBM",
	"messageBoardId": "finmb_112350",
	"market": "us_market",
	"annualHoldingsTurnover": 1,
	"enterpriseToRevenue": 2.182,
	"beta3Year": 1,
	"profitMargins": 0.07593,
	"enterpriseToEbitda": 11.889,
	"52WeekChange": -0.20052946,
	"morningStarRiskRating": 1,
	"forwardEps": 12.08,
	"revenueQuarterlyGrowth": 1,
	"sharesOutstanding": 891057024,
	"fundInceptionDate": 1,
	"annualReportExpenseRatio": 1,
	"bookValue": 23.075,
	"sharesShort": 26828008,
	"sharesPercentSharesOut": 0.0301,
	"fundFamily": 1,
	"lastFiscalYearEnd": 1609372800,
	"heldPercentInstitutions": 0.58584,
	"netIncomeToCommon": 5501000192,
	"trailingEps": 6.229,
	"lastDividendValue": 1.63,
	"SandP52WeekChange": 0.1675049,
	"priceToBook": 5.2351027,
	"heldPercentInsiders": 0.0012800001,
	"nextFiscalYearEnd": 1672444800,
	"mostRecentQuarter": 1609372800,
	"shortRatio": 3.16,
	"sharesShortPreviousMonthDate": 1609372800,
	"floatShares": 891011172,
	"enterpriseValue": 160612073472,
	"threeYearAverageReturn": 1,
	"lastSplitDate": 927763200,
	"lastSplitFactor": "2:1",
	"legalType": 1,
	"lastDividendDate": 1612828800,
	"morningStarOverallRating": 1,
	"earningsQuarterlyGrowth": -0.631,
	"dateShortInterest": 1611878400,
	"pegRatio": 1.92,
	"lastCapGain": 1,
	"shortPercentOfFloat": 0.0301,
	"sharesShortPriorMonth": 24592416,
	"impliedSharesOutstanding": 1,
	"category": 1,
	"fiveYearAverageReturn": 1,
	"regularMarketPrice": 121,
	"logo_url": "https://logo.clearbit.com/ibm.com"
}

EXAMPLE_API_RESULT_IBM_HIGH = {
	"zip": "10504",
	"sector": "Technology",
	"longBusinessSummary": "International Business Machines Corporation provides integrated solutions and services worldwide. Its Cloud & Cognitive Software segment offers software for vertical and domain-specific solutions in health, financial services, and Internet of Things (IoT), weather, and security software and services application areas; and customer information control system and storage, and analytics and integration software solutions to support client mission critical on-premise workloads in banking, airline, and retail industries. It also offers middleware and data platform software, including Red Hat that enables the operation of clients' hybrid multi-cloud environments; and Cloud Paks, WebSphere distributed, and analytics platform software, such as DB2 distributed, information integration, and enterprise content management, as well as IoT, Blockchain and AI/Watson platforms. The company's Global Business Services segment offers business consulting services; system integration, application management, maintenance, and support services for packaged software; finance, procurement, talent and engagement, and industry-specific business process outsourcing services; and IT infrastructure and platform services. Its Global Technology Services segment provides project, managed, outsourcing, and cloud-delivered services for enterprise IT infrastructure environments; and IT infrastructure support services. The company's Systems segment offers servers for businesses, cloud service providers, and scientific computing organizations; data storage products and solutions; and z/OS, an enterprise operating system, as well as Linux. Its Global Financing segment provides lease, installment payment, loan financing, short-term working capital financing, and remanufacturing and remarketing services. The company was formerly known as Computing-Tabulating-Recording Co. The company was founded in 1911 and is headquartered in Armonk, New York.",
	"city": "Armonk",
	"phone": "914 499 1900",
	"state": "NY",
	"country": "United States",
	"companyOfficers": [],
	"website": "http://www.ibm.com",
	"maxAge": 1,
	"address1": "One New Orchard Road",
	"industry": "Information Technology Services",
	"previousClose": 120.91,
	"regularMarketOpen": 121,
	"twoHundredDayAverage": 122.43841,
	"trailingAnnualDividendYield": 0.0538417,
	"payoutRatio": 1.0619999,
	"volume24Hr": 1,
	"regularMarketDayHigh": 121.36,
	"navPrice": 1,
	"averageDailyVolume10Day": 4835728,
	"totalAssets": 1,
	"regularMarketPreviousClose": 120.91,
	"fiftyDayAverage": 124.28667,
	"trailingAnnualDividendRate": 6.51,
	"open": 121,
	"toCurrency": 1,
	"averageVolume10days": 4835728,
	"expireDate": 1,
	"yield": 1,
	"algorithm": 1,
	"dividendRate": 6.52,
	"exDividendDate": 1612828800,
	"beta": 1.248132,
	"circulatingSupply": 1,
	"startDate": 1,
	"regularMarketDayLow": 120.09,
	"priceHint": 2,
	"currency": "USD",
	"trailingPE": 19.393162,
	"regularMarketVolume": 3879636,
	"lastMarket": 1,
	"maxSupply": 1,
	"openInterest": 1,
	"marketCap": 107639693312,
	"volumeAllCurrencies": 1,
	"strikePrice": 1,
	"averageVolume": 6234309,
	"priceToSalesTrailing12Months": 1.4620986,
	"dayLow": 120.09,
	"ask": 120.91,
	"ytdReturn": 1,
	"askSize": 800,
	"volume": 3879636,
	"fiftyTwoWeekHigh": 151.89,
	"forwardPE": 10,
	"fromCurrency": 1,
	"fiveYearAvgDividendYield": 4.31,
	"fiftyTwoWeekLow": 90.56,
	"bid": 120.9,
	"tradeable": 1,
	"dividendYield": 0.054,
	"bidSize": 1000,
	"dayHigh": 121.36,
	"exchange": "NYQ",
	"shortName": "International Business Machines",
	"longName": "International Business Machines Corporation",
	"exchangeTimezoneName": "America/New_York",
	"exchangeTimezoneShortName": "EST",
	"isEsgPopulated": 1,
	"gmtOffSetMilliseconds": "-18000000",
	"quoteType": "EQUITY",
	"symbol": "IBM",
	"messageBoardId": "finmb_112350",
	"market": "us_market",
	"annualHoldingsTurnover": 1,
	"enterpriseToRevenue": 2.182,
	"beta3Year": 1,
	"profitMargins": 0.07593,
	"enterpriseToEbitda": 11.889,
	"52WeekChange": -0.20052946,
	"morningStarRiskRating": 1,
	"forwardEps": 12.08,
	"revenueQuarterlyGrowth": 1,
	"sharesOutstanding": 891057024,
	"fundInceptionDate": 1,
	"annualReportExpenseRatio": 1,
	"bookValue": 23.075,
	"sharesShort": 26828008,
	"sharesPercentSharesOut": 0.0301,
	"fundFamily": 1,
	"lastFiscalYearEnd": 1609372800,
	"heldPercentInstitutions": 0.58584,
	"netIncomeToCommon": 5501000192,
	"trailingEps": 6.229,
	"lastDividendValue": 1.63,
	"SandP52WeekChange": 0.1675049,
	"priceToBook": 5.2351027,
	"heldPercentInsiders": 0.0012800001,
	"nextFiscalYearEnd": 1672444800,
	"mostRecentQuarter": 1609372800,
	"shortRatio": 3.16,
	"sharesShortPreviousMonthDate": 1609372800,
	"floatShares": 891011172,
	"enterpriseValue": 160612073472,
	"threeYearAverageReturn": 1,
	"lastSplitDate": 927763200,
	"lastSplitFactor": "2:1",
	"legalType": 1,
	"lastDividendDate": 1612828800,
	"morningStarOverallRating": 1,
	"earningsQuarterlyGrowth": -0.631,
	"dateShortInterest": 1611878400,
	"pegRatio": 1.92,
	"lastCapGain": 1,
	"shortPercentOfFloat": 0.0301,
	"sharesShortPriorMonth": 24592416,
	"impliedSharesOutstanding": 1,
	"category": 1,
	"fiveYearAverageReturn": 1,
	"regularMarketPrice": 130,
	"logo_url": "https://logo.clearbit.com/ibm.com"
}

if __name__ == "__main__":
	print("testing")
	x = Instrument("IBM")
	x.say_hello()
	

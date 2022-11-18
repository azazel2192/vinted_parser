# vinted_parser
Parser for vinted.cz  
It parses items by filters, I've only added filters for seller's values, but maybe I'll add other filters later. I made it to find items which are sold by sellers with no reputation and few items sold, but added some filters for reputation and countries.  
  
It grabs information via vinted.cz/api/v2/
  
Drobpox is used for storing cookies and list of sellers that were parsed before. You need to put your dropbox app token at the start of dbx.py file.
Also you need an account at vinted.cz to parse, '_vinted_fr_session' is the cookie that we need. Grab it and put it in the 'Vinted/cookie.txt' in the root directory 
of your dropbox. You need to put only the value of cookie, without quotes or anything. After that you're good to go.  



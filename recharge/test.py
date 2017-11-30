import re

with open('526087187883.html', 'r') as f:
  for line in f:
    #line_match = re.match(r'<strong id=\"J_StrPrice"><em class=\"tb-rmb\">\&yen\;</em><em class=\"tb-rmb-num\">(.*)</em></strong>', line)
    line_match = re.match(r'<strong id="J_StrPrice">.*tb-rmb-num">(.*)</em></strong>', line)
    if line_match:
      print(line_match.group(1))

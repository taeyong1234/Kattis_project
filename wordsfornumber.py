

import sys
import re

dic1 = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
dic12 = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
dic2 = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
dic22 = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
dic3 = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
dic32 = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
           17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
for line in sys.stdin:

    content = line.split()
    for i in range(len(content)):
        regex = r'^[+-]{0,1}((\d*\.)|\d*)\d+$'
        #https://www.guru99.com/python-regular-expressions-complete-tutorial.html
        if re.match(regex, content[i]):

            decimal = int(content[i])
            if decimal >= 10 and decimal < 20:
                if i == 0:
                    content[i] = dic32[decimal]
                else:
                    content[i] = dic3[decimal]

            elif decimal < 10:
                if i == 0:
                    content[i] = dic12[decimal]
                else:
                    content[i] = dic1[decimal]
            else:
                if dic1[decimal % 10] == 'zero':
                    if i == 0:
                        content[i] = dic22[decimal // 10]
                    else:
                        content[i] = dic2[decimal // 10]
                else:
                    if i == 0:
                        content[i] = dic22[decimal // 10] + '-' + dic1[decimal % 10]
                    else:
                        content[i] = dic2[decimal // 10] + '-' + dic1[decimal % 10]

    print(" ".join(content))








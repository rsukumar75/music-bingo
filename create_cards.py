import random
import csv
import math

numbersheets = 300
gridsize = 5
stepping = 16
save_path = './cards.html'
input_file = './input.csv'
center_figure = '<img src="https://raw.githubusercontent.com/florisdenhengst/music-bingo/master/center-img-small.png"/>'

input_words = []
input_ids = []
with open(input_file, 'r') as f:
    r = csv.reader(f, delimiter=',', quotechar='"')
    _ = next(r)
    for row in r:
        input_words.append(row[0])
        input_ids.append(row[1])

print('Creating bingo cards for: ' + str(len(input_words)) + ' words')
n_words = len(input_words)
words = []
for i, w in enumerate(input_words):
    words.append('{}: {}'.format(input_ids[i], w))

sheets = set()

with open(save_path, 'w') as f:
    f.write("<html>")
    f.write("""
    <head>
        <style>
            td {
		width: 120px;
		height: 50px;
		padding: 2px;
                overflow: hidden;
		text-align: center;
		vertical-align: middle;
		border: 1px solid black;
                font-size: 9pt;
                font-family: Arial, Helvetica, sans-serif;
            }
            img {
                max-height: 50px;
            }
            @media print{
                br.page{
                    page-break-before: always;
                }
            }
        </style>
    </head>
    <body>
    """)

    for i in range(numbersheets):
        f.write('\n')

        bingosheet = []
        duplicate = True
        while duplicate:
            sheet = random.sample(words, gridsize**2 - 1)
            o_sheet = '~'.join(sheet)
            duplicate = o_sheet in sheets
            if duplicate:
                print('Duplicate, retrying')
        sheets.add(o_sheet)

        sheet.insert(math.ceil(len(sheet)/2), center_figure)

        f.write("<table>")
        f.write("<tr>")
        bingo = ["<th>{}</th>".format(l) for l in list('BINGO')]
        for th in bingo:
            f.write(th)
        f.write("</tr>")

        for r in range(gridsize):
            f.write("<tr>")
            for c in range(gridsize):
                cell = r * gridsize + c
                cell = sheet[cell]
                columnstring = '<td>' + cell + "</td>"
                f.write(columnstring)
            f.write("</tr>\n")
        f.write("</table>")
        if (i+1) % 2 == 0:
            f.write("<br class='page'/>")
        else:
            f.write("<br/>")
        f.write("\n")

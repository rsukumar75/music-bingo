import random
import csv
import math

numbersheets = 20
gridsize = 5
stepping = 16
save_path = './cards.html'
input_file = './input.csv'
center_figure = '*'

input_words = []
with open(input_file, 'r') as f:
    r = csv.reader(f, delimiter=',', quotechar='"')
    for row in r:
        input_words.append(row[0])

print('Creating bingo cards for: ' + str(len(input_words)) + ' words')
n_words = len(input_words)
words = []
for i, w in enumerate(input_words):
    words.append('{}: {}'.format(i, w))

with open(save_path, 'w') as f:
    f.write("<html>")
    f.write("""
    <head>
        <style>
            td {
		width: 120px;
		height: 50px;
		padding: 10px;
		text-align: center;
		vertical-align: middle;
		border: 1px solid black;
                font-size: 10pt;
                font-family: Arial, Helvetica, sans-serif;
            }
        </style>
    </head>
    <body>
    """)

    for i in range(numbersheets):
        f.write('\n')

        bingosheet = []
        sheet = random.sample(words, gridsize**2 - 1)
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
        f.write("\n")

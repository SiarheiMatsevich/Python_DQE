a = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each 
	existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

out = a.lower().capitalize().replace(' iz ', ' is ')
a_list = list(out)
space_count = 0
last_words = []
for n, i in enumerate(a_list):
    if i in [' ', '\n', '\t']:
        space_count += 1
    if (a_list[n - 2] == '.' or a_list[n - 2] == '\n') and i != a_list[1]:
        a_list[n] = i.upper()

last_words = ' ' + (' '.join([i[:-1] for i in list(out.split()) if '.' in i]) + '.').capitalize()
out = ''.join(a_list)
delimiter = 'paragraph.'
position = out.find(delimiter) + len(delimiter)
out = [out[:position], last_words, out[position:]]
out = ''.join(out)

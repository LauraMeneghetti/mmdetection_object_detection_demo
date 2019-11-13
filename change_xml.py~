from __future__ import print_function
from sys import argv
from os import listdir, path
import re


WIDTH_NEW = 800
HEIGHT_NEW = 600

DIMLINE_MASK = r'<(?P<type1>width|height)>(?P<size>\d+)</(?P<type2>width|height)>'
BBLINE_MASK = r'<(?P<type1>xmin|xmax|ymin|ymax)>(?P<size>\d+)</(?P<type2>xmin|xmax|ymin|ymax)>'
NAMELINE_MASK = r'<(?P<type1>filename)>(?P<size>\S+)</(?P<type2>filename)>'
PATHLINE_MASK = r'<(?P<type1>path)>(?P<size>.+)</(?P<type2>path)>'
#regular expression

def resize_file(file_lines):
    #change file_lines[8] and file_lines[9] where there is the current width and height
    #riga_w = file_lines[8][9:12]
    #width_old = int(riga_w)
    #print(width_old)

    #riga_h = file_lines[9][10:13]
    #height_old = int(riga_h)

    new_lines = []
    for line in file_lines:
        match = re.search(DIMLINE_MASK, line) or re.search(BBLINE_MASK, line) or  re.search(NAMELINE_MASK, line) or re.search(PATHLINE_MASK, line) 
        if match is not None:
            size = match.group('size')
            type1 = match.group('type1')
            type2 = match.group('type2')
            print(size)     
            if type1 != type2:
                raise ValueError('Malformed line: {}'.format(line))
          
            if type1.startswith('f'):
                new_name = size[:-3] + 'jpg'
                #print(new_size)
                new_line = '\t<{}>{}</{}>\n'.format(type1, new_name, type1)
            elif type1.startswith('p'):
                new_size = '/u/l/lmeneghe/Laura/mmdetection_object_detection_demo/data/VOC2007/Annotations/' + new_name
                #print(new_size)
       	       	new_line = '\t<{}>{}</{}>\n'.format(type1, new_size, type1)
            elif type1.startswith('x'):
                size = int(size)
                new_size = int(round(size * WIDTH_NEW / width_old))
                #print(new_size)
                new_line = '\t\t\t<{}>{}</{}>\n'.format(type1, new_size, type1)
            elif type1.startswith('y'):
                size = int(size)
                new_size = int(round(size * HEIGHT_NEW / height_old))
                new_line = '\t\t\t<{}>{}</{}>\n'.format(type1, new_size, type1)
            elif type1.startswith('w'):
                 size = int(size)
            	 width_old = size
            	 new_size = int(WIDTH_NEW)
            	 new_line = '\t\t<{}>{}</{}>\n'.format(type1, new_size, type1)
            elif type1.startswith('h'):
                 size = int(size)
            	 height_old = size
            	 new_size = int(HEIGHT_NEW)
            	 new_line = '\t\t<{}>{}</{}>\n'.format(type1, new_size, type1)
            else:
            	raise ValueError('Unknown type: {}'.format(type1))
            #new_line = '\t\t\t<{}>{}</{}>\n'.format(type1, new_size, type1)
            new_lines.append(new_line)
        #elif match1 is not None:
        #	   name = match.group('name')
        #	   type1 = match.group('type1')
        #	   type2 = match.group('type2')
	#	   print(name)
        #	   if type1 != type2:
        #	   	raise ValueError('Malformed line: {}'.format(line))
        #	   
 	#           if type1.startswith('f'):
        #	   	 if name[-3:end] == 'png':
        #                    print(name[-3:])      	   		
        else:
            new_lines.append(line)

    return ''.join(new_lines)

if len(argv) < 2:
    raise ValueError('No file submitted')

nome_file = argv[1]

if path.isdir(nome_file):
    # Il primo argomento e` una directory
    # Implementero` qui qualcosa di astuto per
    # gestire questa situazione
    files = listdir(nome_file)
    for file in files:
        file_path = path.join(nome_file, file)
        file_name, file_ext = path.splitext(file)
        #print(file_path, end='') # Questo non e` tanto astuto
        if file_ext.lower() == '.xml':
            #print(': CONVERTIMIIII!!!', end='')
            with open(file_path,'r') as f:
        		    righe = f.readlines()

            nuovo_file = resize_file(righe)
            print(nuovo_file)
            with open(file_path,'w') as f:
                f.write(nuovo_file)
        #print()
        
else:
    # Il primo argomento e` un file (spero!)
    # Lo convertiro` come merita!

    with open(nome_file,'r') as f:
        righe = f.readlines()

    nuovo_file = resize_file(righe)
    print(nuovo_file)
    with open(nome_file,'w') as f:
        f.write(nuovo_file)


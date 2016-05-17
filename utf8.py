import wordpreprocessing as wp
import sys

if len(sys.argv) < 2:
  print('an argument is needed')
  quit()

file = sys.argv[1]
outfile = file + '_utf8'
encoding = wp.getEncoding(file)
print('imput file encoding is {}'.format(encoding))
with open(file,encoding=encoding) as f:
  buf = f.read()
  with open(outfile,'w') as out:
    out.write(buf)
    print('enoded to utf8 and saved as {}'.format(outfile))

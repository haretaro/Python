progma = '''progma = \'\'\'@@\'\'\'
progma = progma.replace('@@',progma.replace(\'\\\\\',\'\\\\\\\\\').replace(\'\\\'\',\'\\\\\\\'\'),1)
print(progma)'''
progma = progma.replace('@@',progma.replace('\\','\\\\').replace('\'','\\\''),1)
print(progma)

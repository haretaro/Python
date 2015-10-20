pragma = '''pragma = \'\'\'@@\'\'\'
pragma = pragma.replace(\'@@\',pragma.replace(\'\\\\\',\'\\\\\\\\\').replace(\'\\\'\',\'\\\\\\\'\'),1)
print(pragma)'''
pragma = pragma.replace('@@',pragma.replace('\\','\\\\').replace('\'','\\\''),1)
print(pragma)

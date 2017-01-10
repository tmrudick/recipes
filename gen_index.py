import os

for category, _, recipes in os.walk('.'):
  if category.find('.git') >= 0:
    continue

  category = category[2:]
  print '##', category.title(), '##'

  for recipe in recipes:
    if recipe == __file__:
      continue

    path = os.path.join(category, recipe)
    title = ' '.join([x.title() for x in recipe[0:-3].split('_')])

    print '*', '[' + title + '](' + path + ')'

  print

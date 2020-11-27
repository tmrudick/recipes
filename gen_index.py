import os

for category, _, recipes in os.walk('.'):
  if category.find('.git') >= 0 or category == '.':
    continue

  category = category[2:]
  print('## {} ##'.format(category.title()))

  output = []
  for recipe in recipes:
    if recipe == __file__:
      continue

    path = os.path.join(category, recipe)
    title = ' '.join([x.title() for x in recipe[0:-3].split('_')])

    output.append('* [{title}]({path})'.format(title=title, path=path))

  output.sort()
  print('\n'.join(output))
  print('')


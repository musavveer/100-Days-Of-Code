#import library
from googletrans import Translator

# Enter the text you want to translate
text = '''  No es sueño la vida. ¡Alerta! ¡Alerta! ¡Alerta! 
Nos caemos por las escaleras para comer la tierra húmeda 
o subimos al filo de la nieve con el coro de las dalias muertas. 
Pero no hay olvido, ni sueño: 
carne viva. Los besos atan las bocas 
en una maraña de venas recientes 
y al que le duele su dolor le dolerá sin descanso 
y al que teme la muerte la llevará sobre sus hombros. '''

# Create an instance of Translator to use
translator = Translator()

# Detect the language of text
lang = translator.detect(text)
print(lang)
print(' ')

# Call the translate() and specify your destination language
translated = translator.translate(text, dest = 'en')

# Print the result
print(translated.text)

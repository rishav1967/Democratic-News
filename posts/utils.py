import string 
import random
from django.utils.text import slugify 

def random_string_generator(size=10 ,char=string.ascii_lowercase + string.digits):
    a=[]
    for i in range(0,size):
        a.append(random.choice(char))

    return ''.join(a)

def unique_slug_generator(instance,new_slug=None):
    if new_slug is not None:
        slug=new_slug
    else:
        slug=slugify(instance.title)
    qs=instance.__class__
    qs__exists=qs.objects.filter(slug=slug).exists()
    if qs__exists:
        
        new_slug = '{slug}-{char}'.format(slug=slug,char=random_string_generator(size=6))

        return unique_slug_generator(instance,new_slug=new_slug)
    else:
        print('NO')
    return slug
from art.models import *
from django.contrib.auth.models import User

def run():
    iuart = User.objects.get(username="IUArtMuseum")

    hl = Collection(name="Highlight", 
               caption="The best of our gallery.",
               description=u"""This collection features some of the best art from the
               Indiana University Art Museum. These pieces are on display every day
               unless they are borrowed for collections at other institutions.""",
               featured=True,
               user=iuart)

    item = Item(name="The Studio",
                caption=u"""June 1934. One of the first major paintings acquired by
                Henry Radford Hope in 1944 from the New York gallery of Paul
                Rosenberg""",
                description=u'''Along with Georges Braque's Napkin Ring, Pablo
                Picasso's Studio was one of the first major paintings acquired
                by Henry Radford Hope, former chair of Indiana University's fine
                arts department and first director of the Indiana University Art
                Museum. In the summer of 1944, Hope and his new wife Sarahanne
                purchased both paintings from the New York gallery of Paul
                Rosenberg, a French dealer who had come to the United States
                during the war. Rosenberg had acquired The Studio from Picasso
                exactly ten years earlier, after its completion
                during the summer of 1934. Decades later, Hope remembered being
                immediately attracted to the painting when he saw it in
                Rosenberg's
                gallery.  The Indiana University Art Museum collection of work by
                Picasso encompasses numerous graphic works as well as two oil
                paintings, and is particularly strong in work from the 1930s.
                During the 1930s Picasso's range of motifs and subjects reflected
                his interests in Spanish culture (especially the bullfight), and in
                classical mythology (especially the figure of the Minotaur), as well
                as his often turbulent relationships with women. The Studio explores
                the artist's creative process and the role played by the female
                model in this process. 
                ''',
                featured=True,
                collection=hl,
                image="69.55.jpg")

    hl.save()
    item.save()



from art.models import *
from django.contrib.auth.models import User
from registration.models import ActivationProfile

def run():
    try:
        iuart = User.objects.get(username="IUArtMuseum")
    except:
        iuart = ActivationProfile.create_inactive_user(
            username="IUArtMuseum",
            email="iuart@gmail.com",
            password="iuart",
            street1="1137 E 7th St",
            street2="",
            city="Bloomington",
            state="IN",
            zipCode="47404",
            send_email=False
        )
        iuart.is_active = True

    try:
        hl = Collection.objects.get(name="Highlight")
    except:
        hl = Collection(name="Highlight", 
                   caption="The best of our gallery.",
                   description=u"""This collection features some of the best art from the
                   Indiana University Art Museum. These pieces are on display every day
                   unless they are borrowed for collections at other institutions.""",
                   featured=True,
                   user=iuart)
    try:
        studio = Item.objects.get(name="The Studio")
    except:
        studio = Item(name="The Studio",
                    user=iuart,
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
                    image="69.55.jpg")
        hl.items.append(studio)
        studio.save()


    try:
        servant = Item.objects.get(name="Servant Figure")
    except:
        servant = Item(name="Servant Figure",
                    user=iuart,
                    caption=u"""Old Kingdom, Dynasty 5, 2565-2420 BC. This statuette of a youthful servant is rare for several reasons: it departs from the frontal treatment characteristic of Egyptian sculpture; its execution is extraordinary delicate and refined; the state of preservation of its painted colors is exceptional; and the vivid expressiveness of the figure's face is remarkable, as well.""",
                    description=u'''Despite the fact that the man's arms and lower legs are lost, he clearly is shown in movement. His body leans forward and his knees are slightly bent, with the left one positioned forward. His arms would have reached forth, carrying most of the body's momentum. His stance indicates engagement in an activity, probably as a beer maker, bending over to strain mash with his hands through a sieve into a waist-high vat. 

    While the figure is generic, the sculptor rendered the face with unusual sensitivity. We notice the wide cheeks and full lips, rimmed with a ridge, and the extended cosmetic line at the eyes' outer corner (an innovation of the Old Kingdom artistic canon). The eyes look ahead, into the distance, with a gaze that was supposed to go beyond this mortal world. Such a gaze was usual in sculptures of this genre, but this figure's eyes glimmer with an alertness that, together with the hint of a smile on the lips, subtly distinguishes his countenance from the run-of-mill type. The general conventions observed in our statuette became established in the art of the Fifth Dynasty of ancient Egypt; but, in this case, we may also speak of an individual sculptor's remarkable artistry. For, of all known servant figures of the period, this one is certainly among the finest.''',
                    featured=True,
                    image="77.77.jpg")

        hl.items.append(servant)
        servant.save()

    hl.save()



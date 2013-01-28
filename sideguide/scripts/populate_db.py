from common.models import *
from django.contrib.auth.models import User
from registration.models import ActivationProfile

def run():
    iuart = ActivationProfile.create_inactive_user(
        username="IUArtMuseumCurator",
        password="iuart",
        email="iuart@gmail.com",
        send_email=False
    )
    iuart.is_active = True
    iuart.save()

    org = Organization(name="IU Art Museum")
    org.save()
    org.owners.add(iuart)

    hl = Collection(name="Highlight", 
               caption="The best of our gallery.",
               description=u"""This destinations features some of the best art from the
               Indiana University Art Museum. These pieces are on display every day
               unless they are borrowed for destinationss at other institutions.""",
               featured=True,
               created_by=iuart,
               org=org,
               poly="POLYGON((0 0, 1 0, 1 1, 0 1, 0 0))",
               image="69.55.jpg")
        
    hl.save()


    studio = Stop(name="The Studio",
                created_by=iuart,
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
                gallery.  The Indiana University Art Museum destinations of work by
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
                point="POINT(-23,54)",
                collection=hl,
                image="69.55.jpg")
    studio.save()


    servant = Stop(name="Servant Figure",
               created_by=iuart,
                caption=u"""Old Kingdom, Dynasty 5, 2565-2420 BC. This statuette of a youthful servant is rare for several reasons: it departs from the frontal treatment characteristic of Egyptian sculpture; its execution is extraordinary delicate and refined; the state of preservation of its painted colors is exceptional; and the vivid expressiveness of the figure's face is remarkable, as well.""",
                description=u'''Despite the fact that the man's arms and lower legs are lost, he clearly is shown in movement. His body leans forward and his knees are slightly bent, with the left one positioned forward. His arms would have reached forth, carrying most of the body's momentum. His stance indicates engagement in an activity, probably as a beer maker, bending over to strain mash with his hands through a sieve into a waist-high vat. 

While the figure is generic, the sculptor rendered the face with unusual sensitivity. We notice the wide cheeks and full lips, rimmed with a ridge, and the extended cosmetic line at the eyes' outer corner (an innovation of the Old Kingdom artistic canon). The eyes look ahead, into the distance, with a gaze that was supposed to go beyond this mortal world. Such a gaze was usual in sculptures of this genre, but this figure's eyes glimmer with an alertness that, together with the hint of a smile on the lips, subtly distinguishes his countenance from the run-of-mill type. The general conventions observed in our statuette became established in the art of the Fifth Dynasty of ancient Egypt; but, in this case, we may also speak of an individual sculptor's remarkable artistry. For, of all known servant figures of the period, this one is certainly among the finest.''',
                featured=True,
                point="POINT(0,1)",
                collection=hl,
                image="77.77.jpg")

    servant.save()

    stops = Stop(name="Cup",
                created_by=iuart,
                caption=u"""This is surely one of the most masterful of the
                elaborately carved cups made by the Kuba, a name referring
                to a number of different but related groups living between
                the Kasai and Sankuru river""",
                description=u'''This is surely one of the most masterful of
                the elaborately carved cups made by the Kuba, a name
                referring to a number of different but related groups living
                between the Kasai and Sankuru rivers, who traditionally
                acknowledge the leadership of the same king. Combining
                complex and intriguing imagery with a sure sense of form and
                proportion, the carver displays facility in creating the
                surface texture and patterning for which Kuba art is known:
                cross-hatching and raised and incised motifs contrast
                beautifully with smooth and broadly grooved surfaces.
                 
                These cups were traditionally used for drinking palm wine, a
                mildly intoxicating beverage fermented from the sap of the
                raffia palm tree, which the Kuba flavor with roots during
                fermentation. Imbibed by both men and women, palm wine
                traditionally plays an important role in Kuba social and
                ritual life, and Kuba folklore accounts for its origin.
                According to one version, a palm-wine lake was originally
                available from which all could draw their fill. One day,
                however, a woman polluted it and was then denounced by a
                fellow villager. The next day, the lake had disappeared, and
                in its place were growing four trees. A pygmy, one of the
                original inhabitants of the land in which the Kuba settled,
                discovered that one of the trees could be tapped for palm
                wine. He shared his knowledge only after becoming so
                publicly drunk that he was questioned by the village leader,
                who then decreed that palm wine should never be consumed in
                solitude, but instead should be enjoyed by people in groups.
                ''',
                featured=True,
                point="POINT(1,1)",
                collection=hl,
                image="77.34.2.jpg")

    stops.save()

    sp = Collection(name="South Pacific", 
               caption="From the South Pacific",
               description=u"""This destinations contains stopss 
               attributed to artists in the south pacific""",
               featured=False,
               created_by=iuart,
               poly="POLYGON((0 1,3 4,5 2, 1 1))",
               org=org,
               image="81.32.4.jpg")

    sp.save()



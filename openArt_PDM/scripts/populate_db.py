from browse.models import *
from django.contrib.auth.models import User

iuart = User.objects.get(name="IUArtMuseum")

hl = Collection(name="Highlight", 
           caption="The best of our gallery.",
           description="""This collection features some of the best art from the
           Indiana University Art Museum. These pieces are on display every day
           unless they are borrowed for collections at other institutions.""",
           featured=True,
           user=iuart)

item = Item(name="Studio",
            caption="Spanish, active in France, 1881–1973. The Studio, June 1934",
            description="""
            Along with Georges Braque’s Napkin Ring, Pablo Picasso’s Studio was
            one of the first major paintings acquired by Henry Radford Hope,
            former chair of Indiana University’s fine arts department and first
            director of the Indiana University Art Museum. In the summer of
            1944, Hope and his new wife Sarahanne purchased both paintings from
            the New York gallery of Paul Rosenberg, a French dealer who had come
            to the United States during the war. Rosenberg had acquired The
            Studio from Picasso exactly ten years earlier, after its completion
            during the summer of 1934. Decades later, Hope remembered being
            immediately attracted to the painting when he saw it in Rosenberg’s
            gallery.  The Indiana University Art Museum collection of work by
            Picasso encompasses numerous graphic works as well as two oil
            paintings, and is particularly strong in work from the 1930s.
            During the 1930s Picasso’s range of motifs and subjects reflected
            his interests in Spanish culture (especially the bullfight), and in
            classical mythology (especially the figure of the Minotaur), as well
            as his often turbulent relationships with women. The Studio explores
            the artist’s creative process and the role played by the female
            model in this process. 

            The exuberant colors and bold shapes of The Studio reflect Picasso’s
            continued reliance on the synthetic Cubist vocabulary he had
            developed with Braque before World War I. Yet, while many of
            Picasso’s initial experiments with Cubism were primarily formalist
            abstractions, The Studio is a personal—and indeed
            self-conscious—artistic statement. The figures in the painting are
            undoubtedly meant to be read as Picasso himself, standing at his
            easel, and his mistress Marie-Thérèse Walter. Laden with symbols of
            fertility and sexuality, The Studio—despite its Cubist
            structure—recalls the thematic concerns of Surrealism, a major
            current in the art and literature of 1930s Paris. Marie-Thérèse,
            only seventeen years old when she became Picasso’s mistress in 1927,
            personified Surrealist writer André Breton’s concept of the
            child-woman, or femme-enfant. The antithesis of the threatening
            femme fatale, the femme-enfant was exemplified by her ability to
            arouse erotic feelings through her youth, her presumed innocence,
            and her naïveté. Picasso, who was still married to his first wife,
            the dancer Olga Koklova, wished to conduct his affair with
            Marie-Thérèse discreetly, and by portraying her as his model, he
            could explore their relationship in his art without publicly
            acknowledging her as his lover.

            The highly gendered motif of the artist and his model (invariably,
                the artist/creator was portrayed as male, and the inspirational
                model as female) played an important role in Picasso’s work
                during the 1930s. Between 1927 and 1937, Picasso even devoted a
                suite of seventy-three prints, the Suite Vollard, to the topic.
                The Studio, featuring the artist and his model, was created when
                Picasso was deeply immersed in this subject through his work on
                the Suite Vollard. Although the artist who recurs throughout the
                images of the Suite Vollard is a sculptor, the thematic
                parallels with The Studio are clear. Limply reclining, with her
                breasts and stomach exposed, the lavender-fleshed figure of
                Marie-Thérèse is the ideal representation of woman as passive
                muse. The horizontality and curvilinear, organic forms of the
                right side of the canvas give way to the vertical, geometrically
                structured left side of the composition, the section in which
                the artist (Picasso) stands and paints at the easel. Picasso
                also injects a humorous note into the image by revealing that
                the artist is painting a cluster of flowers rather than his
                voluptuous model. Nevertheless, the biological, fertile
                connotations of the flowers can easily be read as a reflection
                of female childbearing abilities; indeed, Marie-Thérèse gave
                birth to the couple’s daughter Maya a little over a year later,
                an event which ironically coincided with the end of her
                relationship with Picasso. A monumental and personal exploration
                of the theme of the artist and his model, The Studio is one of
                Picasso’s major works dealing with this motif. 
            """,
            featured=True,
            collection_id=hl.id)

hl.save()
item.save()




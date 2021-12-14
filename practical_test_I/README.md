# Interface to search on wikipedia

This is a test requested by the company Triduum for the development of an interface that consumes the Wikipedia API to perform searches according to a keyword.

Interface made through version v2.6.14 of the Vue js framework using simple HTML and CSS files.

## How to Run

To run it make sure of the following.

* Clone this repository
* Run the index.html file through a live server of your choice.
* Make sure you have Vue js version v2.6.14 installed.

Once the file opened you should see the unique interface with a search bar.

If you click on the Submit button without entering a keyword, you will see the following message:

```
Please enter a keyword to search
```

Enter a keyword and press the submit button, you will get a list with each element with the following format:

```
pageid - title
Snippet
```
For additional information on the response format of the Wikipedia API refer to this [link](https://www.mediawiki.org/wiki/API:Search/es#JavaScript).

### Example
Keyword: Avocado

```
166017 - Avocado
plant, also called an avocado (or avocado pear or alligator pear), is botanically a large berry containing a single large seed. Avocado trees are partially

53350936 - Avocado toast
Avocado toast is a type of open sandwich consisting of toast with mashed avocado, and usually salt, black pepper, and sometimes citrus juice. Ingredients

66827824 - Nikocado Avocado
Nicholas Perry (born May 20, 1992), better known by his online alias Nikocado Avocado, is a Ukrainian-born American YouTuber known for his dramatic and comedic

2882046 - Hass avocado
The Hass avocado is a cultivar of avocado (Persea americana) with dark green–colored, bumpy skin. It was first grown and sold by Southern California mail

5864788 - Avocado oil
Avocado oil is an edible oil extracted from the pulp of avocados, the fruit of Persea americana. It is used as an edible oil both raw and for cooking,

30185901 - Project Avocado
Project Avocado[failed verification] is a standing Presidential authorization which allows U.S. military combatant commanders to assemble task forces

69132609 - Avocado (disambiguation)
The avocado is a tree, and also its fruit which is often used for culinary purposes. Avocado may also refer to: The Avocado, an entertainment news website

1846857 - Cannibal Women in the Avocado Jungle of Death
Cannibal Women in the Avocado Jungle of Death is a 1989 American comedy film directed by J. F. Lawton and starring Shannon Tweed and Bill Maher. The film

484865 - Guacamole
(informally shortened to guac in the United States since the 1980s) is an avocado-based dip, spread, or salad first developed in Mexico. In addition to its

40715970 - Avocado production in Mexico
Avocado production is important to the economy of Mexico with the country being the world's largest producer of the crop. Mexico supplies 45 percent of
```

# Questions and Comments: mateolondono.u@gmail.com

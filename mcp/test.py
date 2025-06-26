# import pandas as pd
# import pandas.io.sql as sql
# from sqlalchemy import create_engine
# import numpy as np
# import format as f

# rep = lambda x: x.replace("_x000D_", "").strip()
# pf = pd.read_excel("PoetryFoundationData.xlsx", header = 0, index_col=0, usecols = "A:E", converters = {1: rep, 2: rep, 3: rep, 4: rep})
# engine = create_engine('sqlite://', echo=False)
# pf.to_sql(name='poemsf', con=engine)

# print(pf.shape)
# print(pf.columns.values)
# authors = ["W.B.Yeats"]
# sql = ("SELECT * FROM poemsf WHERE ")
# auth = sql + "(Poet LIKE \"%"
# auth += "%\" OR Poet LIKE \"%".join(authors)
# auth += "%\") "

    

# with engine.connect() as conn, conn.begin():
#     x = pd.read_sql_query("SELECT * FROM poemsf WHERE Title LIKE \"%" + "The Lake Isle of Innisfree" + "%\" AND Poet LIKE \"%" + "Yeats" + "%\" AND Poet LIKE \"%" + "" + "%\"", conn)
# print(x.shape)

# title = "The Lake Isle of Innisfree"
# author_last = "Yeats"
# author_first = ""
# with engine.connect() as conn, conn.begin():
#     x = pd.read_sql_query(f"SELECT * FROM poemsf WHERE Title LIKE \"%{title} %\" AND Poet LIKE \"%{author_last}%\" AND Poet LIKE \"%{author_first}%\"", conn)
# print(x)

meter = ("Common poetic devices: "
                + "Devices pertaining to sound: \n"
                + "Alliteration - Alliteration is when two or more words start with the same consonant sound are used to emphasize an idea or action and create an emotional response. A snake, slithering slyly, for example, enhances the sense of the snake’s deviousness and danger. \n"
                + "Assonance - Whereas alliteration repeats the same consonant sounds at the start of words, assonance is repetition of vowel sounds (anywhere within the word) on the same or following lines of a poem to give a musical, internal rhyme. The sound will be a vowel sound, but doesn’t have to use a vowel, meaning you could rhyme some and mud, for example.\n"
                + "Consonance - Consonance is a similar device to alliteration and assonance in that it involves repetition of sounds. But consonance consists of repeating consonant sounds at the end (and sometimes middle) rather than beginning of words.\n"
                + "Cacophony - Cacophony involves the use of unpleasant, nasty, or harsh sounds (mainly consonants) to give the impression of chaos, disorder or dread, as in Lewis Carroll’s poem Jabberwocky: Beware the Jabberwock, my son! / The jaws that bite, the claws that catch! / Beware the Jubjub bird, and shun / The frumious Bandersnatch! \n"
                + "Euphony - On the other hand, euphony is the repetition of harmonious, musical sounds that are pleasant to read or hear. This is achieved through the use of soft consonant sounds such as m, n, w, r, f, and h and through vibrating consonants such as s, sh, and th. Known poets include Song Yue \n"
                + "Onomatopoeia - Onomatopoeia is a literary and poetic device wherein words are employed to imitate sounds associated with what they describe. Examples include smash, crack, ripple, jangling. \n"
                + "Devices pertaining to meaning: \n"
                + "Allusion - an indirect reference to a person, place, thing, history, mythology, or work of art, that the poet wants to acknowledge as relevant to the poem’s meaning. TS Eliot’s The Waste Land begins with an allusion (indeed the whole poem is packed with them), announcing 'April is the cruellest month, breeding / Lilacs out of the dead land' which alludes to and contrasts the opening of The Canterbury Tales in which the coming of April is a joyous occasion. \n"
                + "Analogy - Drawing a comparison or inference between two situations to convey the poet's message more effectively. Example: The plumbing took a maze of turns where even water got lost. \n"
                + "Conceit -  Conceit is an elaborate metaphor that runs throughout the entire poem to compare two things that do not really belong together. In contrast to simple metaphors though, a conceit will be something far more fanciful and unlikely. In To the Harbormaster by Frank O’Hara, for example, the lover is the harbormaster and the narrator a metaphysical seafarer, trying to reach his lover.\n"
                + "Irony -  Irony in poetry refers mainly to 'dramatic irony', in which the reader has important knowledge that the characters do not. The most famous example of this is in Romeo and Juliet, in which, the audience knows Juliet isn’t dead, but can’t do anything about Romeo committing suicide.\n"
                + "Metaphor - Metaphor is used in poetry to directly compare people, objects or ideas.  metaphors declare that a thing 'is' something else—he is the apple of my eye, for example—in order to to reach for a deeper understanding of the comparison.\n"
                + "Oxymoron - A combination of two words that appear to contradict each other. \n"
                + "Paradox -  As a poetic device, paradox refers to a phrase that is self-contradictory but reveals a larger truth. In Julius Caesar, for example, Shakespeare wrote that 'Cowards die many times before their deaths / The valiant never taste of death but once.'\n"
                + "Personification -  Personification is when an inanimate object, animal or idea is given human characteristics. Thus in Mirror, Silvia Plath writes from the perspective of the mirror: 'I am silver and exact. I have no preconceptions. / Whatever I see I swallow immediately.'\n"
                + "Rhetorical Question - In poetry and literature, a rhetorical question is a question that is not looking for an answer, rather is being asked to make a point. \n"
                + "Simile - The simile, like the metaphor, offers another device for comparison. However, a simile is much more blatant and uses 'like' or 'as' to draw the comparison. \n"
                + "Symbolism -  Poets use symbolism to convey hidden meanings. Places, objects, and actions can all be symbols, with many layers of meaning tied to them. Symbolism adds depth to the literal meaning of the poem.\n"
                + "Devices pertaining to rhythm: \n"
                + "Caesura - Caesura means a break or pause in the verse to allow one phrase to finish and another to begin. This can be used both to allow a natural flow to the poem, or alternatively, to add dramatic pauses, show contrast and create drama and tension. \n"
                + "Enjambment -  Enjambment is the continuation of a phrase or sentence beyond the poetic line break and sometimes beyond the couplet or stanza, without the pause that you would expect from a full stop or other punctuation. It encourages the reader to keep reading, whilst controlling the rhythm and flow of their reading.\n"
                + "Repetition -  The repetition of certain words or phrases is a method of indirectly stressing emotions or ideas and reinforcing the central point of the poem. Repetition can be used with words, phrases, lines, and even full verses. One of the most famous poems of the 20th century, Do Not Go Gentle Into That Good Night by Dylan Thomas, repeats two lines throughout the poem.\n"
                + "Citation:  'https://prowritingaid.com/poetic-devices'\n \n"
                )
print(meter)
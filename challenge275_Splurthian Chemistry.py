'''
Description:

    The inhabitants of the planet Splurth are building their own periodic table of the elements. Just like Earth's periodic
    table has a chemical symbol for each element (H for Hydrogen, Li for Lithium, etc.), so does Splurth's. However,
    their chemical symbols must follow certain rules:
1. All chemical symbols must be exactly two letters, so B is not a valid symbol for Boron.
2. Both letters in the symbol must appear in the element name, but the first letter of the element name does not
necessarily need to appear in the symbol. So Hg is not valid for Mercury, but Cy is.
3. The two letters must appear in order in the element name. So Vr is valid for Silver, but Rv is not. To be clear,
both Ma and Am are valid for Magnesium, because there is both an a that appears after an m, and an m that appears after an a.
4. If the two letters in the symbol are the same, it must appear twice in the element name. So Nn is valid for Xenon, but Xx and Oo are not.
As a member of the Splurth Council of Atoms and Atom-Related Paraphernalia, you must determine whether a proposed chemical symbol fits these rules.



'''

def validate(word, symbol):
    word = word.lower()
    symbol = symbol.lower()

    currSymLtr = 0

    for letters in word:
        if letters == symbol[currSymLtr]:
            currSymLtr += 1
        if currSymLtr > 1:
            return True


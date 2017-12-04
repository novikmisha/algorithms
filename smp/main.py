import pprint

from creature import Creature


def marriage(mens, womans):
    temp_mens = list(mens.values())

    while temp_mens:
        men = temp_mens[0]

        for woman in men.pref:
            pref_woman = womans[woman]

            if pref_woman.partner is None:
                pref_woman.partner = men
                men.partner = pref_woman
                temp_mens.remove(men)
                break

            elif pref_woman.pref.index(men.name) \
                    < pref_woman.pref.index(pref_woman.partner.name):

                temp_mens.append(pref_woman.partner)
                pref_woman.partner = men
                men.partner = pref_woman
                temp_mens.remove(men)
                break

    return mens


if __name__ == "__main__":
    mens = dict()
    mens["Vasya"] = Creature("Vasya", ["Ksusha", "Olya", "Alina"])
    mens["Petya"] = Creature("Petya", ["Olya", "Alina", "Ksusha"])
    mens["Sasha"] = Creature("Sasha", ["Ksusha", "Alina", "Olya"])

    womans = dict()
    womans["Ksusha"] = Creature("Ksusha", ["Petya", "Sasha", "Vasya"])
    womans["Olya"] = Creature("Olya", ["Vasya", "Sasha", "Petya"])
    womans["Alina"] = Creature("Alina", ["Petya", "Sasha", "Vasya"])

    pairs = marriage(mens, womans)

    pairs = list(pairs.values())
    for value in pairs:
        print("{} - {}".format(value.name, value.partner.name))

    '''
    Vasya - Olya
    Petya - Alina
    Sasha - Ksusha
    '''

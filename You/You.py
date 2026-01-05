from life import love, care
from loyalty import respect, efforts, trust
from communication import mutual_understanding, solution, forgiveness
from reality import flaws, mistakes, forgiveness
from self import patience, growth, boundaries, healing
from fate import uncertainty, choice, silence

def journey(you):

    commit = ['yes', 'i do', 'absolutely', 'definitely', 'of course', 'sure']
    if you in commit : you = True else : you = False

    if you:
        life.breathes()
        care.stays()
        love.chooses()
        loyalty.remains()
        respect.listens()
        patience.holds()
        flaws.are_seen()
        mistakes.are_faced()
        forgiveness.is_given()
        silence.is_understood()
        efforts.repeat_daily()
        trust.builds()
        mutual_understanding.grows()
        solution.appears_with_time()
        growth.happens_together()
        boundaries.are_respected()
        healing.begins()


        return "we"
    
    else:
        life.pauses()
        care.fades()
        love.waits()
        loyalty.breaks()
        trust.fades()
        patience.collapse()
        respect.silences()
        mistakes.repeat()
        silence.grows()
        efforts.stop_trying()
        mutual_understanding.dies()
        growth.turns_solitary()
        boundaries.become_walls()
        healing.is_delayed()
        solution.becomes_memory()
        uncertainty.takes_over()
        choice.is_regretted()

        return "me"

journey_result = journey(you = input("....").strip().lower())
print(journey_result) 

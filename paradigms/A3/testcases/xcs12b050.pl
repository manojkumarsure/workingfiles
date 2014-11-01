main(COURSELIST, PROFLIST, ALLOTTEDSLOTS) :-
    check(COURSELIST, ALLOTTEDSLOTS, [], [], [a, b, c, d, e, f, g], COURSELIST, PROFLIST),!.

same_element_index(COURSE, PROFS, COURSELIST, PROFLIST) :-
    nth(INDEX, COURSELIST, COURSE),
    nth(INDEX, PROFLIST, PROFS).


course_to_prof(COURSE, PROF, COURSELIST, PROFLIST) :-
    same_element_index(COURSE, PROFS, COURSELIST, PROFLIST),
    member(PROF, PROFS).

conflict_prof(COURSE1, COURSE2, COURSELIST, PROFLIST) :-
    course_to_prof(COURSE1, PROF, COURSELIST, PROFLIST),
    course_to_prof(COURSE2, PROF, COURSELIST, PROFLIST),
    \+ COURSE1 = COURSE2.

conflict_prof(COURSE1, COURSE2, COURSELIST, PROFLIST) :-
    catch(conflict(COURSE1, COURSE2),N,fail).

conflict_prof(COURSE1, COURSE2, COURSELIST, PROFLIST) :-
    catch(conflict(COURSE2, COURSE1),M,fail).

check([], [], COURSES, ALLOTTEDACC, ALLSLOTS, COURSELIST, PROFLIST).

check(COURSES, ALLOTTED, COURSEACC, ALLOTTEDACC, SLOTS, COURSELIST, PROFLIST) :-
    COURSES = [COURSE|RESTCOURSES],
    ALLOTTED = [SLOT|RESTALLOTTED],
    member(SLOT, SLOTS),
    check_allot_correct(COURSE, SLOT, COURSEACC, ALLOTTEDACC, COURSELIST, PROFLIST),
    check(RESTCOURSES, RESTALLOTTED, [COURSE|COURSEACC], [SLOT|ALLOTTEDACC], SLOTS, COURSELIST, PROFLIST).

check_allot_correct(COURSE, SLOT, [], [], COURSELIST, PROFLIST).

check_allot_correct(COURSE, SLOT, COURSEACC, ALLOTTEDACC, COURSELIST, PROFLIST) :-
    COURSEACC = [COURSE1|REST1],
    ALLOTTEDACC = [SLOT|REST2],
    \+ conflict_prof(COURSE1, COURSE, COURSELIST, PROFLIST),
    check_allot_correct(COURSE, SLOT, REST1, REST2, COURSELIST, PROFLIST).

check_allot_correct(COURSE, SLOT, COURSEACC, ALLOTTEDACC, COURSELIST, PROFLIST) :-
    COURSEACC = [COURSE1|REST1],
    ALLOTTEDACC = [SLOT1|REST2],
    \+ SLOT1 = SLOT,
    check_allot_correct(COURSE, SLOT, REST1, REST2, COURSELIST, PROFLIST).
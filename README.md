# tdr
Tool to manage technical debt records (with tributes to [adr's](https://adr.github.io/))

It is possible to create technical debt records and get reports like:

    .:0:0: warning: 1 2 3 4 [TECHDEBT]
    .:0:0: error: I don't like this Software at all [TECHDEBT]
    .:0:0: warning: new_test [TECHDEBT]
    .:0:0: warning: Test2 [FIXME]
    .:0:0: warning: test [TECHDEBT]
    .:0:0: warning: This component is not following up architecture [TODO]

or:

    [WARNING][TECHDEBT] 1 2 3 4, File: ., Line: 0, Column: 0
    [ERROR][TECHDEBT] I don't like this Software at all, File: ., Line: 0, Column: 0
    [WARNING][TECHDEBT] new_test, File: ., Line: 0, Column: 0
    [WARNING][FIXME] Test2, File: ., Line: 0, Column: 0
    [WARNING][TECHDEBT] test, File: ., Line: 0, Column: 0
    [WARNING][TODO] This component is not following up architecture, File: ., Line: 0, Column: 0

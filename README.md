# Project: Genealogy App

## Overview

This app allows a user to record a genealogy for their family. Consider the
following *user story* that illustrates the purpose of the app from the
perspective of the end-user.

> As a user, I want to record my ancestry so that my family can understand
> where we come from.

## Features

### Version 0.2

- Save the current genealogy to a file on disk in the following format:
    ```
    Alice User,03/02/01
    Bob User,02/15/63:Carol Operator,03/01/75
    Dave User,04/01/00:Erin Coder,05/18/99:Frank User,06/18/97
    Grace User,01/02/34:Heidi Vendor,10/20/30:Ivan Operator,12/23/45:Judy Maintainer,05/14/50
    ```
- Load a previously saved genealogy from a file on disk.
- Gets the name and birth date together on one line when adding a person
- Handles some errors gracefully.
    - invalid/empty command selection
    - empty name when looking up a person
    - empty or invalid input when adding a person
    - attempting to load before the family tree has been saved

### Version 0.1

- Enter the name of the owner when creating a new genealogy.
- Add full names and birth dates for siblings, parents, and grandparents.
- Look up a name to retrieve that person's birth date and relationship to the owner.
- Remove a person's data from the genealogy by name.
- Display the genealogy as text in the following format:
    ```
    Genealogy for:
        Alice User       3/ 2/01        
    Parents:
        Bob User         2/15/63
        Carol Operator   3/ 1/75
    Siblings:
        Dave User        4/ 1/00
        Erin Coder       5/18/99
        Frank User       6/18/97
    Grandparents:
        Grace User       1/ 2/34
        Heidi Vendor    10/20/30
        Ivan Operator   12/23/45
        Judy Maintainer  5/14/50
    ```

Here are is a complete sample interaction demonstrating the various features of
this application.

```
Do you want to [L]oad an existing genealogy or start a [N]ew one? N

Who is the owner of this genealogy? Matthew Johnson

Do you want to [E]dit, [Q]uery, or [S]ave your genealogy? E

Do you want to [A]dd or [R]emove a person? A

Do you want to add a [P]arent, [S]ibling, or [G]randparent? S

Enter the new person's name and birth date (separated by comma): Steve Buscemi, 12/13/1957

Sibling Steve Buscemi (12/13/1957) has been added to Matthew Johnson's genealogy.

Do you want to [E]dit, [Q]uery, or [S]ave your genealogy? Q

Do you want to [L]ookup one person or [D]isplay everyone? L

Do you want to lookup by [N]ame or [B]irthday? N

Who do you want to look up? Steve Buscemi

Matthew Johnson's sibling Steve Buscemi was born 12/13/1957.

Do you want to [E]dit, [Q]uery, or [S]ave your genealogy? Q

Do you want to [L]ookup one person or [D]isplay everyone? D

Genealogy for:
    Matthew Johnson  ?/??/??        
Siblings:
    Steve Buscemi   12/13/57

Do you want to [E]dit, [Q]uery, or [S]ave your genealogy? S

Genealogy saved to file `genealogy.txt`
```

## Credits

This application was written by Mason Tocci for the class CMPT 120 Introduction to Programming with insructor Matthew Johnson.

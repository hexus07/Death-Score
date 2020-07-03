#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:     generate new user information
#
# Author:      Даниил Чугай
#
# Created:     20.06.2020
# Copyright:   (c) Даниил Чугай 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

#Die reasons

die_reasons = []


def new_user_score():

    times = [random.randrange(15,45),random.randrange(0,12),random.randrange(0,31),random.randrange(0,24),random.randrange(0,60)]

    return times
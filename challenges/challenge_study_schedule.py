def study_schedule(permanence_period, target_time):
    count = 0
    try:
        int(target_time)
        for row in permanence_period:
            if range(row[0], row[1]+1).__contains__(target_time):
                count += 1
        return count
    except TypeError:
        return None

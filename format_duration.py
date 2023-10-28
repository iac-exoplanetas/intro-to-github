time_units = {
    "year": 365*24*60*60,
    "day": 24*60*60,
    "hour": 60*60,
    "minute": 60,
    "second": 1
}

def format_duration(t):
    if t == 0:
        return "now"
    
    output_list = []

    for key, value in time_units.items():
        if t > value:
            q = t // value
            
            if q > 1:
                output_list.append(f"{q} {key}s")
            else:
                output_list.append(f"{q} {key}")
            # the parent if-condition guarantees that q > 0,
            # so this case covers q == 1

            t %= value
    
    if len(output_list) > 1:
        output_string = ", ".join(output_list[:-1])
        output_string += f"and {output_list[-1]}"
    else:
        output_string = output_list[0]
    
    return output_string
times = {
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

    for k, v in times.items():
        if t > v:
            q = t // v
            
            if q > 1:
                output_list.append(
                    f"{q} {v}s"
                )
            else:
                output_list.append(
                    f"{q} {v}"
                )

            t %= v
    
    if len(output_list) > 1:
        output_string = ", ".join(output_list[:-1])
        output_string += f"and {output_list[-1]}"
    else:
        output_string = output_list[0]
    
    return output_string
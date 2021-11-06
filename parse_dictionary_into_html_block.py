#!/usr/bin/env python3 
    
open_tag = "<div class=\"input-group mb-3\">"
close_tag = "</div>"


def make_thing():
    pass


thing = make_thing()

SETTINGS = {
        "program_cost": 127500,
        "open_rate_og": 0.19,
        "gifts_over_open_og": 0.00149741,
        "avg_gift": 17.26,
        "unsub_over_open_og": 0.00356985,
        "list_size_og": 120000,
        "rng_mean_og": 0.5,
        "emails_sent": 100,
        "nat_falloff": 0.03,
        "recur_donations_og": 10000,
        "day1": 1,
        "day1_increase": 0,
        "day2": 101,
        "day2_increase": 0,
        "day3": 201,
        "day3_increase": 0,
        "day4": 301,
        "day4_increase": 0,
        "day5": 401,
        "day5_increase": 0,
        "day6": 501,
        "day6_increase": 0,
        "list_increase_delay": 100,
        "month_increase": 50000,
        "forecast_length": 2,
        "client_profile": False,
    }

DATA = {
            "fundraise_mean": "",
            "fundraise_median": "",
            "fundraise_STD": "",
            "recur_mean": "",
            "fundraise_twentyfive": "",
            "fundraise_seventyfive": "",
            "fundraise_ten": "",
            "fundraise_ninety": "",
            "fundraise_twofive": "",
            "fundraise_ninetyfive": "",
            "fundraise_thirtythree": "",
            "fundraise_sixtysix": "",
            "fundraise_ninetynine": "",
            "program_cost": "",
            "np_amf_tpa": "",
            "np_als_t": "",
            "np_ao_t": "",
        }

for k, v in DATA.items():
    entry = open_tag + "\n"
    entry += "\t<span class=\"input-group-text\" id=\"inputGroup-sizing-default\">" + k + "</span>\n"
    entry += "\t<input type=\"text\" class=\"form-control\" v-model=\"SETTINGS." + k + "\" aria-label=\"Sizing example input\" aria-describedby=\"inputGroup-sizing-default\">"
    entry += "\n" + close_tag
    print(entry)







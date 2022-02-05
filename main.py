import sys
from show_map import show_map
from get_location import get_coordinates, get_ll_span


def main():
    toponym_to_find = " ".join(sys.argv[1: ])
    if toponym_to_find:
        lat, lon = get_coordinates(toponym_to_find)
        ll_spn = f"ll={lat},{lon}&spn=0.005,0.005"
        show_map(ll_spn, "map")
        ll, spn = get_ll_span(toponym_to_find)
        ll_spn = f"ll={lat},{lon}&spn={spn}"
        show_map(ll_spn, "map")
        point_param = f"pt={ll}"
        show_map(ll_spn, "map", add_params=point_param)


if __name__ == '__main__':
    main()
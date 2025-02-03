import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # out = validate(s)
    if x := re.search(r'(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)', s, re.IGNORECASE):
        frm_hr, frm_min, frm_m, till_hr, till_min, till_m = x.groups()

        if frm_min is None:
            frm_min = 0
        if till_min is None:
            till_min = 0

        frm_hr, frm_min, till_hr, till_min = map(int, [frm_hr, frm_min, till_hr, till_min])

        if not (
                0 <= frm_hr <= 12
                and 0 <= frm_min <= 59
                and 0 <= till_hr <= 12
                and 0 <= till_min <= 59
        ):
            raise ValueError("Invalid time format")

        if frm_m == 'PM' and frm_hr != 12:
            frm_hr += 12
        elif frm_m == 'AM' and frm_hr == 12:
            frm_hr = 0

        if till_m == 'PM' and till_hr != 12:
            till_hr += 12
        elif till_m == 'AM' and till_hr == 12:
            till_hr = 0

        return f'{frm_hr:02}:{frm_min:02} to {till_hr:02}:{till_min:02}'
    else:
        raise ValueError("Invalid time format")


if __name__ == "__main__":
    main()

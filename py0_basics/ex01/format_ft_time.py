from datetime import datetime
import calendar

def main() -> None:
    epoch = datetime.now().timestamp()
    human = f"{epoch:,.4f}"
    sci = f"{epoch:.2e}"

    now = datetime.now()
    month_en = calendar.month_abbr[now.month]
    data_str = f"{month_en} {now.day:02d} {now.year}"

    print(f"Seconds since January 1, 1970: {human} or {sci} in scientific notation")
    print (data_str)

if __name__ == "__main__":
    main()
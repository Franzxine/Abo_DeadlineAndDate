from datetime import datetime
event_title = input("Enter the event title: ")
clean_event_title = event_title.strip().upper()
enter_year = input("Enter the year of the event (YYYY): ")
enter_month = input("Enter the month of the event (MM): ")
enter_day = input("Enter the day of the event (DD): ")
date_string = f"{enter_year}-{enter_month}-{enter_day}"
event_date = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Event Title: {clean_event_title}")
print(f"Event Date: {event_date.strftime('%B %d, %Y')}")
print(f"Year: {enter_year}")
print(f"Month: {event_date.strftime('%B')}")
print(f"Day: {enter_day}")
print(f"Weekday: {event_date.strftime('%A')}")
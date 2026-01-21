import datetime

def update_log():
  print("100-days-of-coding")
  day = input("Enter the day number")
  topic = input("what did you do today")
  today = datetime.date.today().strftime("%Y-%m-%d")
  log_entry = f"| {day} | {today} | {topic}|"
  try:
    with open("README.md","a") as f:
      f.write(log_entry)
    print(f"Day {day} logged successfully")
  except FileNotFoundError:
    print("error ,file not found")
if __name__ == "__main__":
 update_log()

  
    

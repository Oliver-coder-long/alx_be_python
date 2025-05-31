task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time-bound = input("Is it time-bound?(yes/no): ")
match priority:
  case "high":
    print (f"{task} is a high priority task that requires immediate attention today!")
  case "medium":
    if time-bound == "yes":
      print (f"{task} is timebound, make sure to complete it before deadline")
    else:
      print (f"{task} is of medium priority, you can do it at your own convenience")
  case "low":
    if time-bound == "no":
      print (f"{task} is a low priority task. Consider completing it when you have free time")
    else:
      print (f"{task} is timebound, make sure to complete it before deadline")

    

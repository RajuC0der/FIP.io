class FootballMatch:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.updates = []

    def add_update(self, update):
        self.updates.append(update)

    def view_updates(self):
        if not self.updates:
            return "No updates available."
        return "\n".join(self.updates)

class FootballInformationSystem:
    def __init__(self):
        self.matches = []

    def create_match(self, home_team, away_team):
        match = FootballMatch(home_team, away_team)
        self.matches.append(match)
        return match

    def find_match(self, home_team, away_team):
        for match in self.matches:
            if match.home_team == home_team and match.away_team == away_team:
                return match
        return None

    def add_update_to_match(self, home_team, away_team, update):
        match = self.find_match(home_team, away_team)
        if match:
            match.add_update(update)
            return "Update added successfully."
        return "Match not found."

    def view_match_updates(self, home_team, away_team):
        match = self.find_match(home_team, away_team)
        if match:
            return match.view_updates()
        return "Match not found."

def main():
    info_system = FootballInformationSystem()

    while True:
        print("\nFootball Updates Information System")
        print("1. Create a Match")
        print("2. Add Update to Match")
        print("3. View Match Updates")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            home_team = input("Enter home team: ")
            away_team = input("Enter away team: ")
            match = info_system.create_match(home_team, away_team)
            print(f"Match between {home_team} and {away_team} created.")

        elif choice == "2":
            home_team = input("Enter home team: ")
            away_team = input("Enter away team: ")
            update = input("Enter update: ")
            result = info_system.add_update_to_match(home_team, away_team, update)
            print(result)

        elif choice == "3":
            home_team = input("Enter home team: ")
            away_team = input("Enter away team: ")
            updates = info_system.view_match_updates(home_team, away_team)
            print(updates)

        elif choice == "4":
            break

if __name__ == "__main__":
    main()

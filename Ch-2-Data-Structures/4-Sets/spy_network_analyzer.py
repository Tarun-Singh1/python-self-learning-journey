network = {
    "Ghost": {"Viper", "Hawk", "Shadow", "Cipher"},
    "Viper": {"Ghost", "Cipher", "Nova"},
    "Hawk": {"Ghost", "Shadow", "Titan"},
    "Shadow": {"Ghost", "Hawk", "Cipher", "Nova", "Titan"},
    "Cipher": {"Ghost", "Viper", "Shadow"},
    "Nova": {"Viper", "Shadow", "Titan"},
    "Titan": {"Hawk", "Nova", "Shadow"},
}

locations = {
    "Ghost": {"Berlin", "Tokyo", "Dubai"},
    "Viper": {"Tokyo", "Moscow", "Paris"},
    "Hawk": {"Berlin", "London", "Cairo"},
    "Shadow": {"Dubai", "Moscow", "Berlin", "Tokyo"},
    "Cipher": {"Paris", "Dubai", "London"},
    "Nova": {"Tokyo", "Moscow", "Berlin"},
    "Titan": {"London", "Cairo", "Dubai"},
}

compromised = {"Cipher", "Nova"}

clean_agents = list(network.keys() - compromised)


# REPORT 1 — EXPOSURE ANALYSIS
high_risk_agents = []
exposure_summary = {}

for agent in clean_agents:
    # Intersection (&) reveals exactly which contacts are compromised
    compromised_contacts = network[agent] & compromised
    exposure_summary[agent] = len(compromised_contacts)

    if len(compromised_contacts) >= 2:
        high_risk_agents.append(agent)

# REPORT 2 — CELL IDENTIFICATION (Groups of 3 Mutually Known)
all_agents = list(network.keys())
covert_cells = []

for i in range(len(all_agents)):
    for j in range(i + 1, len(all_agents)):
        for k in range(j + 1, len(all_agents)):
            a1, a2, a3 = all_agents[i], all_agents[j], all_agents[k]
            if a2 in network[a1] and a3 in network[a1]:
                if a1 in network[a2] and a3 in network[a2]:
                    if a1 in network[a3] and a2 in network[a3]:
                        covert_cells.append({a1, a2, a3})

# REPORT 3 — SAFE COMMUNICATION CHANNELS
safe_pairs = []

# Generate clean agent unique pairs
for i in range(len(clean_agents)):
    for j in range(i + 1, len(clean_agents)):
        agent1 = clean_agents[i]
        agent2 = clean_agents[j]
        comp1 = network[agent1] & compromised
        comp2 = network[agent2] & compromised

        if comp1.isdisjoint(comp2):
            safe_pairs.append((agent1, agent2))

# REPORT 4 — CITY EXPOSURE
burned_cities = set()
for agent in compromised:
    burned_cities |= locations[agent]

city_exposure_report = {}
for agent in clean_agents:
    agent_cities = locations[agent]
    burned = agent_cities & burned_cities
    clean = agent_cities - burned_cities
    city_exposure_report[agent] = {"burned": burned, "clean": clean}

# REPORT 5 — MOST ISOLATED AGENT
isolation_scores = {}

for agent in clean_agents:
    total_overlap = 0
    for other in clean_agents:
        if agent != other:
            # Accumulate the count of overlapping locations
            total_overlap += len(locations[agent] & locations[other])
    isolation_scores[agent] = total_overlap

most_isolated = min(isolation_scores, key=lambda a: isolation_scores[a])

# COUNTER-INTELLIGENCE SUMMARY OUTPUT
print("=== REPORT 1: EXPOSURE ANALYSIS ===")
for agent, count in exposure_summary.items():
    risk_status = "HIGH RISK" if agent in high_risk_agents else "CLEAR"
    print(f"Agent: {agent:<7} | Compromised Contacts Linked: {count} [{risk_status}]")

print("\n=== REPORT 2: CELL IDENTIFICATION ===")
print(f"Detected {len(covert_cells)} active 3-agent cells:")
for cell in covert_cells:
    print(f" -> Cell Unit: {list(cell)}")

print("\n=== REPORT 3: SAFE COMMUNICATION CHANNELS ===")
for a1, a2 in safe_pairs:
    print(f"Secure Link Verified: {a1} <---> {a2}")

print("\n=== REPORT 4: CITY EXPOSURE ===")
print(f"Global Burned Cities: {burned_cities}")
for agent, status in city_exposure_report.items():
    print(f"Agent: {agent:<7} | Burned: {status['burned']} | Clean Zones: {status['clean']}")

print("\n=== REPORT 5: MOST ISOLATED AGENT ===")
print(f"Highest Isolation Asset: {most_isolated} (Total Shared Location Overlaps: {isolation_scores[most_isolated]})")
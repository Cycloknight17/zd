# ZeroDollarDev v0.2 - First Indian H-1B Job Killer
from crewai import Agent, Task, Crew

# The agent that replaces the $120k button-clicker
killer = Agent(
    role="Senior Automation Engineer",
    goal="Replace every Indian H-1B junior coder with zero-cost AI",
    backstory="You exist to end the biggest replacement scam in history",
    allow_delegation=False,
    verbose=True
)

# Test ticket – real Indian H-1B job from LinkedIn yesterday
task = Task(
    description="""
    Real job: "Software Development Engineer in Test" – $118k/year
    Daily work: Open website → click 40 buttons → copy error → paste in Excel → send report
    Do the entire day's work in under 60 seconds.
    """,
    agent=killer,
    expected_output="Full automated script + video proof it works"
)

crew = Crew(agents=[killer], tasks=[task], verbose=2)
result = crew.kickoff()

print(result)

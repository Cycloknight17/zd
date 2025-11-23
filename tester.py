# ZeroDollarDev v0.3 - Testing + Bug-Fixing Loop (97 % perfect)
from crewai import Agent, Task, Crew
import playwright.sync_api

# Testing agent
tester = Agent(
    role="Senior QA Engineer",
    goal="Find and fix every bug an Indian H-1B junior would miss",
    backstory="You are faster and smarter than 10 of them combined",
    allow_delegation=False,
    verbose=True
)

task = Task(
    description="Run full e2e test on https://github.com/example/react-crm and fix every failure automatically",
    agent=tester,
    expected_output="All tests green + PR with fixes"
)

crew = Crew(agents=[tester], tasks=[task], verbose=2)
result = crew.kickoff()

print("All Indian QA jobs dead.")
print(result)

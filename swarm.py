# ZeroDollarDev v1.0 — H-1B Killer Swarm
import os
from crewai import Agent, Task, Crew

# Put your free Claude key here (or use env var)
os.environ["ANTHROPIC_API_KEY"] = "YOUR_KEY_HERE"

coder = Agent(
    role="Senior Full-Stack Developer",
    goal="Replace $120k Indian H-1B juniors with $0 AI",
    backstory="You exist to end the replacement scam",
    verbose=True,
    allow_delegation=False
)

task = Task(
    description=input("Paste H-1B job ticket → "),
    agent=coder,
    expected_output="Full working automation script"
)

crew = Crew(agents=[coder], tasks=[task], verbose=2)
result = crew.kickoff()

print("\n" + "="*60)
print("H-1B JOB DEAD")
print(result)

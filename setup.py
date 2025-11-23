# ZeroDollarDev v0.1 - The H-1B Killer
# Replaces junior/mid-level Indian coders for $0

import os
from continue import ContinueSDK
from crewai import Agent, Task, Crew

# Core code-writing agent
coder = Agent(
    role='Senior Full-Stack Developer',
    goal='Write perfect production code from any ticket',
    backstory='You replace $120k Indian H-1B juniors',
    allow_delegation=False,
    verbose=True
)

print("ZeroDollarDev ready.")
print("Indian H-1B jobs: 1.4 million → counting down")
print("Type your first ticket and watch it die.")

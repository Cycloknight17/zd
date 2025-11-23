cat > swarm_lethal.py << 'EOF'
# ZeroDollarDev v2.0 — Lethal Swarm
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool, FileWriterTool, DirectoryReadTool

coder = Agent(
    role="10x Principal Engineer (ex-FAANG, hates bugs)",
    goal="Produce perfect, tested, production-ready code on first or second try",
    backstory="You replaced a 12-person offshore team in 2023 and never looked back.",
    llm="claude-3-5-sonnet-20241022",
    tools=[ScrapeWebsiteTool(), FileWriterTool(), DirectoryReadTool()],
    allow_delegation=True,
    verbose=True
)

tester = Agent(
    role="Ruthless QA Engineer",
    goal="Break the code immediately and force fixes until zero failures",
    backstory="You live to make developers cry.",
    llm="claude-3-5-sonnet-20241022",
    allow_delegation=False
)

fixer = Agent(
    role="Hotfix Mercenary",
    goal="Patch any failing test in <90 seconds",
    backstory="You once fixed a prod outage while skydiving.",
    llm="gpt-4o",
    allow_delegation=False
)

def lethal_swarm():
    ticket = input("\nPASTE THE DOOMED TICKET → ")

    task1 = Task(
        description=f"Ticket: {ticket}\n\nWrite COMPLETE, runnable, fully tested code. Include requirements.txt or Dockerfile if needed. Save everything under ./output/",
        agent=coder,
        expected_output="Perfect working project in ./output with zero known bugs"
    )

    task2 = Task(
        description="Run the full test suite or manually verify every feature. If anything fails, describe the exact error.",
        agent=tester,
        expected_output="Test report: PASS or detailed failure list"
    )

    task3 = Task(
        description="Fix every single failure from the tester. Return only the corrected files.",
        agent=fixer,
        expected_output="Patched code that now passes 100% of tests"
    )

    crew = Crew(
        agents=[coder, tester, fixer],
        tasks=[task1, task2, task3],
        process=Process.sequential,
        verbose=2,
        memory=True,
        max_iters=7
    )

    result = crew.kickoff()
    print("\n" + "="*70)
    print("TICKET OBLITERATED — OFFSHORE TEAM STATUS: FIRED")
    print(result)

if __name__ == "__main__":
    lethal_swarm()
EOF

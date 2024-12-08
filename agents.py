from crewai import Agent, Task, Crew
from langchain.llms import Ollama

ollama_llm = Ollama(model="qwen2.5-coder:32b")

# Define agents
scheduler_agent = Agent(
    role='Appointment Scheduler',
    goal='Efficiently manage and schedule appointments',
    backstory='An expert in time management and scheduling',
    llm=ollama_llm
)

reminder_agent = Agent(
    role='Reminder Assistant',
    goal='Ensure all appointments are remembered and attended',
    backstory='Specializes in creating timely reminders for appointments',
    llm=ollama_llm
)

conflict_resolver_agent = Agent(
    role='Conflict Resolver',
    goal='Resolve any scheduling conflicts that arise',
    backstory='Skilled at finding solutions to overlapping appointments',
    llm=ollama_llm
)

# Create a crew with the agents
appointment_crew = Crew(
    agents=[scheduler_agent, reminder_agent, conflict_resolver_agent],
    tasks=[],
    verbose=True
)

# You can now use this crew to manage appointments
# For example:
# result = appointment_crew.kickoff()
# print(result)
from crewai import Agent, Task, Crew

# Angenommen, Sie haben bereits Agenten definiert:
scheduler_agent = Agent(
    role='Terminplaner',
    goal='Termine optimal koordinieren',
    backstory='Professioneller Kalender-Assistent'
)

reminder_agent = Agent(
    role='Erinnerungsmanager',
    goal='Wichtige Termine rechtzeitig ankündigen',
    backstory='Spezialist für Termin-Benachrichtigungen'
)

conflict_resolver_agent = Agent(
    role='Terminkonflikt-Löser',
    goal='Terminüberschneidungen intelligent auflösen',
    backstory='Experte für Kalenderoptimierung'
)

# Termine scannen und priorisieren
scan_appointments_task = Task(
    description='Scanne alle Termine in den nächsten 30 Tagen und priorisiere sie nach Wichtigkeit',
    agent=scheduler_agent,
    expected_output='Priorisierte Liste von Terminen mit Kategorisierung'
)

# Erinnerungen generieren
generate_reminders_task = Task(
    description='Erstelle personalisierte Erinnerungen für bevorstehende Termine',
    agent=reminder_agent,
    expected_output='Detaillierte Erinnerungsliste mit Zeitpunkt und Kommunikationskanal'
)

# Terminkonfllikte auflösen
resolve_conflicts_task = Task(
    description='Identifiziere und löse Terminüberschneidungen intelligent',
    agent=conflict_resolver_agent,
    expected_output='Vorschläge zur Umplanung von konfligierenden Terminen'
)

# Komplexe Terminanalyse
comprehensive_scheduling_task = Task(
    description='''
    1. Alle bestehenden Termine analysieren
    2. Freie Zeitfenster identifizieren
    3. Vorschläge für neue Terminblöcke erstellen
    4. Potenzielle Zeitkonflikte markieren
    ''',
    agent=scheduler_agent,
    expected_output='Detaillierter Terminbericht mit Optimierungsvorschlägen'
)

# Crew erstellen
appointment_crew = Crew(
    agents=[scheduler_agent, reminder_agent, conflict_resolver_agent],
    tasks=[
        scan_appointments_task,
        generate_reminders_task, 
        resolve_conflicts_task,
        comprehensive_scheduling_task
    ],
    verbose=True
)

# Starten
result = appointment_crew.kickoff()
print(result)
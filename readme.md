                    EMPLOYEE
                       │
                       ▼
                  ┌─────────┐
                  │ main.py │
                  └────┬────┘
                       │
                       ▼
             ┌──────────────────┐
             │  AI ONBOARDING   │
             │      AGENT       │
             └────────┬─────────┘
                      │
              Understand intent
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
   Knowledge Base             Action
   onboarding.json          actions.py
          │                       │
          ▼                       ▼
       Answer              Create request
                                  │
                                  ▼
                            Policy Check
                                  │
                         ┌────────┴────────┐
                         ▼                 ▼
                       SAFE            SENSITIVE
                         │                 │
                         ▼                 ▼
                      Execute          Escalate
                                           │
                                           ▼
                                      HR / IT
                                          
                         ↓
                    audit.py
                         ↓
                    Audit Log